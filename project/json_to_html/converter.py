import json
import os
import re
from html import escape


class HTMLClassIdFormatter:
    """Class that transform text-strings to html-format text"""

    def _get_tag_classes_id(self, text_value):
        class_ = []
        id_ = ''

        tag, *items = re.split('[.#]', text_value)
        prefixs = re.findall('[.#]', text_value)
        if items:
            items[-1] = items[-1].rstrip('>') # strip last symbol in strings like 'my-class2">'

        for prefix, value in zip(prefixs, items):
            if prefix == '#':
                id_ = value
            else:
                class_.append(value)

        return tag, ' '.join(class_), id_

    def format_key(self, text):
        """Transform expressions like 'p.my-class1.my-class2' to next format '<p class="my-class1 my-class2">' """
        tag, classes, id_ = self._get_tag_classes_id(text)
        id_text = f' id="{id_}"' if id_ else ''
        classes_text = f' class="{"".join(classes)}"' if classes else ''

        transformed = f'{tag}{id_text}{classes_text}>'
        closed_tag = f'</{tag[1:]}>'

        return transformed, closed_tag


class HTMLTagsWrapperFactory(HTMLClassIdFormatter):
    """
    Class that makes html-tags from text,
    stores it in cache and return outside.
    """
    __close_tags_stack = [] # it used for keep close tags with recursion function self._parse_json_list

    def __init__(self):
        self.__tags_cache = {}
        self._parsed_json = []

    def _get_pair_tags(self, open_tag):
        self.pair_tags = self.__tags_cache.get(open_tag)

        if not self.pair_tags:  # save new tags to cache
            self.__tags_cache[open_tag] = (f'<{open_tag}>', f'</{open_tag}>')

        return self.__tags_cache[open_tag]

    def _parse_json_list(self, obj):
        if isinstance(obj, dict):
            self._parsed_json.append('<li>')
            for key, value in obj.items():
                open_close_tags = self._get_pair_tags(key)
                open_tag = open_close_tags[0]
                HTMLTagsWrapperFactory.__close_tags_stack.append(
                                                        open_close_tags[1]
                                                        )
                self._parsed_json.append(open_tag)
                self._parse_json_list(value)
            HTMLTagsWrapperFactory.__close_tags_stack.append('</li>')

        elif isinstance(obj, list):
            self._parsed_json.append('<ul>')
            for item in obj:
                self._parse_json_list(item)
            HTMLTagsWrapperFactory.__close_tags_stack.append('</ul>')
            self._parsed_json.append(
                HTMLTagsWrapperFactory.__close_tags_stack.pop()
                )

        else:
            self._parsed_json.append(obj)


        try:
            if HTMLTagsWrapperFactory.__close_tags_stack:
                self._parsed_json.append(
                    HTMLTagsWrapperFactory.__close_tags_stack.pop()
                )
        except IndexError as err:
            print(err)
            print(f'{self}.__close_tags_stack is empty list.'
                  'Impossible pop() from empty list')

    def _parse_json_dict(self, obj):
        """
        This function go through all objects in obj with depth recursion and wrap dicts and lists in html-tags
        """
        if isinstance(obj, dict):
            for key, value in obj.items():
                open_tag, HTMLTagsWrapperFactory.__close_tag = (
                                                        self._get_pair_tags(key)
                                                        )
                self._parsed_json.append(open_tag)
                self._parse_json_dict(value)
        elif isinstance(obj, list):
            for item in obj:
                self._parse_json_dict(item)
        else:
            self._parsed_json.append(obj)
            self._parsed_json.append(HTMLTagsWrapperFactory.__close_tag)

    def _parse_json_dict_escape(self, obj):
        """
        This function go through all objects in obj with depth recursion and
        transfer text to html valid classes & id expressions.
        """
        if isinstance(obj, dict):
            for key, value in obj.items():
                open_tag, HTMLTagsWrapperFactory.__close_tag = (
                                                        self._get_pair_tags(key)
                                                        )
                open_tag, closed_tag = self.format_key(open_tag)
                self._parsed_json.append(open_tag)
                self._parse_json_dict_escape(value)
                self._parsed_json.append(closed_tag)
        elif isinstance(obj, list):
            for item in obj:
                self._parse_json_dict_escape(item)
        else:
            self._parsed_json.append(escape(obj))

    def get__parse_json_list(self, obj):
        self._parsed_json = []
        if isinstance(obj, list):
            self._parse_json_list(obj)
        elif isinstance(obj, dict):
            if any([True for key in obj.keys() if 'id' in key or 'class' in key]):
                self._parse_json_dict_escape(obj)
            else:
                self._parse_json_dict(obj)
        else:
            raise Exception(
                'Something went wrong, JSON-data contains invalid data format'
                )

        return self._parsed_json


class Converter:
    """Class that convert json-files to html string."""

    def __init__(self, file_path=None):

        _parent_path = os.path.dirname(os.getcwd())
        self._file_path = file_path or os.path.join(
                                        _parent_path,
                                        'json_to_html/json_files/source.json'
        )

    def get_file_path(self):
        return self._file_path

    def set_file_path(self, file_path):
        self._file_path = file_path

    def _load_json_data(self, file_path):
        with open(file_path) as f:
            json_data = json.load(f)
            return json_data

    def _convert_json_to_html(self, json_data) -> str:
        html_factory = HTMLTagsWrapperFactory()
        html_list = html_factory.get__parse_json_list(json_data)
        html_string = ''.join(html_list)
        return html_string

    def convert(self) -> str:
        """Convert the list with json data to html-string and return it."""

        try:
            data = self._load_json_data(self._file_path)
        except FileNotFoundError as err:
            print(err)
            print(
                "\nMethod can't find json file with current self._file_path"
                f"\n{self}._file_path = {self._file_path}"
                f"\nUse {self}.set_file_path(file_path) to set correct json "
                 "file path")
        else:
            html_string = self._convert_json_to_html(data)

            return html_string


if __name__ == '__main__':
    # use it for check how to working current module
    print('start')
    conv = Converter('../../json_files/source.json')
    print(conv.get_file_path())
    print(conv.convert())

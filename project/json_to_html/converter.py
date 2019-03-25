import json
import os


class Converter:
    """
        Class that convert json-files to html string.
    """

    def __init__(self, file_path=None):
        self._html_tags = {
            'title': ['<h1>', '</h1>'],
            'title': ['<h2>', '</h2>'],
            'title': ['<h3>', '</h3>'],
            'title': ['<h4>', '</h4>'],
            'title': ['<h5>', '</h5>'],
            'title': ['<h6>', '</h6>'],
            'body': ['<p>', '</p>']
        }

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

    def _convert_json_to_html(self, json_data: list) -> str:
        html_list = []
        for d in json_data:
            for key, value in d.items():
                start_tag, end_tag = self._html_tags[key]
                html_list.extend([start_tag, value, end_tag])
        
        html_string = ''.join(html_list)
        return html_string

    def convert(self) -> str:
        """
            Convert the list with json data to html-string and return it.
        """
        try:
            data = self._load_json_data(self._file_path)
        except FileNotFoundError as err:
            print(err)
            print(
                "\nFunction can't find json file with current self._file_path"
                f"{self}._file_path = {self._file_path}"
                f"\nUse {self}.set_file_path(file_path) to set correct json "
                 "file path")
        else:
            html_string = self._convert_json_to_html(data)

            return html_string

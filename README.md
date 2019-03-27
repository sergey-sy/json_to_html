#  json_to_html module

# **This module is converting json-files to html-text.**

It used only standart python libraries for python 3.6+, except pytest module.
But it will be working with earlie python 3 versions also if you change f-strings to string.format().
If you need to run any tests install pytest. Check the documentation in the current [tests modules](project/tests/test_tasks_output.py).
If you no need default test from it project you may delete all folders that names 'tests'.

Be shure that you have all dependencies from requirements.txt.
Usually it all includes in standart python3 libraries.

## **How it's works.**

Put your json-file (filename should be 'source.json') to folder json_files.

Execute commands below in terminal:
```
$ cd you_project_path/json_to_html
$ python3 project/__init__.py
```

Module takes 'source.json' file from folder: json_files, converts it to html-string and printouts the converted data to console.

### Sample json-file in:
```json
[
    {
        "h3": "Title #1",
        "div": "Hello, World 1!"
    },
    {
        "h3": "Title #2",
        "div": "Hello, World 2!"
    }
]
```

### Sample html-string out:
```
<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li><li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>
```


## **How to use class Converter in you code.**
```bash
$ cd json_to_html/project
```
```python
>>> from json_to_html import converter


>>> file_path = '/you_project_path/json_to_html/json_files/source.json'
>>> conv = converter.Converter(file_path)
>>> html_string = conv.convert()
>>> print(html_string)
```
### Out:
```
<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li><li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>
```

*If you need get current filepath use:*
```python
conv.get_file_path()
```

*If you need set current filepath use:* 
```python
conv.set_file_path(file_path)
```


*Please contact with me for any question by e-mail:
[maiyashik@gmail.com](maiyashik@gmail.com)*
...
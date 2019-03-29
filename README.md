#  json_to_html module

# **This module is converting json-files to html-text.**

It used only standart python libraries for python 3.6+, except pytest module.
But it will be working with earlie python 3 versions also if you change f-strings to string.format() method.

If you need to run any tests install pytest. Check the documentation in the current [tests modules](project/tests/test_tasks_output.py).
If you no need default test from it project you may delete all folders that names 'tests'.

Be shure that you have all dependencies from requirements.txt.
Usually it all includes in standart python3 libraries (except pytest).

## **How it's works.**

Put your json-file (filename should be 'source.json') to folder json_files (default folder).
Also you can keep you json files in any place. Read below hot to do it.

Execute commands below in terminal:
```
$ cd you_project_path/json_to_html
$ python3 project/__init__.py
```

Module takes 'source.json' file from folder: json_files, converts it to html-string and printouts the converted data to console.

### Current module version has 3 flow to convert with different ways.
Flow depends from input data format:
1. JSON is array (python list)

2.1 JSON is obj (python dict)

2.2 JSON is obj (python dict, dict keys contain html classes or id)


#### 1. JSON is array (python list)
##### 1.1 Sample json-file in:
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

##### 1.1 Sample html-string out:
```html
'<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li><li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>'
```
##### 1.2 Sample json-file in:
```json
[
    {
        "span": "Title #1",
        "content": [
            {
                "p": "Example 1",
                "header": "header 1"
            }
        ]
    },
    {
        "div": "div 1"
    }
]
```

##### 1.2 Sample html-string out:
```html
'<ul><li><span>Title #1</span><content><ul><li><p>Example 1</p><header>header 1</header></li></ul></content></li><li><div>div 1</div></li></ul>'
```


#### 2.1 JSON is obj (python dict)
##### 2.1 Sample json-file in:
```json
{
    "p": "hello1"
}
```

##### 2.1 Sample html-string out:
```html
'<p>hello1</p>'
```

#### 2.2 JSON is obj (python dict, dict keys contain html classes or id)
##### 2.2 Sample json-file in:
```json
{
    "p.my-class#my-id": "hello",
    "p.my-class1.my-class2": "example<a>asd</a>"
}
```

##### 2.2 Sample html-string out:
```html
<p id="my-id" class="my-class">hello</p><p class="my-class1 my-class2">example&lt;a&gt;asd&lt;/a&gt;</p>
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

*If you need set or change current filepath use:* 
```python
conv.set_file_path(file_path)
```


*Please contact with me for any question by e-mail:
[maiyashik@gmail.com](maiyashik@gmail.com)*
...
"""
For run current test-file install pytest package.
https://docs.pytest.org/en/latest/getting-started.html

Execute the commands bellow to start test-process:
$ cd your_project_path/json_to_html/project
$ python3 -m pytest -v
"""


from json_to_html import converter


def test_task1_output():
    print('Test-task-1')
    conv = converter.Converter()
    conv._file_path = 'tests/test_source/source.json'
    html_string = conv.convert()
    sample_tring = '<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>'
    assert html_string == sample_tring

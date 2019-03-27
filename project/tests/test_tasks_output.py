"""
For run current test-file install pytest package.
https://docs.pytest.org/en/latest/getting-started.html

Execute the commands bellow to start test-process:
$ cd your_project_path/json_to_html/project
$ python3 -m pytest -v
"""


from json_to_html import converter

# no longer necessary
# def test_task1_output():
#     pass


def test_task2_output():
    print('Test-task-2')
    conv = converter.Converter()
    conv._file_path = 'tests/test_source/source_2.json'
    html_string = conv.convert()
    sample_tring = '<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li></ul>'
    assert html_string == sample_tring


def test_task3_output():
    print('Test-task-3')
    conv = converter.Converter()
    conv._file_path = 'tests/test_source/source_3.json'
    html_string = conv.convert()
    sample_tring = '<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li><li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>'
    assert html_string == sample_tring

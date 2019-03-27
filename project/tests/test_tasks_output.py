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
    sample_string = '<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li></ul>'
    assert html_string == sample_string


def test_task3_output():
    print('Test-task-3')
    conv = converter.Converter()
    conv._file_path = 'tests/test_source/source_3.json'
    html_string = conv.convert()
    sample_string = '<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li><li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>'
    assert html_string == sample_string


def test_task4_1_output():
    print('Test-task-4-1')
    conv = converter.Converter()
    conv._file_path = 'tests/test_source/source_4_1.json'
    html_string = conv.convert()
    sample_string = '<ul><li><span>Title #1</span><content><ul><li><p>Example 1</p><header>header 1</header></li></ul></content></li><li><div>div 1</div></li></ul>'
    assert html_string == sample_string


def test_task4_2_output():
    print('Test-task-4-2')
    conv = converter.Converter()
    conv._file_path = 'tests/test_source/source_4_2.json'
    html_string = conv.convert()
    sample_string = '<p>hello1</p>'
    assert html_string == sample_string

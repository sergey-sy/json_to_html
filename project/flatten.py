
import re
from pprint import pprint


with open('../json_files/source.json') as f:
    print(type(f))
    re_strip = re.compile('')
    array = [line.strip().split(':') for line in f.readlines()]

    for each in array:
        if '"' in str(each):
            print(re.findall(r'"(.*?)"', str(each)))
        else:
            print(str(each))

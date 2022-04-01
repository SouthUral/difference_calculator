from general_code.diff_code import diff_files
import json


input_file_1 = json.load(open('tests/fixtures/file1.json'))
input_file_2 = json.load(open('tests/fixtures/file2.json'))


txt = diff_files.generate_diff(input_file_1, input_file_2)


file = open('tests/fixtures/file3_fixture.txt', 'w')
file.write(txt)
file.close()
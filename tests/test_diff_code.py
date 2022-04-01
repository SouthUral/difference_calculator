from general_code.diff_code import diff_files
import json


input_file_1 = json.load(open('tests/fixtures/file1.json'))
input_file_2 = json.load(open('tests/fixtures/file2.json'))


# print(diff_files.generate_diff(input_file_1, input_file_2))
test_new = []
test_str = "{\n  - follow : false\n   host : hexlet.io\n  - proxy : 123.234.53.22  - timeout : 50  + timeout : 20  + verbose : true}"
answer_test = open('tests/fixtures/file3_fixture.txt', 'r')
for i in answer_test:
    test_new.append(i)
answer_test.close()
test_txt_str = ''.join(test_new)
# print(test_txt_str)
# print(test_str)

def test_diff_files():
    assert diff_files.generate_diff(input_file_1, input_file_2) == test_txt_str

# def test_diff_files():
import unittest,json
from simple_flatten_json_py import simple_flatten_json

def read_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
# data=read_file("input/test3.json")
# print(data)
# print(simple_flatten_json.flatten_json(data))

# Create a test case class
class TestFlatClass(unittest.TestCase):

    def test_1(self):
        data=read_file("input/test1.json")
        function_output=simple_flatten_json.flatten_json(data)
        correct_result=read_file("output/result1.json")
        self.assertEqual(function_output,correct_result)
    def test_2(self):
        data=read_file("input/test2.json")
        function_output=simple_flatten_json.flatten_json(data)
        correct_result=read_file("output/result2.json")
        self.assertEqual(function_output,correct_result)
    def test_3(self):
        data=read_file("input/test3.json")
        function_output=simple_flatten_json.flatten_json(data)
        correct_result=read_file("output/result3.json")
        self.assertEqual(function_output,correct_result)


if __name__ == '__main__':
    unittest.main()

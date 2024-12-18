import unittest
import json
import os
try:
    from data_handler import read_json, write_json, get_parameter, set_parameter
except ImportError:
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from data_handler import read_json, write_json, get_parameter, set_parameter
    # No additional code needed here since the import error handling is already in place
class TestDataHandler(unittest.TestCase):

    def setUp(self):
        # Create a sample JSON file for testing
        self.filename = 'test_data.json'
        self.sample_data = {
            "example_key": "example_value",
            "another_key": "another_value"
        }
        with open(self.filename, 'w') as file:
            json.dump(self.sample_data, file, indent=4)

    def tearDown(self):
        # Remove the sample JSON file after testing
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_read_json(self):
        # Test reading JSON data from a file
        data = read_json(self.filename)
        self.assertEqual(data, self.sample_data)

    def test_write_json(self):
        # Test writing JSON data to a file
        new_data = {
            "new_key": "new_value"
        }
        write_json(self.filename, new_data)
        with open(self.filename, 'r') as file:
            data = json.load(file)
        self.assertEqual(data, new_data)

    def test_get_parameter(self):
        # Test getting a parameter from JSON data
        data = read_json(self.filename)
        value = get_parameter(data, "example_key")
        self.assertEqual(value, "example_value")

        # Test getting a non-existent parameter
        value = get_parameter(data, "non_existent_key")
        self.assertIsNone(value)

    def test_set_parameter(self):
        # Test setting a parameter in JSON data
        data = read_json(self.filename)
        set_parameter(data, "new_key", "new_value")
        self.assertEqual(data["new_key"], "new_value")

        # Test updating an existing parameter
        set_parameter(data, "example_key", "updated_value")
        self.assertEqual(data["example_key"], "updated_value")

if __name__ == '__main__':
    unittest.main()
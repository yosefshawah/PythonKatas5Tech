import unittest
from katas.api_response_handler import extract_user_data  

class TestExtractUserData(unittest.TestCase):

    def test_all_fields_present(self):
        sample_json = '''
        {
            "users": [
                {
                    "id": "1",
                    "name": "John",
                    "email": "john@example.com",
                    "company": {"name": "Tech Co"},
                    "address": {"city": "New York"}
                }
            ]
        }
        '''
        result = extract_user_data(sample_json)
        expected = [{
            "id": "1",
            "name": "John",
            "email": "john@example.com",
            "company_name": "Tech Co",
            "city": "New York"
        }]
        self.assertEqual(result, expected)

    def test_missing_fields(self):
        sample_json = '''
        {
            "users": [
                {
                    "id": "42",
                    "name": "Alice",
                    "email": null,
                    "company": null,
                    "address": null
                }
            ]
        }
        '''
        result = extract_user_data(sample_json)
        expected = [{
            "id": "42",
            "name": "Alice",
            "email": "Unknown",
            "company_name": "Unknown",
            "city": "Unknown"
        }]
        self.assertEqual(result, expected)

    def test_partial_nested_fields(self):
        sample_json = '''
        {
            "users": [
                {
                    "id": "99",
                    "name": "Bob",
                    "email": "bob@example.com",
                    "company": {},
                    "address": {"city": null}
                }
            ]
        }
        '''
        result = extract_user_data(sample_json)
        expected = [{
            "id": "99",
            "name": "Bob",
            "email": "bob@example.com",
            "company_name": "Unknown",
            "city": "Unknown"
        }]
        self.assertEqual(result, expected)

    def test_empty_users_list(self):
        sample_json = '''
        {
            "users": []
        }
        '''
        result = extract_user_data(sample_json)
        expected = []
        self.assertEqual(result, expected)

    def test_missing_users_key(self):
        sample_json = '''
        {
            "data": []
        }
        '''
        result = extract_user_data(sample_json)
        expected = []
        self.assertEqual(result, expected)

    def test_malformed_json_raises(self):
        malformed_json = '{ "users": [ { "id": "1", "name": "Foo" '  # Missing closing brackets/quotes
        with self.assertRaises(ValueError):
            extract_user_data(malformed_json)


if __name__ == '__main__':
    unittest.main()

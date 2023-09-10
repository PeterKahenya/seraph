import requests
import unittest


class TestSchema(unittest.TestCase):

    def test_add_schema(self):

        response = requests.post("http://localhost:5000/schema",
                                 json={
                                     "title":"students",
                                     "description":"my awesome students table",
                                     "fields":[
                                          {
                                            "_cls": "SeraphStringField",
                                            "field_description": "Student's first name",
                                            "field_key": "fname",
                                            "field_name": "First Name",
                                            "field_type": "String",
                                            "max_length": 1000,
                                            "min_length": 1
                                        },
                                        {
                                            "_cls": "SeraphIntegerField",
                                            "field_description": "Student's age",
                                            "field_key": "age",
                                            "field_name": "Age",
                                            "field_type": "Integer",
                                            "max_value": 18,
                                            "min_value": 60
                                        }
                                     ]})
        # print(response)
        self.assertEqual(response.status_code,200, "Should be 200")

    def test_get_schemas(self):
        response = requests.get("http://localhost:5000/schema")
        print(response.json())
        self.assertEqual(response.status_code,200, "Should be 200")

if __name__ == '__main__':
    unittest.main()
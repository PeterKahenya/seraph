import requests
import unittest


class TestSchema(unittest.TestCase):

    def test_add_schema(self):
        response = requests.post("http://localhost:5000/schema",json={"title":"students","description":"my awesome students table"})
        print(response)
        self.assertEqual(response.status_code,200, "Should be 200")

    def test_get_schemas(self):
        response = requests.get("http://localhost:5000/schema")
        print(response.json())
        self.assertEqual(response.status_code,200, "Should be 200")

if __name__ == '__main__':
    unittest.main()
import unittest
import requests

class TestApi(unittest.TestCase):
    URL = "http://127.0.0.1:5000/colors"

    NewColor = {
        "color":"white",
        "value":"#fff"
    }

    def test_1_get_all_colors(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        print("Test 1 Completed")

    def test_2_retrieve_single_color_by_id(self):
        resp = requests.get(self.URL + '/1')
        self.assertEqual(resp.status_code, 200)
        print("Test 2 Completed")

    def test_3_retrieve_single_color_by_value(self):
        resp = requests.get(self.URL + '/red')
        self.assertEqual(resp.status_code, 200)
        print("Test 3 Completed")

    def test_4_insert_new_color(self):
        resp = requests.post(self.URL, json=self.NewColor)
        self.assertEqual(resp.status_code, 201)
        print("Test 4 Completed")

    def test_5_remove_color_by_value(self):
        resp = requests.delete(self.URL + '/' + self.NewColor['color'])
        self.assertEqual(resp.status_code, 204)
        print("Test 5 Completed")
        

if __name__ == "__main__":
    tester = TestApi()
    # Execute tests
    tester.test_1_get_all_colors()
    tester.test_2_retrieve_single_color_by_id()
    tester.test_3_retrieve_single_color_by_value()
    tester.test_4_insert_new_color()
    tester.test_5_remove_color_by_value()

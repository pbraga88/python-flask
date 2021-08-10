import unittest
import requests

class TestApi(unittest.TestCase):
    URL = "http://127.0.0.1:5000/colors"

    NewColor = {
        "color":"white",
        "value":"#fff"
    }
    NewColor_Edit = {
        "color":"silver",
        "value":"#c0c0c0"
    }
    WrongColor = {
        "clr":"invalid_color",
        "vl":"#xxx"
    }

    # [GET] Retrieve all
    def test_1_get_all_colors(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        print("Test 1 Completed")
    
    # [GET] Retrieve by id
    def test_2_retrieve_single_color_by_id(self):
        resp = requests.get(self.URL + '/1')
        self.assertEqual(resp.status_code, 200)
        print("Test 2 Completed")
    def test_3_retrieve_single_color_by_null_id(self):
        resp = requests.get(self.URL + '/1000')
        self.assertEqual(resp.status_code, 404)
        print("Test 3 Completed")

    # [GET] Retrieve by value
    def test_4_retrieve_single_color_by_value(self):
        resp = requests.get(self.URL + '/red')
        self.assertEqual(resp.status_code, 200)
        print("Test 4 Completed")
    def test_5_retrieve_single_color_by_null_value(self):
        resp = requests.get(self.URL + '/null_color')
        self.assertEqual(resp.status_code, 404)
        print("Test 5 Completed")

    # [POST] Insert new color
    def test_6_insert_new_color(self):
        resp = requests.post(self.URL, json=self.NewColor)
        self.assertEqual(resp.status_code, 201)
        print("Test 6 Completed")
    def test_7_insert_new_color_null_value(self):
        resp = requests.post(self.URL, json=self.WrongColor)
        self.assertEqual(resp.status_code, 400)
        print("Test 7 Completed")

    # [PUT] Modify color by id
    def test_8_modify_by_id(self):
        resp = requests.put(self.URL + '/8', json=self.NewColor)
        self.assertEqual(resp.status_code, 200)
        print("Test 8 Completed")
    def test_9_modify_by_null_id(self):
        resp = requests.put(self.URL + '/1000', json=self.NewColor)
        self.assertEqual(resp.status_code, 404)
        print("Test 9 Completed")
    def test_10_modify_by_null_value(self):
        resp = requests.put(self.URL + '/8', json=self.WrongColor)
        self.assertEqual(resp.status_code, 400)
        print("Test 10 Completed")

    # [DELETE] Remove Color
    def test_11_remove_color_by_value(self):
        resp = requests.delete(self.URL + '/' + self.NewColor['color'])
        self.assertEqual(resp.status_code, 204)
        print("Test 11 Completed")
    def test_12_remove_color_by_null_value(self):
        resp = requests.delete(self.URL + '/' + self.WrongColor['clr'])
        self.assertEqual(resp.status_code, 404)
        print("Test 12 Completed")

if __name__ == "__main__":
    tester = TestApi()
    #Execute tests
    tester.test_1_get_all_colors()
    tester.test_2_retrieve_single_color_by_id()
    tester.test_3_retrieve_single_color_by_null_id()
    tester.test_4_retrieve_single_color_by_value()
    tester.test_5_retrieve_single_color_by_null_value()
    tester.test_6_insert_new_color()
    tester.test_7_insert_new_color_null_value()
    tester.test_8_modify_by_id()
    tester.test_9_modify_by_null_id()
    tester.test_10_modify_by_null_value()
    tester.test_11_remove_color_by_value()
    tester.test_12_remove_color_by_null_value()
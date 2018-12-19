import unittest
import track_and_trace


class TestCase(unittest.TestCase):
    def test_join_product_code_data(self):
        result = track_and_trace.join_product_code_data('a', 'b', 'c')
        self.assertEqual(result, 'abc')
        print(result)

    def test_batch_lenth(self):
        data = ["", "", "", ""]
        expected = len(data[1])


    def test_join_product_code(self):
        result = track_and_trace.join_product_code('a', 1)
        self.assertEqual(result, 'a/1')
        print(result)

    def test_create_box_code(self):
        result = track_and_trace.create_box_code('a', 'b')
        self.assertEqual(result, 'a/b/box')
        print(result)

    def test_product_code_group(self):

        box_code = 'APAP20181215202012/100,025/box'
        product_code_list = ['APAP20181212202012/100,027', 'APAP20181212202012/100,028', 'APAP20181212202012/100,029']

        expected_result = {'APAP20181215202012/100,025/box': ['APAP20181212202012/100,027', 'APAP20181212202012/100,028', 'APAP20181212202012/100,029']}
        result = track_and_trace.product_code_group(box_code, product_code_list)
        self.assertEqual(result, expected_result)
    


unittest.main()

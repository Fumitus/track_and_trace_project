import unittest
import track_and_trace


class TestCase(unittest.TestCase):
    def test_join_product_code_data(self):
        result = track_and_trace.join_product_code_data('a', 'b', 'c')
        self.assertEqual(result, 'abc')
        print(result)

    def test_read_codes(self):
        box_size = 6
        filename = "data/codes.txt"
        expected_result = ['100102', '100103', '100104', '100105', '100106', '100107']
        result = track_and_trace.read_codes(box_size, filename)
        self.assertEqual(result, expected_result)

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

    def test_product_codes_to_list(self):
        product = 'a'
        codes = ['1', '2', '3', '4', '5', '6']
        
        expected_result = ['a/2', 'a/3', 'a/4', 'a/5', 'a/6'], 'a/1/box'
        result = track_and_trace.product_codes_to_list(product, codes)
        print(expected_result)
        print(result)
        self.assertEqual(result, expected_result)
            


unittest.main()

import unittest
import track_and_trace


class TestCase(unittest.TestCase):
    def test_join_product_code_data(self):
        result = track_and_trace.join_product_code_data('a', 'b', 'c')
        self.assertEqual(result, 'abc')
        print(result)

    def test_open_not_used_codes(self):
        result = track_and_trace.open_not_used_codes("data/test_codes.txt")

        self.assertEqual(result, ['100097','100098','100099'])
        print(result)

    def test_join_product_code(self):
        result = track_and_trace.join_product_code('a', ['1','2','3','4'])
        self.assertEqual(result, 'a/1')
        print(result)

    def test_create_box_code(self):
        result = track_and_trace.create_box_code('a', 'b')
        self.assertEqual(result, 'a/b/box')
        print(result)

    def test_create_pallet_code(self):
        result = track_and_trace.create_pallet_code('a', 'b')
        self.assertEqual(result, 'a/b/pallet')
        print(result)

    def test_stuff(self):

        box_list = ['APAP20181215202012/100,025/box'],
        product_code_list = ['APAP20181212202012/100,027', 'APAP20181212202012/100,028', 'APAP20181212202012/100,029']

        expected_result = {'APAP20181215202012/100,025/box': ['APAP20181212202012/100,027', 'APAP20181212202012/100,028', 'APAP20181212202012/100,029']}
        result = stuff(box_list, product_code_list)
        self.assertEqual(result, expected_result)
    


unittest.main()

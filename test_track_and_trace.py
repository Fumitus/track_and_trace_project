import unittest
import track_and_trace


class TestCase(unittest.TestCase):
    def test_join_product_code_data(self):
        result = track_and_trace.join_product_code_data('a', 'b', 'c')
        self.assertEqual(result, 'abc')
        print(result)

    def test_code_management(self):
        result = track_and_trace.code_management("data/test_codes.txt")
        self.assertEqual(result,'100097')
        print(result)

    # def test_code_management(self):
    #     with open("data/test_codes.txt", "r") as f:
    #         contents = f.readlines()
    #         result = track_and_trace.code_management(contents)
    #         self.assertEqual(result, ['100098\n', '100099\n'])
    #         print(result)

        # with open("data/used_codes.txt", "r") as f:
        #     result = track_and_trace.code_management(f.readlines())
        #     self.assertEqual(result, '100097')
        #     print(result)

    def test_join_product_code(self):
        result = track_and_trace.join_product_code('a', '1')
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

    # def test_stuff(self):

    #     box_list = ['APAP20181215202012/100,025/box'],
    #     product_code_list = ['APAP20181212202012/100,027', 'APAP20181212202012/100,028', 'APAP20181212202012/100,029']

    #     expected_result = {'APAP20181215202012/100,025/box': ['APAP20181212202012/100,027', 'APAP20181212202012/100,028', 'APAP20181212202012/100,029']}
    #     result = stuff(box_list, product_code_list)
    #     self.assertEqual(result, expected_result)
    


unittest.main()

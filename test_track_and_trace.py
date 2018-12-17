import unittest
import track_and_trace


class TestCase(unittest.TestCase):
    def test_join_product_code_data(self):
        result = track_and_trace.join_product_code_data('a', 'b', 'c')
        self.assertEqual(result, 'abc')

def join_product_code(self):
        result = track_and_trace.join_product_code('a', '1234')
        self.assertEqual(result, 'a/1234')

def test_create_box_code(self):
        result = track_and_trace.create_box_code('a', 'b', 'c')
        self.assertEqual(result, 'a/b/box')

def test_create_pallet_code(self):
        result = track_and_trace.create_pallet_code('a', 'b')
        self.assertEqual(result, 'a/b/pallet')

    


unittest.main()

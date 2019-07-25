import unittest
from haskell_repos import r, response_dict


class MyTest(unittest.TestCase):
    def test_status_code(self):
        self.assertEqual(r.status_code, 200)

    def test_total_count_greater(self):
        self.assertGreater((response_dict['total_count']), 80000)


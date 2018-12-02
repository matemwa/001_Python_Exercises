import unittest
from haskell_repos import r, response_dict


class MyTest(unittest.TestCase):
    def test_haskell_repos(self):
        self.assertEqual(r.status_code, 200)
        self.assertGreaterEqual((response_dict['total_count']), 80000)
        self.assertLess((response_dict['total_count']), 100000)
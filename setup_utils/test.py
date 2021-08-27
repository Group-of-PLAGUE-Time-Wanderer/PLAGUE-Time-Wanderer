import unittest
import os


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(os.system("su -c 'python3 test_setup.py;PLAGUE-Time-Wanderer'"), 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()

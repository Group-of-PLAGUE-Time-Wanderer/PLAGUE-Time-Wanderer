import unittest
import os


class TestSetup(unittest.TestCase):
    def test_plague(self):
        self.assertEqual(os.system("su -c 'python3 test_setup.py;PLAGUE-Time-Wanderer'"), 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()

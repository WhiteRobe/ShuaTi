import unittest
import sys
sys.path.append('./')


class TestEnv(unittest.TestCase):
    def test_environment(self):
        assert './' in sys.path


if __name__ == '__main__':
    unittest.main()
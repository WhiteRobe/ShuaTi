import unittest
from newcoder.trick import 替换空格 as tT


class TestFunc(unittest.TestCase):
    def test_replaceSpace(self):
        s = tT.Solution()
        self.assertEqual(s.replaceSpace('We Are Happy'), 'We%20Are%20Happy')


if __name__ == '__main__':
    unittest.main()

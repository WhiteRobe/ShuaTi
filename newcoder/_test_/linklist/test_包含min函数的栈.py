import unittest
from newcoder.linklist import 包含min函数的栈 as tT


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = tT.Solution()
        s.push(3)
        self.assertEqual(3, s.min())
        s.push(4)
        self.assertEqual(3, s.min())
        s.push(2)
        self.assertEqual(2, s.min())
        s.push(3)
        self.assertEqual(2, s.min())
        s.pop()
        self.assertEqual(2, s.min())
        s.pop()
        self.assertEqual(3, s.min())
        s.pop()
        self.assertEqual(3, s.min())
        s.push(0)
        self.assertEqual(0, s.min())
        s.pop()
        self.assertEqual(3, s.min())
        s.pop()
        self.assertEqual(None, s.min())


if __name__ == '__main__':
    unittest.main()

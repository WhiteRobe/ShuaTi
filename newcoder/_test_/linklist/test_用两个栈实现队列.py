import unittest
from newcoder.linklist import 用两个栈实现队列 as tT


class TestCase(unittest.TestCase):
    def test_queue(self):
        q = tT.Solution()
        q.append_tail(1)
        q.append_tail(2)
        assert q.delete_head() == 1
        assert q.delete_head() == 2

    def test_complex_queue(self):
        q = tT.Solution()
        q.append_tail(1)
        assert q.delete_head() == 1
        q.append_tail(2)
        q.append_tail(3)
        assert q.delete_head() == 2
        q.append_tail(1)
        assert q.delete_head() == 3
        assert q.delete_head() == 1

    def test_clean_func(self):
        q = tT.Solution()
        q.push(1)
        assert q.pop() == 1
        q.sa.clean()
        assert q.sa.empty()


if __name__ == '__main__':
    unittest.main()

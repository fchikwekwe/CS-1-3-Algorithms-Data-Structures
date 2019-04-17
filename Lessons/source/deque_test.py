#!python

from deque import Deque
import unittest


class DequeTest(unittest.TestCase):

    # def test_init(self):
    #     d = Deque()
    #     assert d.peek_front() is None
    #     assert d.length() == 0
    #     assert d.is_empty() is True

    def test_init_with_list(self):
        d = Deque(['A', 'B', 'C'])
        # assert d.peek_front() == 'C'
        # assert d.length() == 3
        # assert d.is_empty() is False

    # def test_length(self):
    #     d = Deque()
    #     assert d.length() == 0
    #     d.push('A')
    #     assert d.length() == 1
    #     d.push('B')
    #     assert d.length() == 2
    #     d.pop()
    #     assert d.length() == 1
    #     d.pop()
    #     assert d.length() == 0

    def test_push_front(self):
        d = Deque()
        d.push_front('A')
        d.push_front('B')
        assert d.pop_front() == 'B'

        d.push_front('B')
        d.push_front('C')
        assert d.pop_back() == 'A'
        # assert d.is_empty() is False

    def test_push_back(self):
        d = Deque()


    def test_pop_front(self):
        d = Deque(['A', 'B', 'C'])

    def test_pop_back(self):
        d = Deque(['A', 'B', 'C'])


if __name__ == '__main__':
    unittest.main()

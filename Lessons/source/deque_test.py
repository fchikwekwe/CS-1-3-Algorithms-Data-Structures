#!python

from deque import Deque
import unittest


class DequeTest(unittest.TestCase):

    def test_init(self):
        d = Deque()
        assert d.peek_front() is None
        assert d.length() == 0
        assert d.is_empty() is True

    def test_init_with_list(self):
        d = Deque(['A', 'B', 'C'])
        assert d.peek_front() == 'C'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_length(self):
        d = Deque()
        assert d.length() == 0
        d.push_front('A')
        assert d.length() == 1
        d.push_front('B')
        assert d.length() == 2
        d.pop_front()
        assert d.length() == 1
        d.pop_front()
        assert d.length() == 0

    def test_push_front(self):
        d = Deque()
        d.push_front('A') # (['A'])
        assert d.peek_front() == 'A'
        assert d.peek_back() == 'A'
        assert d.length() == 1
        d.push_front('B') # (['B' => 'A'])
        print(d.list)
        assert d.peek_front() == 'B'
        assert d.peek_back() == 'A'
        assert d.length() == 2

        assert d.pop_front() == 'B' # (['A'])

        d.push_front('B') #  (['B' => 'A'])
        d.push_front('C') #  (['C' => 'B' => 'A'])
        assert d.pop_back() == 'A' # (['C' => 'B'])
        assert d.is_empty() is False

    def test_push_back(self):
        d = Deque()
        assert d.is_empty() is True

        d.push_back(1)
        assert d.is_empty() is False
        assert d.length() == 1
        assert d.peek_back() == 1
        assert d.peek_front() == 1

        d.push_back(2)
        d.push_back(3)
        # print (d.list)
        assert d.length() == 3
        assert d.peek_back() == 3
        assert d.peek_front() == 1

    def test_pop_front(self):
        d = Deque(['A', 'B', 'C'])
        assert d.is_empty() is False
        assert d.length() == 3

        assert d.peek_front() == 'C'
        assert d.peek_back() == 'A'

        assert d.pop_front() == 'C'
        assert d.length() == 2

        assert d.pop_front() == 'B'

        d.push_front('D')
        assert d.pop_front() == 'D'

    def test_pop_back(self):
        d = Deque(['A', 'B', 'C'])
        assert d.length() == 3
        assert d.peek_front() == 'C'
        assert d.peek_back() == 'A'

        assert d.pop_back() == 'A'
        assert d.length() == 2

        assert d.pop_back() == 'B'

        d.push_back('Z')
        assert d.pop_back() == 'Z'


if __name__ == '__main__':
    unittest.main()

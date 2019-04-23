#!python

from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        set = Set()
        assert set.size == 0
        assert len(set) == 0

        elements = [1, 2, 3, 4]
        other_set = Set(elements)
        assert other_set.size == 4
        assert len(other_set) == 4

    def test_hashtable(self):
        pass

    def test_size(self):
        pass

    def test_contains(self):
        pass

    def test_repr(self):
        pass

    def test_add(self):
        pass

    def test_remove(self):
        pass

    def test_union(self):
        pass

    def test_intersection(self):
        pass

    def test_difference(self):
        pass

    def test_is_subset(self):
        pass


    # elements = [1, 2, 3]
    # new_set = Set(elements)
    # if 1 in new_set:
    #     print(True)
    # else:
    #     print(False)
    # new_set.add("something")
    # print(new_set.hashtable)
    # new_set.remove(2)
    # print(new_set.hashtable)

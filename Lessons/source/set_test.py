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

    def test_contains(self):
        s = Set()
        assert s.size == 0
        assert s.__contains__(1) == False
        s.add(1)
        s.add(2)
        assert s.size == 2
        assert s.__contains__(1) == True
        assert s.__contains__(4) == False
        s.remove(1)
        assert s.size == 1
        assert s.__contains__(1) == False
        assert s.__contains__(2) == True

    def test_str(self):
        s = Set([1, 2, 3, 4])
        assert s.size == 4
        assert s.__str__() == "{1, 2, 3, 4}"

        t = Set(["a", "b", "c"])
        assert t.size == 3
        assert t.__str__() == "{'a', 'b', 'c'}"

        t.remove('b')
        assert t.size == 2
        assert t.__str__() == "{'a', 'c'}"

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

#!python

from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init_and_len(self):
        set = Set()
        assert set.size == 0
        assert len(set) == 0

        elements = [1, 2, 3, 4]
        other_set = Set(elements)
        assert other_set.size == 4
        assert len(other_set) == 4

    def test_contains_and_len(self):
        s = Set()
        assert s.size == 0
        assert len(s) == 0
        assert s.__contains__(1) == False
        s.add(1)
        s.add(2)
        assert s.size == 2
        assert len(s) == 2
        assert s.__contains__(1) == True
        assert s.__contains__(4) == False
        s.remove(1)
        assert s.size == 1
        assert len(s) == 1
        assert s.__contains__(1) == False
        assert s.__contains__(2) == True

    # def test_str(self):
    #     s = Set([1, 2, 3, 4])
    #     assert s.size == 4
    #     assert len(s) == 4
    #     assert s.__str__() == "{1, 2, 3, 4}"
    #
    #     t = Set(["a", "b", "c"])
    #     assert t.size == 3
    #     assert t.__str__() == "{'a', 'b', 'c'}"
    #
    #     t.remove('b')
    #     assert t.size == 2
    #     assert len(2) == 2
    #     assert t.__str__() == "{'a', 'c'}"

    def test_add(self):
        s = Set([1])
        assert s.size == 1
        assert len(s) == 1
        assert s.__contains__(1) == True

        s.add(25)
        assert s.__contains__(25) == True
        assert s.__contains__(2) == False
        assert s.__contains__(5) == False
        assert s.__contains__('2') == False
        assert s.size == 2

        s.add('f')
        assert s.__contains__('f') == True
        assert s.size == 3

    def test_remove(self):
        s = Set([1, 2, 3, 'f', 'g', None, 0.5])
        assert s.size == 7
        assert len(s) == 7

        s.remove(1)
        assert s.__contains__(1) == False
        assert s.__contains__(None) == True
        assert s.__contains__(0.5) == True
        assert s.size == 6

        s.remove('g')
        assert s.__contains__('g') == False
        assert s.__contains__(3) == True
        assert s.size == 5
        assert len(s) == 5

        s.remove(None)
        s.remove(0.5)
        assert s.__contains__(None) == False
        assert s.__contains__(0.5) == False
        assert s.__contains__(2) == True

    def test_union(self):
        a = Set([6, 7, 8, 9])
        b = Set([8, 9, 0, 1])

        a_and_b = a.union(b)

        assert a_and_b.__contains__(6) == True
        assert a_and_b.__contains__(7) == True
        assert a_and_b.__contains__(8) == True
        assert a_and_b.__contains__(1) == True

        assert a_and_b.__contains__(11) == False
        assert a_and_b.__contains__(5) == False

    def test_intersection(self):
        a = Set([6, 7, 8, 9])
        b = Set([8, 9, 0, 1])

        both_a_and_b = a.intersection(b)

        assert both_a_and_b.__contains__(6) == False
        assert both_a_and_b.__contains__(8) == True
        assert both_a_and_b.__contains__(9) == True
        assert both_a_and_b.__contains__(1) == False

        a.add('f')
        b.add('f')
        b.add(0.5)

        both_a_and_b = a.intersection(b)

        assert both_a_and_b.__contains__('f') == True
        assert both_a_and_b.__contains__(0.5) == False

        b.remove(8)

        both_a_and_b = a.intersection(b)

        assert both_a_and_b.__contains__(8) == False


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

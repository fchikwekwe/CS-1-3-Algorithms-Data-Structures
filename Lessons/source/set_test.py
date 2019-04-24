#!python

from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init_and_len(self):
        s = Set()
        assert s.size == 0
        assert len(s) == 0

        elements = [1, 2, 3, 4]
        other_set = Set(elements)
        assert other_set.size == 4
        assert len(other_set) == 4

    def test_contains_and_len(self):
        s = Set()
        assert s.size == 0
        assert len(s) == 0
        assert s.__contains__(1) is False
        s.add(1)
        s.add(2)
        assert s.size == 2
        assert len(s) == 2
        assert s.__contains__(1) is True
        assert s.__contains__(4) is False
        s.remove(1)
        assert s.size == 1
        assert len(s) == 1
        assert s.__contains__(1) is False
        assert s.__contains__(2) is True

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
        assert s.__contains__(1) is True

        s.add(25)
        assert s.__contains__(25) is True
        assert s.__contains__(2) is False
        assert s.__contains__(5) is False
        assert s.__contains__('2') is False
        assert s.size == 2

        s.add('f')
        assert s.__contains__('f') is True
        assert s.size == 3

    def test_remove(self):
        s = Set([1, 2, 3, 'f', 'g', None, 0.5])
        assert s.size == 7
        assert len(s) == 7

        s.remove(1)
        assert s.__contains__(1) is False
        assert s.__contains__(None) is True
        assert s.__contains__(0.5) is True
        assert s.size == 6

        s.remove('g')
        assert s.__contains__('g') is False
        assert s.__contains__(3) is True
        assert s.size == 5
        assert len(s) == 5

        s.remove(None)
        s.remove(0.5)
        assert s.__contains__(None) is False
        assert s.__contains__(0.5) is False
        assert s.__contains__(2) is True

    def test_union(self):
        a = Set([6, 7, 8, 9])
        b = Set([8, 9, 0, 1])

        a_and_b = a.union(b)

        assert a_and_b.__contains__(6) is True
        assert a_and_b.__contains__(7) is True
        assert a_and_b.__contains__(8) is True
        assert a_and_b.__contains__(1) is True

        assert a_and_b.__contains__(11) is False
        assert a_and_b.__contains__(5) is False

    def test_intersection(self):
        a = Set([6, 7, 8, 9])
        b = Set([8, 9, 0, 1])

        both_a_and_b = a.intersection(b)

        assert both_a_and_b.__contains__(6) is False
        assert both_a_and_b.__contains__(8) is True
        assert both_a_and_b.__contains__(9) is True
        assert both_a_and_b.__contains__(1) is False

        a.add('f')
        b.add('f')
        b.add(0.5)

        both_a_and_b = a.intersection(b)

        assert both_a_and_b.__contains__('f') is True
        assert both_a_and_b.__contains__(0.5) is False

        b.remove(8)

        both_a_and_b = a.intersection(b)

        assert both_a_and_b.__contains__(8) is False


    def test_difference(self):
        a = Set([6, 7, 8, 9])
        b = Set([8, 9, 0, 1])

        a_or_b = a.difference(b)

        assert a_or_b.__contains__(6) == True
        assert a_or_b.__contains__(7) == True
        assert a_or_b.__contains__(8) == False
        assert a_or_b.__contains__(9) == False

        a.remove(8)

        a_or_b = a.difference(b)

        assert a_or_b.__contains__(8) == True

        a.add(None)
        a.add(3.1)
        print("a", a, "b", b, "both", a_or_b)
        b.add(3.0)
        print(a, b)
        a.add('f')
        b.add('f')

        a_or_b = a.difference(b)

        assert a_or_b.__contains__('f') == False
        assert a_or_b.__contains__(3.0) == True
        assert a_or_b.__contains__(3.1) == True
        assert a_or_b.__contains__(None) == True

    def test_is_subset(self):
        a = Set([1, 2, 3])
        b = Set([1, 2, 4, 5])

        assert a.is_subset(b) == False

        b.add(3)
        assert a.is_subset(b) == True

        a.remove(3)
        assert a.is_subset(b) == True

        a.add(3)
        a.add(4)
        a.add(5)
        assert a.is_subset(b) == True

        a.add('f')
        assert a.is_subset(b) == False

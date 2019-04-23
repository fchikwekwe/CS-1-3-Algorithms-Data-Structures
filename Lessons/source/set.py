
from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.hashtable = HashTable() # start with whatever elements are passed in
        self.size = 0 # property that tracks number of elements in constant time
        if elements is not None:
            for element in elements:
                self.add(element)
                print(self.hashtable)

    def __contains__(self, element):
        """
        Return a boolean indicating whether element is in this set using the
        built in Python "in" keyword
        TODO: Analyze Time and Space Complexity
        """
        return self.hashtable.contains(element) # should return True or False

    def add(self, element):
        """
        add element to this set, if not present already
        TODO: Analyze Time and Space Complexity
        """
        self.hashtable.set(element, None)
        self.size += 1 # increment size property

    def remove(self, element):
        """
        remove element from this set, if present, or else raise KeyError
        TODO: Analyze Time and Space Complexity
        """
        self.hashtable.delete(element)
        self.size -= 1 # decrement size property

    def union(self, other_set):
        """
        return a new set that is the union of this set and other_set
        TODO: Analyze Time and Space Complexity
        """
        pass

    def intersection(self, other_set):
        """
        return a new set that is the intersection of this set and other_set
        TODO: Analyze Time and Space Complexity
        """
        pass

    def difference(self, other_set):
        """
        return a new set that is the difference of this set and other_set
        TODO: Analyze Time and Space Complexity
        """
        pass

    def is_subset(self, other_set):
        """
        return a boolean indicating whether other_set is a subset of this set
        TODO: Analyze Time and Space Complexity
        """
        pass

if __name__ == '__main__':
    elements = [1, 2, 3]
    new_set = Set(elements)
    if 1 in new_set:
        print(True)
    else:
        print(False)
    new_set.add("something")
    print(new_set.hashtable)
    new_set.remove(2)
    print(new_set.hashtable)

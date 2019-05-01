
from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.hashtable = HashTable() # start with whatever elements are passed in
        self.size = 0 # property that tracks number of elements in constant time
        self.index = -1
        if elements is not None:
            for element in elements:
                self.add(element)

    def __len__(self):
        """
        Return the number of elements in set.
        TODO: Analyze Time and Space Complexity
        """
        return self.size

    def __contains__(self, element):
        """
        Return a boolean indicating whether element is in this set using the
        built in Python "in" keyword
        TODO: Analyze Time and Space Complexity
        """
        return self.hashtable.contains(element) # should return True or False

    def __str__(self):
        """Return a formatted string representation of this set."""
        items = ['{!r}'.format(key) for key in self.hashtable.keys()]
        return "{" + ', '.join(items) + "}"

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
        results = Set()
        for element in self.hashtable.keys():
            results.add(element)

        for element in other_set.hashtable.keys():
            results.add(element)

        return results

    def intersection(self, other_set):
        """
        Time complexity: O(n) where n is the length of the smaller set
        Space complexity: O(1) because no new space is created except output. 
        """
        results = Set()

        # figure out which set is shorter
        if self.size > other_set.size: 
            smaller = other_set
            bigger = self
        else: 
            bigger = self
            smaller = other_set

        # iterate only over the smaller set
        for element in smaller.hashtable.keys():
            if element in bigger:
                results.add(element)
        return results

    def difference(self, other_set):
        """
        Time complexity: O(n) where n is the length of self. 
        Space complexity: O(1) because no new space is created except output. 
        """
        results = Set()

        # iterate only over the smaller set
        for element in self.hashtable.keys():
            if element not in other_set.hashtable.keys():
                results.add(element)
        
        return results

    def is_subset(self, other_set):
        """
        Time complexity: O(n) where n is the length of self. 
        Space complexity: O(1) because no new space is created except input
        and output.
        """
        for element in self.hashtable.keys():
            if element not in other_set.hashtable.keys():
                return False
        # all items in self are also in set
        return True

if __name__ == '__main__':
    elements = [1, 2, 3]
    new_set = Set(elements)
    new_set.add(3)
    print(new_set)

    other_elements = [3, 4, 5]
    other_set = Set(other_elements)

    print(new_set.union(other_set))
    print(new_set.intersection(other_set))
    print(new_set.difference(other_set))
    print(new_set.is_subset(other_set))

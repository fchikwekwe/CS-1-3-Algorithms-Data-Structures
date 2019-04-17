from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedDeque(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push_front(self, item):
        """
        Running time: O(1) - Because we always add to the same place in deque
        and only modify one node.
        """
        self.list.prepend(item)

    def push_back(self, item):
        """
        Running time: O(1) - Because we always add to the same place in deque
        and only modify one node.
        """
        self.list.append(item)

    def pop_front(self):
        """
        Running time: O(1) - Because we always remove from the same place in
        deque and only modify one node.
        """
        if self.list.is_empty():
            raise ValueError("There is nothing in the stack.")

        # keep track of the node we're removing
        data = self.list.head.data

        # access the delete property of the LinkedList class
        self.list.delete(data)

        return data

    def pop_back(self):
        """
        Running time: O(1) - Because we always remove from the same place in
        deque and only modify one node.
        """
        if self.list.is_empty():
            raise ValueError("There is nothing in the stack.")

        # keep track of the node we're removing
        data = self.list.tail.data

        # access the delete property of the LinkedList class
        self.list.delete(data)

        return data


class ArrayDeque(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push_front(self, item):
        """
        Running time: O(n) worst case – Because you have to change the index of
        every other item in the list.
        """
        self.list.append(item, 0)

    def push_back(self, item):
        """
        Running time: O(1) - Because we always add to the same place in deque
        and only modify one value.
        """
        self.list.append(item)

    def pop_front(self):
        """
        Running time: O(n) worst case – Because you have to change the index of
        every other item in the list.
        """
        if self.is_empty():
            raise ValueError("That item is not on top of the stack.")
        return self.list.pop(0)

    def pop_back(self):
        """
        Running time: O(1) - Because we always remove from the same place in deque
        and only modify one value.
        """
        if self.is_empty():
            raise ValueError("That item is not on top of the stack.")
        return self.list.pop()

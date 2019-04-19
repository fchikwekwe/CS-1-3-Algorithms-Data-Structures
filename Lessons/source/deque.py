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
                self.push_front(item)

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # will return true if 0 and false otherwise
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # accessing the size property of LinkedList class
        return self.list.length()

    def peek_front(self):
        """
        Time complexity: O(1) because we only have to get data for one node and
        we are not changing any other nodes.
        """
        if self.list.is_empty():
            return None

        # keep track of the node we're removing
        node = self.list.head
        #  And keep track of the data we're returning
        data = node.data

        # Return the head's data value
        return data

    def peek_back(self):
        """
        Time complexity: O(1) because we only have to get data for one node and
        we are not changing any other nodes.
        """
        if self.list.is_empty():
            return None

        # keep track of the node we're removing
        node = self.list.tail
        #  And keep track of the data we're returning
        data = node.data

        # Return the head's data value
        return data

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
                self.push_front(item)

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return len(self.list) <= 0

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def peek_front(self):
        """
        TODO:
        """
        if self.is_empty():
            return None
        return self.list[0]

    def peek_back(self):
        """
        TODO:
        """
        if self.is_empty():
            return None
        return self.list[-1]


    def push_front(self, item):
        """
        Running time: O(n) worst case – Because you have to change the index of
        every other item in the list.
        """
        self.list.insert(0, item)

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

Deque = LinkedDeque
# Deque = ArrayDeque

#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # will return true if 0 and false otherwise
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # accessing the size property of LinkedList class
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) - Because we always add to the same place in stack
        and only modify one node.
        """
        # Pushing onto the top of the stack
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Check if the list is empty
        if self.list.is_empty():
            return None

        # keep track of the node we're removing
        node = self.list.head
        #  And keep track of the data we're returning
        data = node.data

        # Return the head's data value
        print("Peek at data", data)
        return data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) - Because we always remove from the same place in stack
        and only modify one node.
        """
        if self.list.is_empty():
            raise ValueError("There is nothing in the stack.")

        # keep track of the node we're removing
        data = self.list.head.data

        # access the delete property of the LinkedList class
        self.list.delete(data)

        return data


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return len(self.list) <= 0

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) - Because we always add to the same place in deque
        and only modify one value.
        """
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.is_empty():
            return None
        return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) - Because we always remove from the same place in deque
        and only modify one value. """
        if self.is_empty():
            raise ValueError("That item is not on top of the stack.")
        return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack

# if __name__ == '__main__':
#     s = Stack()
#     s.push(1)
#     print(s)

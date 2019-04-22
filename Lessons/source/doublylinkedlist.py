#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case: O(1) because just has to access size. """
        return self.size

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if list is empty or index is first.
        Worst case running time: O(n) if index is later in list or not found. """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        node = self.head
        node_index = 0
        while node is not None and node_index != index:
            # move to next node
            node = node.next
            # keep track of next index value
            node_index += 1
        # check if you got to the end of the list without finding node
        if node is None:
            raise ValueError('Item {} not found in list.'.format(index))

        # otherwise return the found node
        return node.data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if list is empty or index is first.
        Worst case running time: O(n) if index is later in list or not found. """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # check if index is at the end
        if index == self.size:
            self.append(item)
            return

        elif index == 0:
            self.prepend(item)
            return

        node = self.head # start with the head node
        node_index = 0 # counter to keep track of iterations
        index_before_target = index - 1 # node at index before target

        while node is not None and node_index != index_before_target:
            node = node.next
            node_index += 1

        # update size property
        self.size += 1
        # create a new node
        new_node = Node(item)
        print(new_node)
        # change next to point to new node
        new_node.next = node.next
        # add the new node at the right index
        node.next = new_node


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) because the item is always
        inserted at the end of list. """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node # set the head since this is the only node
            new_node.previous = None
            new_node.next = None
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
            new_node.previous = self.tail

        # update size property
        self.size += 1
        # Update tail to new node either way
        self.tail = new_node
        # No other nodes after this one since appending at end
        new_node.next = None

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) because items is always inserted
        at the beginning of the list. """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
            new_node.next = None
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            # make head point to previous
            self.head.previous = new_node
        # update size property
        self.size += 1
        # set the new node as head
        self.head = new_node
        # no other nodes to keep track of
        new_node.previous = None

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: O(1) if list is empty or old_item is first.
        Worst case running time: O(n) if old_item is later in list or not found."""

        node = self.head # start at the head node

        # keep going until you find the node or until end of list
        while node is not None and node.data != old_item:
            node = node.next
        if node is None:
            raise ValueError('Item {} not found in list.'.format(old_item))
        node.data = new_item

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if list is empty or item is first.
        Worst case running time: O(n) if item is later in list or not found."""
        # Start at the head node
        node = self.head
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                node.previous = node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                node.previous.next = node.next
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                self.head.previous = None # might not be necessary
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if node.previous is not None:
                    # Unlink the previous node from the found node
                    node.previous.next = None
                # Update tail to the previous node regardless
                self.tail = node.previous
            # update size property
            self.size -= 1
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    dll = DoublyLinkedList()
    print(dll)

    print('Appending items:')
    dll.append('A')
    print(dll)
    dll.append('B')
    print(dll)
    dll.append('C')
    print(dll)
    dll.insert_at_index(2, "TEST")
    print(dll)
    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('size: {}'.format(dll.size))
    print('length: {}'.format(dll.length()))


    # print('Getting items by index:')
    # for index in range(dll.size):
    #     item = dll.get_at_index(index)
    #     print('get_at_index({}): {!r}'.format(index, item))
    #
    # print('Deleting items:')
    # dll.delete('B')
    # print(dll)
    # dll.delete('C')
    # print(dll)
    # dll.delete('A')
    # print(dll)
    # print('head: {}'.format(dll.head))
    # print('tail: {}'.format(dll.tail))
    # print('size: {}'.format(dll.size))
    # print('length: {}'.format(dll.length()))


if __name__ == '__main__':
    test_linked_list()

 #!python

"""
Implementation of hashtable collision avoidance with linear probing. 
This is still a WIP. I'm aware that its not yet functional. 
"""

class HashTableLinear(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.cells = [[None, None] for _ in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        for cell in self.cells: 
            print("cell", cell)
        cells = ['{!r}: {!r}'.format(cell[0], cell[1]) for cell in self.cells]
        return '{' + ', '.join(cells) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.cells)

    def _cell_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.cells)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        if len(self.cells) == 0:
            raise AssertionError("HashTable is empty.")
        return self.size / len(self.cells)

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Collect all keys in each of the buckets
        all_keys = []
        for cell in self.cells:
            for key, _ in cell.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Collect all values in each of the buckets
        all_values = []
        for cell in self.cells:
            for _, value in cell.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        # index = 0
        for cell in self.cells:
            # index += 1
            # print(key, value, index)
            all_items.append(cell)
            # print(all_items)
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Count number of key-value entries in each of the buckets
        if self.size:
            return self.size

        item_count = 0
        for cell in self.cells:
            item_count += cell.length()
        return item_count
            # Equivalent to this list comprehension:
            # return sum(bucket.length() for bucket in self.buckets)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._cell_index(key)
        cell = self.cells[index]
        # Check if an entry with the given key exists in that bucket
        entry = cell.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._cell_index(key)
        cell = self.cells[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = cell.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]

        # Not found
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value using
        linear probing"""

        # use modulus to wrap around to the 0th index

        # Find the bucket the given key belongs in
        index = self._cell_index(key)
        cell = self.cells[index]
        print("start index", index)
        while cell[0] is not None:  # Looking for empty spot
            if cell[0] == key: # replacing value
                ("found cell")
                cell.delete(cell[0])
                # Insert the new key-value entry into the bucket in either case
                break
            # keep looking for empty spot
            index += 1
            print("searching for empty", index, cell)
        
        # found an empty spot; exited loop
        cell.append([key, value])
        cell.pop(0)
        cell.pop(0)
        
        print("cell", cell)
        self.size += 1 # increment size property
        # Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
            # If so, automatically resize to reduce the load factor
            self._resize()


    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._cell_index(key)
        cell = self.cells[index]

        if cell[0] is not None:  # Found
            # Remove the key-value entry from the bucket
            cell.clear()
            print("cell deleted", cell)
            self.size -= 1 # decrement size property
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None, linear=False):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: ??? under what conditions? [TODO]
        Best and worst case space usage: ??? what uses this memory? [TODO]"""
        print("resizing")
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.cells) * 2  # Double size
        # Option to reduce size if cells are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.cells) / 2  # Half size

        # Get a list to temporarily hold all current key-value entries
        pairs_list = self.items() # get all key-value pairs from hashtable

        # Create a new list of new_size total empty linked list buckets
        self.cells = [LinkedList() for i in range(new_size)] # same as init
        self.size = 0 # reset size

        # Insert each key-value entry into the new list of buckets, which will
        # rehash them into a new bucket index based on the new size
        for key, value in pairs_list:
            # this will reset the overall size
            self.set(key, value)

def test_hash_table():
    ht = HashTableLinear(4)
    print(ht)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.cells)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.cells)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.cells)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()

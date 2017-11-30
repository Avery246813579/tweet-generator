"""
TITLE: hashtable.py
DESCRIPTION:    This is a functioning class instance of a simple Python hash table
                with Linked List implementation. 
SOURCE: Make School Product College: CS2
AUTHOR: Aakash Sudhakar
"""

# ================================================================================
# ============================== IMPORT STATEMENTS ===============================
# ================================================================================


from linkedlist import LinkedList                       # Linked List dependency
from time import time                                   # Time logger library


# ================================================================================
# =============================== CLASS DEFINITION ===============================
# ================================================================================


class HashTable(object):

    # =========================== CLASS INITIALIZER(S) ===========================
    def __init__(self, init_size=8):

        # Creates new list (static array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]


    # ====== METHOD TO RETURN FORMATTED STRING REPRESENTATION OF HASH TABLE ======
    def __str__(self):
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        
        return "{" + ", ".join(items) + "}"


    # =========== METHOD TO RETURN STRING REPRESENTATION OF HASH TABLE ===========
    def __repr__(self):
        return "HashTable({!r})".format(self.items())


    # ================= METHOD TO RETURN INDEX OF TARGET BUCKET ==================
    # TODO: O(?) for time; O(?) for memory
    def _bucket_index(self, key):

        # Calculates given key's hash code and transforms into bucket index
        return hash(key) % len(self.buckets)


    # ======================== METHOD TO RETURN ALL KEYS =========================
    # TODO: O(?) for time; O(?) for memory
    def keys(self):
        all_keys = []

        # Collects all keys per bucket
        for bucket in self.buckets:
            for item_key, item_value in bucket.items():
                all_keys.append(item_key)

        return all_keys


    # ======================= METHOD TO RETURN ALL VALUES ========================
    # TODO: O(?) for time; O(?) for memory
    def values(self):
        all_values = []

        # Collects all values per key per bucket
        for bucket in self.buckets:
            for item_key, item_value in bucket.items():
                all_values.append(item_value)

        return all_values


    # =============== METHOD TO RETURN ALL ITEMS (KEY-VALUE PAIRS) ===============
    # TODO: O(?) for time; O(?) for memory
    def items(self):
        all_items = []

        # Collects all key-value pairs per bucket
        for bucket in self.buckets:
            all_items.extend(bucket.items())

        return all_items


    # ======================= METHOD TO RETURN ITEM LENGTH =======================
    # TODO: O(?) for time; O(?) for memory
    def length(self):

        # NOTE: Default solution using manual bucket iteration
        """
        length_of_items = 0

        # Iterates length counter per item per bucket
        for bucket in self.buckets:
            for item in bucket.items():
                length_of_items += 1

        return length_of_items
        """

        # NOTE: Alternative solution uses defined method
        length_of_items = len(self.items())

        return length_of_items


    # =================== METHOD TO INDICATE EXISTENCE OF ITEM ===================
    # TODO: O(?) for time; O(?) for memory
    def contains(self, key):
        all_keys = self.keys()

        # Checks existence of given key per bucket
        for _ in all_keys:
            if key in all_keys:
                return True
            return False


    # ===================== METHOD TO RETURN VALUE FROM KEY ======================
    # TODO: O(?) for time; O(?) for memory
    def get(self, key):
        items = self.items()

        # Checks key existence per bucket (or returns KeyError), then returns associated value
        if self.contains(key):
            for item_key, item_value in items:
                if item_key == key:
                    return item_value
                # else:
                #     KeyError("Key mismatch: {} does not match {}".format(item_key, key))
        else:
            raise KeyError("Key not found: {}".format(key))


    # ====================== METHOD TO INSERT/UPDATE ITEM ========================
    # TODO: O(?) for time; O(?) for memory
    def set(self, key, value):
        item = self.items()
        bucket_index = self._bucket_index(key)

        # Checks item existence per key per bucket (or inserts item), then replaces item
        if self.contains(key):
            # for item_key, item_value in self.buckets
            for bucket in self.buckets:
                for item_key, item_value in bucket.items():
                    if item_key == key:
                        bucket.replace((item_key, item_value), (key, value))
            pass
        else:
            self.buckets[bucket_index].append((key, value))


    # ========================== METHOD TO DELETE ITEM ===========================
    # TODO: O(?) for time; O(?) for memory
    def delete(self, key):

        # Checks item existence per key per bucket (or raises KeyError), then deletes item
        if self.contains(key):
            # for item_key, item_value in self.buckets
            for bucket in self.buckets:
                for item_key, item_value in bucket.items():
                    if item_key == key:
                        bucket.delete((key, item_value))
                    # else:
                    #     raise KeyError("Key mismatch: {} does not match {}".format(item_key, key))
        else:
            raise KeyError("Key not found: {}".format(key))


# ================================================================================
# ============================== MAIN RUN FUNCTIONS ==============================
# ================================================================================


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\n******************************\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\n******************************\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): the associated value is {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))
    print("hash table: {}".format(ht))

    print('\n******************************\nTesting delete:\n')
    for key in ['I', 'V', 'X']:
        print('delete({!r})'.format(key))
        ht.delete(key)
        print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}\n'.format(ht.length()))


def test_ht_iterable():
    pass

def main():
    t0 = time()
    test_hash_table()
    # test_ht_iterable()
    t1 = time()

    delta = 1000 * (t1 - t0)
    print("\n******************************\nRuntime is {0:.3g} milliseconds.\n".format(delta))
    return


if __name__ == "__main__":
    main()
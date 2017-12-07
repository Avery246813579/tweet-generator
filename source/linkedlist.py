"""
TITLE: linkedlist.py
DESCRIPTION:    This is a functioning model of a simple Python linked list with
                two class instances for the Node and Linked List objects.
SOURCE: CS2-Tweet-Generator course repository at Make School Product College
AUTHOR: Aakash Sudhakar
"""


# ================================================================================
# ============================== IMPORT STATEMENTS ===============================
# ================================================================================


from time import time                                   # Time logger library


# ================================================================================
# ============================ CLASS DEFINITION: NODE ============================
# ================================================================================


class Node(object):

    # =========================== CLASS INITIALIZER(S) ===========================
    def __init__(self, data, p=None, n=None):
        self.data = data
        # self.prev = prev
        self.next = n

    # ============== METHOD TO RETURN STRING REPRESENTATION OF NODE ==============
    def __repr__(self):
        return "Node({!r})".format(self.data)  # Returns string representation of current node


# ================================================================================
# ======================== CLASS DEFINITION: LINKED LIST =========================
# ================================================================================


class LinkedList(object):

    # =========================== CLASS INITIALIZER(S) ===========================
    def __init__(self, h=None, l=None, items=None):
        self.head = h  # First node
        self.tail = l  # Last node
        self.size = 0  # Size of the linked list
        
        # Append given items, if any
        if items:
            for item in items:
                self.append(item)

    # ====== METHOD TO RETURN FORMATTED STRING REPRESENTATION OF HASH TABLE ======
    def __str__(self):
        items = ["({!r})".format(item) for item in self.items()]
        return "[{}]".format(" -> ".join(items))  # Returns formatted string representation of linked list

    # =========== METHOD TO RETURN STRING REPRESENTATION OF LINKED LIST ==========
    def __repr__(self):
        return "LinkedList({!r})".format(self.items())  # Returns string representation of linked list

    # ================ METHOD TO RETURN LIST OF LINKED LIST ITEMS ================
    def items(self):
        items = []  
        node = self.head  

        # Iterates through each node while they exist
        while node:
            items.append(node.data)  
            node = node.next  

        return items  

    
    # ================= METHOD TO RETURN IF LINKED LIST IS EMPTY =================
    def is_empty(self):
        return self.head is None


    # ================== METHOD TO RETURN LENGTH OF LINKED LIST ==================
    """
    NOTE: (TIME) Best/Worst Case -> O(1) -> Returns iterated value in other methods
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def length(self):
        return self.size


    # ========================== METHOD TO APPEND NODE ===========================
    """
    NOTE: (TIME) Best Case -> O(1) -> Create new linked list head
    NOTE: (TIME) Worst Case -> O(n) -> Iterate across every linked list item
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def append(self, item):
        self.size += 1

        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        return


    # ========================== METHOD TO PREPEND NODE ==========================
    """
    NOTE: (TIME) Best Case -> O(1) -> Create new linked list head
    NOTE: (TIME) Worst Case -> O(1) -> Add linked list item directly after head
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def prepend(self, item):
        self.size += 1
        node = Node(item)

        if self.is_empty():
            self.tail = self.head
        else: 
            node.next = self.head
        self.head = node
        return


    # =========================== METHOD TO FIND NODE ============================
    """
    NOTE: (TIME) Best Case -> O(1) -> Returns None
    NOTE: (TIME) Worst Case -> O(n) -> Iterate through all linked list items and return last node's data
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def find(self, quality):  # Quality lambda function helps with searching for tuples based on ID
        if self.is_empty():
            return self.head
        
        node = self.head

        # Iterates through each node while they exist
        while node:
            if quality(node.data):
                return node.data
            node = node.next

        # Returns None if quality doesn't exist in linked list
        return None


    # ========================== METHOD TO DELETE NODE ===========================    
    """
    NOTE: (TIME) Best Case -> O(1) -> Returns ValueError
    NOTE: (TIME) Worst Case -> O(n) -> Iterates through all linked list items and deletes last item
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def delete(self, item):
        if self.is_empty():
            return ValueError("Item not found: {}".format(item))

        node = self.head
        prev_node = None

        # Iterates through each node while they exist
        while node: 
            if node.data == item:
                if self.size == 1:
                    node = None
                    self.head = None
                    self.tail = None
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.head = node
                self.size -= 1
                return True
            else:
                prev_node = node
                node = node.next
        return False

    # ========================= METHOD TO REPLACE NODE ===========================
    """
    NOTE: (TIME) Best Case -> O(1) -> Returns None
    NOTE: (TIME) Worst Case -> O(n) -> Iterates through all linked list items and replaces last item
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def replace(self, quality, replacer):   # Quality lambda function helps with searching for tuples based on ID
        if self.is_empty():
            return self.head

        node = self.head

        # Iterates through each node while they exist
        while node:
            if quality(node.data):
                node.data = replacer
            node = node.next
        return None

    # =================== METHOD TO INSERT NODE AFTER QUALITY ====================
    def insert(self, data):
        pass

    # ============= METHOD TO CONVERT LINKED LIST TO LISTOGRAM (???) =============
    """
    NOTE: (TIME) Best Case -> O(?) -> ???
    NOTE: (TIME) Worst Case -> O(?) -> ???
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def convert_to_listogram(): 
        pass


# ============= METHOD TO CONVERT LINKED LIST TO LISTOGRAM (???) =============
def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\n>> Testing append():')
    for item in ['A', 'B', 'C']:
        print('\nappend({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    
    print("\n>> Testing prepend():")
    for item in ["D", "E", "F"]:
        print("\nprepend({!r})".format(item))
        ll.prepend(item)
        print("list: {}".format(ll))
    

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    print("\n>> Testing find():")
    print("\nF found? \n{} was found".format(ll.find(lambda item: item > "E")))

    """
    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\n>> Testing delete():')
        for item in ["F", "D", "E"]:
            print('\ndelete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))
    """

    print("\n>> Testing replace():")
    print("\nlist before replacement: {}".format(ll))
    print("replacing letters that are not B with X...".format(ll.replace(lambda item: item != "B", "X")))
    print("list after replacement: {}".format(ll))

    print('\n\n[==============================]\n')
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))


# ================================== MAIN RUN =====================================
def main():
    my_list = LinkedList()

    my_list.append("dogs")
    my_list.append("are")
    my_list.append("better")
    my_list.append("than")
    my_list.append("cats")

    print(my_list)

    # my_list_

    for item in my_list:
        print(item)

if __name__ == '__main__':
    test_linked_list()
    # main()

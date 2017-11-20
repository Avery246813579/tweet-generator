#!python



class Node(object):

    def __init__(self, data, p=None, n=None):
        self.data = data
        # self.prev = p
        self.next = n

    def __repr__(self):
        return "Node({!r})".format(self.data)  # Returns string representation of current node



class LinkedList(object):

    def __init__(self, h=None, l=None, items=None):
        self.head = h  # First node
        self.tail = l  # Last node
        self.size = 0  # Size of the linked list
        
        # Append given items, if any
        if items:
            for item in items:
                self.append(item)

    # Method that returns formatted string 
    def __str__(self):
        items = ["({!r})".format(item) for item in self.items()]
        return "[{}]".format(" -> ".join(items))  # Returns formatted string representation of linked list

    def __repr__(self):
        return "LinkedList({!r})".format(self.items())  # Returns string representation of linked list

    # Returns list (dynamic array) of all items in the linked list
    def items(self):
        items = []  
        node = self.head  

        # Iterates through each node while they exist
        while node:
            items.append(node.data)  
            node = node.next  

        return items  

    
    # Returns boolean indicating whether or not linked list is empty
    def is_empty(self):
        return self.head is None


    # Method that returns the length of all nodes in the linked list
    def length(self):
        return self.size
        # Implement both solutions to test for timing/memory


    # Method that inserts the given item at the tail of the linked list
    def append(self, item):
        self.size += 1

        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        return


    # Method that inserts the given item at the head of the linked list
    def prepend(self, item):
        self.size += 1
        node = Node(item)

        if self.is_empty():
            self.tail = self.head
        else: 
            node.next = self.head
        self.head = node
        return


    # Method that returns item from the linked list that satisfies the given quality (lambda)
    def find(self, quality):  # Quality lambda function helps with searching for tuples based on ID
        if self.is_empty():
            return self.head
        
        node = self.head

        # Iterates through each node while they exist
        while node:
            if quality(node.data):
                return node.data
            node = node.next
        return None


    # Method that deletes given item from the linked list, otherwise raises a ValueError
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

    def convert_to_listogram(): 
        pass



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

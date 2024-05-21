class Node:                                                 # Creating Node Class
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyLL:                                             # Creating Linked List Class
    def __init__(self):
        self.head = None

    def print_LL(self):                                     # Forward Traversal
        if self.head is None:
            print("Linked list is empty!!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end = " ")
                n = n.nref    
    
    def print_LL_reverse(self):                             # Backward Traversal
        if self.head is None:
            print("Linked list is empty!!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end = " ")
                n = n.pref


dl1 = doublyLL()
dl1.print_LL()
dl1.print_LL_reverse()


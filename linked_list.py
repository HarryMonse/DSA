class Node:                                                 # Creating Node Class
    def __init__(self, data):
        self.data = data
        self.ref = None

# node1 = Node(10)
# print(node1)

class LinkedList:                                           # Creating Linked List Class
    def __init__(self):
        self.head = None
    
    def print_LL(self):                                     # Traversal
        if self.head is None:
            print("Linked list is empty!!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end = " ")
                n = n.ref
    
    def add_begin(self, data):                              # Adding Node at the beginning
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):                                # Adding Node at the end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):                           # Adding Node in between (After a Node)
        n = self.head
        while n is not None:
            if x == n.data:
                break
            else:
                n = n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):                          # Adding Node in between (Before a Node)
        if self.head is None:
            print("Linked List is empty!!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!!")

    
    def delete_begin(self):                                 # Deleting Node at the beginning
        if self.head is None:
            print("LL is empty. So we can't delete nodes!")
        else:
            self.head = self.head.ref

    def delete_end(self):                                   # Deleting Node at the end
        if self.head is None:
            print("LL is empty. So we can't delete nodes!")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self, x):                           # Deleting Node from middle
        if self.head is None:
            print("LL is empty. So we can't delete nodes!")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present!")
        else:
            n.ref = n.ref.ref


LL1 = LinkedList()
LL1.insert_empty(950)
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_after(200, 100)
LL1.add_end(500)
LL1.add_begin(20)
LL1.add_before(700,20)
LL1.add_before(800,20)
LL1.delete_begin()
LL1.delete_end()
LL1.delete_by_value(950)
LL1.print_LL()


   
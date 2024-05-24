# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# # node1 = Node(10)
# # print(node1)

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def print_LL(self):
#         if self.head is None:
#             print("Linked list is empty!!")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

# LL1 = LinkedList()
# LL1.print_LL()


# class recursion:                                            # Recursion
#     def factorial(self, n):
#         if n <= 1:
#             return 1
#         else:
#             return n * self.factorial(n-1)
        
# ans = recursion()
# print(ans.factorial(5))
    


# def reverse(n):                                             # Reversing string using Recursion
#     if len(n) <= 1:
#         return n
#     else:
#         return n[-1] + reverse(n[:-1])
    
# print(reverse("apple"))


# def reverse(s):                                             # Reversing string using Recursion
#     if len(s) <= 1:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
    
# print(reverse("apple"))




# def linear_search(arr, target):                               # Linear Search
#     for i, num in enumerate(arr):
#         if num == target:
#             return i 
#     return -1
        
# arr = [3,6,2,8,5,7]
# target = 8

# print(linear_search(arr, target))



# arr = [5,2,6,7,3,4]                                           # Linear Search
# target = 7

# flag = 0

# for i in range(len(arr)):
#     if arr[i] == target:
#         print("Found at position", i)
#         flag = 1    

# if flag == 0:
#     print("Not found")



# def linear_search(arr, target):                               # Linear Search
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# arr = [5,2,6,7,3,4]
# target = 7

# ans = linear_search(arr, target)
# print(ans)




# def binary_search(arr, target):                                 # Binary Search
#     low = 0 
#     high = len(arr) -1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         else:
#             if arr[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#     return -1

# arr = [2,3,5,7,8,10]
# target = 5

# ans = binary_search(arr, target)
# print(ans)
    



# def recursive_sum(arr):                                         # Sum of array using Recursion
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + recursive_sum(arr[1:])

# arr = [5,25,10,15,20,25]
# print(recursive_sum(arr))




# def recursive_binary_search(arr, target, low, high):                # Binary Search using Recursion
#     if low > high:
#         return -1
#     else:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             return recursive_binary_search(arr, target, mid + 1, high)
#         else:
#             return recursive_binary_search(arr, target, low, mid - 1)

# arr = [2,4,5,8,25,36,57]
# target = 25

# print(recursive_binary_search(arr, target, 0, len(arr)-1))





# arr = [12,14,67,34,3,6,7]                                             # Array Reversing
# print(arr[::-1])





# Reversing Linked List (Two pointers)

# class Node:                                                 # Creating Node Class
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class LinkedList:                                           # Creating Linked List Class
#     def __init__(self):
#         self.head = None

#     def print_LL(self):                                     # Traversal
#         if self.head is None:
#             print("Linked list is empty!!")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data, "-->", end = " ")
#                 n = n.ref

#     def add_begin(self, data):                              # Adding Node at the beginning
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node

#     # def reverse_LL(self):                                   # Reversing Linked List (Two Pointers)
#     #     prev = None
#     #     current = self.head
#     #     while current:
#     #         next_node = current.ref
#     #         current.ref = prev
#     #         prev = current
#     #         current = next_node
#     #     self.head = prev

#     def reverse_LL_recursive(self, current, prev):           # Reversing Linked List (Recursion)
#         if current is None:
#             self.head = prev
#         else:
#             next_node = current.ref
#             current.ref = prev
#             self.reverse_LL_recursive(next_node, current)

#     def reverse_LL(self):
#         self.reverse_LL_recursive(self.head, None)

# LL1 = LinkedList()
# LL1.add_begin(3)
# LL1.add_begin(2)
# LL1.add_begin(1)

# LL1.print_LL()
# print()
# LL1.reverse_LL()
# LL1.print_LL()



# # Backward Traversal - Doubly Linked List
# class Node:                                                 # Creating Node Class
#     def __init__(self, data):
#         self.data = data
#         self.nref = None
#         self.pref = None

# class doublyLL:                                             # Creating Linked List Class
#     def __init__(self):
#         self.head = None
#     def print_LL(self):                                     # Forward Traversal
#         if self.head is None:
#             print("Linked list is empty!!")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data, "-->", end = " ")
#                 n = n.nref    
#     def add_begin(self, data):                              # Adding Node at the beginning
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.nref = self.head
#             self.head.pref = new_node
#             self.head = new_node

#     def print_backward(self):                               # Backward Traversal
#         if self.head is None:
#             print("Doubly linked list is empty!!")
#         else:
#             current = self.head
#             while current.nref:
#                 current = current.nref
#             while current:
#                 print(current.data, "-->", end=" ")
#                 current = current.pref

# dl1 = doublyLL()
# dl1.add_begin(3)
# dl1.add_begin(2)
# dl1.add_begin(1)
# dl1.print_LL()
# print()
# dl1.print_backward() 




# # Backward Traversal - Singly Linked List
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def print_backward(self):
#         if self.tail is None:
#             print("Singly linked list is empty!!")
#         else:
#             current = self.tail
#             while current:
#                 print(current.data, "-->", end=" ")
#                 current = self.find_previous(current)
#     def find_previous(self, node):
#         current = self.head
#         while current:
#             if current.next == node:
#                 return current
#             current = current.next
#         return None
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
# # Creating a singly linked list
# sllist = SinglyLinkedList()
# sllist.append(1)
# sllist.append(2)
# sllist.append(3)
# print("Original Singly Linked List:")
# current = sllist.head
# while current:
#     print(current.data, "-->", end=" ")
#     current = current.next
# print("\nBackward Traversal of Singly Linked List:")
# sllist.print_backward()





# # Reversing Doubly Linked List
# class DoublyNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#     def append(self, data):
#         new_node = DoublyNode(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#             new_node.prev = current
#     def reverse(self):
#         current = self.head
#         while current:
#             # Swap the prev and next pointers of the current node
#             current.prev, current.next = current.next, current.prev
#             # Move to the next node (which is now the previous node)
#             current = current.prev
#         # Update the head pointer
#         if self.head:
#             self.head = self.head.prev
#     def print_LL(self):
#         current = self.head
#         while current:
#             print(current.data, "-->", end=" ")
#             current = current.next
#         print("None")
# # Creating a doubly linked list
# dllist = DoublyLinkedList()
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# print("Original Doubly Linked List:")
# dllist.print_LL()
# dllist.reverse()
# print("Reversed Doubly Linked List:")
# dllist.print_LL() 


# # SINGLY to DOUBLY Linked List CONVERSION

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def print_LL(self):
#         current = self.head
#         while current:
#             print(current.data, "-->", end=" ")
#             current = current.next
#         print("None")

# class DoublyNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = DoublyNode(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#             new_node.prev = current

#     def convert_from_singly_linked_list(self, singly_linked_list):         # SINGLY to DOUBLY Linked List CONVERSION
#         current_singly = singly_linked_list.head
#         while current_singly:
#             self.append(current_singly.data)
#             current_singly = current_singly.next

#     def print_LL(self):
#         current = self.head
#         while current:
#             print(current.data, "-->", end=" ")
#             current = current.next
#         print("None")

# # Example usage:
# singly_linked_list = SinglyLinkedList()
# singly_linked_list.append(1)
# singly_linked_list.append(2)
# singly_linked_list.append(3)

# doubly_linked_list = DoublyLinkedList()
# doubly_linked_list.convert_from_singly_linked_list(singly_linked_list)

# print("Original Singly Linked List:")
# singly_linked_list.print_LL()

# print("Converted Doubly Linked List:")
# doubly_linked_list.print_LL()




# ------------------------------------------------------------------------------------------------------------------------ 

# Practice


# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i 
#     return -1

# arr = [6,4,2,7,8,4,2,1]
# target = 7

# print(linear_search(arr, target))


# def binary_search(arr, target):
#     low = 0 
#     high = len(arr) -1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
    
#     return -1

# arr = [2,4,6,7,9,24,56,89]
# target = 56

# ans = binary_search(arr, target)
# print(ans)


# def reverse(s):
#     if len(s) <= 1:
#         return s
#     else:
#         return s[-1] + reverse(s[:-1])
    
# s = "harry"
# print(reverse(s))


# def reverse(s):
#     if len(s) <= 1:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
    
# s = "harry"
# print(reverse(s))
        

# def recursive_sum(arr):
#     if len(arr) == 0:
#         return 0 
#     else:
#         return arr[0] + recursive_sum(arr[1:])
    
# arr = [2,5,6]
# print(recursive_sum(arr))


# def recursive_binary_search(arr, target, low, high):
#     if low > high:
#         return -1
#     else:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             return recursive_binary_search(arr, target, mid+1, high)
#         else:
#             return recursive_binary_search(arr, target, low, mid-1)
        
# arr = [2,4,6,7,9,24,56,89]
# target = 7

# print(recursive_binary_search(arr, target, 0, len(arr)-1))


# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# n = 5
# print(factorial(n))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print_LL(self):
#         if self.head is None:
#             print("LL is empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data, "-->", end = " ")
#                 n = n.ref

#     def add_begin(self, data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node

#     def reverse_LL(self):
#         prev = None
#         current = self.head
#         while current:
#             next_node = current.ref
#             current.ref = prev
#             prev = current
#             current = next_node
#         self.head = prev

# LL1 = LinkedList()
# LL1.add_begin(3)
# LL1.add_begin(2)
# LL1.add_begin(1)

# LL1.print_LL()
# print()
# LL1.reverse_LL()
# LL1.print_LL()



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


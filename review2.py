# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid 
#         else:
#             high = mid
#     return -1 

# arr = [2,3,5,7,8,10]
# target = 8
# index = binary_search(arr, target)

# if index != -1:
#     print(f"Target found at index {index}")
# else:
#     print("Target not found")




# def factorial(n):                                                 # Reverse "apple" using recursion
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))



# class Node:                                                       # Reverse a linked list
#     def __init__(self, data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def print_LL(self):
#         if self.head is None:
#             print("Linked list is empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data, "-->", end = " ")
#                 n = n.ref

# LL1 = LinkedList()
# LL1.print_LL()









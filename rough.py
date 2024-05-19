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





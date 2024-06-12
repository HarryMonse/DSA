# stack = []

# def push():
#     if len(stack) == n:
#         print("list is full")
#     else:
#         element = input("Enter the element: ")
#         stack.append(element)
#         print(stack)
    
# def pop_element():
#     if not stack:
#         print("Stack is empty")
#     else:
#         e = stack.pop()
#         print("removed element: ", e)
#         print(stack)

# n = int(input("limit of stack: "))
# while True:
#     print("Select the operation 1.push 2.pop 3.quit")
#     choice = int(input())
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop_element()
#     elif choice == 3:
#         break
#     else:
#         print("Enter the correct operation")



# def InsertionSort(my_list):
#     for index in range(1, len(my_list)):
#         current_element = my_list[index]
#         pos = index
#         while current_element < my_list[pos-1] and pos > 0:
#             my_list[pos] = my_list[pos-1]
#             pos = pos - 1
#         my_list[pos] = current_element

# my_list = [64, 34, 25, 12, 22, 11, 90]
# InsertionSort(my_list)
# print(my_list)


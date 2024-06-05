# stack = []                                          # Implementing stack using list

# stack.append(10)
# stack.append(20)
# stack.append(30)

# print(stack)

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


# print(len(stack) == 0)                              # isEmpty 
# print(not stack)


# stack.append(10)                                    # Peek or Top element
# stack.append(20)
# stack.append(30)
# print(stack[-1])                                    



# stack= []                                           #Program

# def push():
#     if len(stack)==n:
#         print("list is full!")
#     else:
#         element = input("Enter the element: ")
#         stack.append(element)
#         print(stack)

# def pop_element():
#     if not stack:
#         print ("stack is empty!")
#     else:
#         e = stack.pop()
#         print("removed element: ", e)
#         print(stack)

# n = int(input("limit of stack: "))
# while True:
#     print("Select the operation 1.push 2.pop 3.quit")
#     choice = int(input())
#     if choice==1:
#         push()
#     elif choice==2:
#         pop_element()
#     elif choice==3:
#         break 
#     else:
#         print("Enter the correct operation!")




# import collections                                  # Implementing stack using modules
# stack = collections.deque()                         # Using 'deque' class from 'collections' module
# print(stack)                     

# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


# print(len(stack) == 0)                              # isEmpty 
# print(not stack)

# stack.append(10)                                    # Peek or Top element
# stack.append(20)
# stack.append(30)
# print(stack[-1]) 


# import queue                                        # Using 'LifoQueue' class from 'queue' module
# stack = queue.LifoQueue(3)

# stack.put(10)                                             # We use put & get instead of append & pop
# stack.put(20)
# stack.put(30)
# # stack.put(40, timeout=1)


# print(stack.get())
# print(stack.get())
# print(stack.get())
# # print(stack.get(timeout=1))



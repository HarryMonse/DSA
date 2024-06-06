# # Queue

# queue = []                                                  # Implementing Queue using list
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)

# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))


# queue = []                                                  # Implementing Queue using list                                                    
# queue.insert(0, 10)
# queue.insert(0, 20)
# queue.insert(0, 30)
# print(queue)

# print(queue.pop())
# print(queue.pop())
# print(queue.pop())


# queue = []                                                  # isEmpty
# print(not queue)                                            


# queue = []                                                  # Front and Rear element
# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue[-1])
# print(queue[0])



# queue = []                                                  # Program
# def enqueue() :
#     element = input("Enter the element: ")
#     queue.append(element)
#     print(element, "is added to queue!")
# def dequeue() :
#     if not queue:
#         print("queue is empty!")
#     else:
#         e = queue.pop(0)
#         print("removed element: " , e)
# def display() :
#     print(queue)

# while True:
#     print("Select the operation 1.add 2.remove 3.show 4.3quit")
#     choice = int(input())
#     if choice==1:
#         enqueue()
#     elif choice==2:
#         dequeue()
#     elif choice==3:
#         display()
#     elif choice==4:
#         break 
#     else:
#         print("Enter the correct operation!")




# import collections                                              # Implementing queue using classes
# q = collections.deque()                                         # Using 'deque' class from 'collections' module
# print(q)

# q.appendleft(10)                                                    # Using append left and pop methods
# q.appendleft(20)
# q.appendleft(30)
# print(q)

# print(q.pop())
# print(q.pop())
# print(q.pop())


# q.append(10)                                                        # Using append and pop left methods
# q.append(20)
# q.append(30)
# print(q)

# print(q.popleft())
# print(q.popleft())
# print(q.popleft())


# print(not q)                                                    # isEmpty


# q.append(20)                                                    # to find values
# q.append(10)
# q.append(5)
# print(q)

# print(q[-1])
# print(q[0])



# import queue                                        # Using 'Queue' class from 'queue' module
# q = queue.Queue()

# q.put(10)                                             # We use put & get instead of append & pop
# q.put(50)
# q.put(30)

# print(q.get())
# print(q.get())
# print(q.get())



# q = []                                              # Priority Queue
# q.append(10)                                            # Taking Lowest Value as Highest Priority
# q.append(40)
# q.append(20)
# q.sort()
# print(q)

# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))


# import queue                                            # Using priority queue class
# q = queue.PriorityQueue()                                  # (Automatically takes the lowest value as the highest priority)
# q.put(10)                                                   # We use put & get
# q.put(60)
# q.put(20)
# q.put(40)
# q.put(40)

# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())


# q = []                                                  # Giving priority manually using tuple
# q.append((1, "alexa"))
# q.append((4, "alex"))
# q.append((2, "al"))
# q.sort(reverse=True)                                        # Taking Highest Value as Highest Priority
# print(q)

# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))


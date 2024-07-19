# class BST:
#     def __init__(self,key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None

#     def insert(self,data):
#         if self.key is None:
#             self.key = data
#             return 
#         if self.key == data:
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = BST(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = BST(data)




# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def starts_with(self, prefix):
        
#         def dfs(node, prefix, results):
#             if node.end_of_word:
#                 results.append(prefix)
#             for char, child_node in node.children.items():
#                 dfs(child_node, prefix, results)
#                 current = self.root
#                 for char in prefix:
#                     if char not in current.children:
#                         return[]
#                     current = current.children[char]

#                     results = []
#                     dfs(current,prefix,results)
#                     r




# Inserting edge and vertices to Graph


# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def add_vertex(self, v):
#         if v not in self.graph:
#             self.graph[v] = []
#         else:
#             print(v, "is already present")

#     def add_edge(self, u, v):
#         if u not in self.graph:
#             print("Vertx does not exist")
#             return
#         if v not in self.graph:
#             print("Vertex does not exist")
#             return
        
#         self.graph[u].append(v)
#         self.graph[v].append(u)




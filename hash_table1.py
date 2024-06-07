# def get_hash(key) :           
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100

# print(get_hash("march 22"))

class HashTable:                                                        # Hash Table
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self, key) :
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None   
t = HashTable()
t['march 6'] = 130
t['march 1'] = 20
t['dec 17'] = 27
# del t['march 6']
print(t['march 6'])
print(t['march 1'])
print(t['dec 17'])
# print(t.arr)

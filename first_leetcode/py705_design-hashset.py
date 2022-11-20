"""
1、设计hashset.
"""


class MyHashSet:

    def __init__(self):
        self.mod = 1000
        self.bucket = [[] for _ in range(self.mod)]

    def add(self, key: int) -> None:
        k = key % self.mod
        if key not in self.bucket[k]:
            self.bucket[k].append(key)

    def remove(self, key: int) -> None:
        k = key % self.mod
        if key in self.bucket[k]:
            self.bucket[k].remove(key)

    def contains(self, key: int) -> bool:
        k = key % self.mod
        if key in self.bucket[k]:
            return True
        else:
            return False





# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
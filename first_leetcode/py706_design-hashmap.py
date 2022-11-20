"""

"""


class MyHashMap:

    def __init__(self):
        self.mod = 1000
        self.bucket = [[] for _ in range(self.mod)]

    def put(self, key: int, value: int) -> None:
        k = key % self.mod
        for kv in self.bucket[k]:
            if kv[0] == key:
                kv[1] = value
                return
        self.bucket[k].append([key, value])

    def get(self, key: int) -> int:
        k = key % self.mod
        for k_, v_ in self.bucket[k]:
            if k_ == key:
                return v_
        return -1

    def remove(self, key: int) -> None:
        k = key % self.mod
        for idx, kv in enumerate(self.bucket[k]):
            if kv[0] == key:
                self.bucket[k].pop(idx)
                return


# Your MyHashMap object will be instantiated and called as such:

"""
    ["MyHashMap","put","put","get","get","put","get","remove","get"]
    [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
"""
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
param_2 = obj.get(1)
param_2 = obj.get(3)
obj.put(2, 1)
param_2 = obj.get(2)
obj.remove(2)
param_2 = obj.get(2)

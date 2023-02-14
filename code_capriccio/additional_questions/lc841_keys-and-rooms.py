class Solution:
    def dfs(self, rooms, key, visited):
        if visited[key]:
            return
        visited[key] = True
        for k in rooms[key]:
            self.dfs(rooms, k, visited)
        return

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        len_rooms = len(rooms)
        visited = [False for _ in range(len_rooms)]
        self.dfs(rooms, 0, visited)
        for i in visited:
            if not i:
                return False
        return True

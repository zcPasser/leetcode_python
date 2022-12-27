from collections import defaultdict, OrderedDict

class Solution:
    def __init__(self):
        self.ans = []
        self.from_to_tickets = defaultdict()
        self.len_tickets = 0

    def backtracking(self, start_airpot: str) -> bool:
        if len(self.ans) == self.len_tickets + 1:
            return True
        if start_airpot in self.from_to_tickets:
            temp = self.from_to_tickets[start_airpot]
            for end_airpot in temp:
                if temp[end_airpot] > 0:
                    self.ans.append(end_airpot)
                    temp[end_airpot] -= 1
                    if self.backtracking(end_airpot):
                        return True
                    self.ans.pop()
                    temp[end_airpot] += 1
        return False

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        self.ans.clear()
        self.from_to_tickets.clear()
        tickets.sort(key=lambda item: item[1])
        # tickets = sorted(lambda item: item[1])
        for item in tickets:
            if item[0] not in self.from_to_tickets:
                self.from_to_tickets[item[0]] = OrderedDict()
            if item[1] not in self.from_to_tickets[item[0]]:
                self.from_to_tickets[item[0]][item[1]] = 0
            self.from_to_tickets[item[0]][item[1]] += 1
        self.len_tickets = len(tickets)
        start_airpot = 'JFK'
        self.ans.append(start_airpot)
        self.backtracking(start_airpot)

        return self.ans

ss = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
s = Solution()
print(s.findItinerary(ss))
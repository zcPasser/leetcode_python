class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for action in moves:
            if action == 'L':
                x -= 1
            elif action == 'R':
                x += 1
            elif action == 'U':
                y += 1
            else:
                y -= 1
        return x == 0 and y == 0
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    # twenty += 1
                elif five > 2:
                    five -= 3
                    # twenty -= 1
                else:
                    return False
        return True
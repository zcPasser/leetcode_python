class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        R, D = True, True
        # 当flag大于0时，R在D前出现，R可以消灭D。
        flag = 0

        len_sen = len(senate)
        while R and D:
            R, D = False, False
            for i in range(len_sen):
                if senate[i] == 'R':
                    if flag < 0:
                        senate[i] = 0
                    else:
                        R = True
                    flag += 1
                if senate[i] == 'D':
                    if flag > 0:
                        senate[i] = 0
                    else:
                        D = True
                    flag -= 1
        return 'Radiant' if R else 'Dire'

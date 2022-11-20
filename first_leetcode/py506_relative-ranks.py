"""
1、长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。
2、所有得分都 互不相同 。
3、根据得分 决定名次：
    名次第 1 的运动员获金牌 "Gold Medal" 。
    名次第 2 的运动员获银牌 "Silver Medal" 。
    名次第 3 的运动员获铜牌 "Bronze Medal" 。
    从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。

返回：
使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。


"""


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        answer = []
        map_score_ranking = {}
        map_ranking_medal = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}
        sorted_score = sorted(score)
        for i, sc in enumerate(reversed(sorted_score)):
            map_score_ranking[sc] = i
        for sc in score:
            answer.append(map_ranking_medal[map_score_ranking[sc]] if map_score_ranking[sc] in map_ranking_medal
                          else str(map_score_ranking[sc] + 1))

        return answer


score = [5, 4, 3, 2, 1]
s = Solution()
print(s.findRelativeRanks(score=score))

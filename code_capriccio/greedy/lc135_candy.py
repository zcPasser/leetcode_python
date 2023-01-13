class Solution:
    def candy(self, ratings: list[int]) -> int:
        # ans = 0
        len_ratings = len(ratings)
        candys = [1] * len_ratings
        for i in range(1, len_ratings):
            if ratings[i] > ratings[i - 1]:
                candys[i] = candys[i - 1] + 1
        for i in range(len_ratings - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candys[i] = max(candys[i], candys[i + 1] + 1)

        return sum(candys)
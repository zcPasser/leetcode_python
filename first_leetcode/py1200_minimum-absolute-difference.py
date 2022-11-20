

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        min_dist = arr[1] - arr[0]
        buckets = {min_dist: [[arr[0], arr[1]]]}
        for i in range(1, len(arr) - 1):
            dist = arr[i + 1] - arr[i]
            if dist < min_dist:
                min_dist = dist
                # if min_dist not in buckets:
                buckets[min_dist] = [[arr[i], arr[i + 1]]]
                # buckets[min_dist].append()
            elif dist == min_dist:
                buckets[min_dist].append([arr[i], arr[i + 1]])

        return buckets[min_dist]


arr = [3,8,-10,23,19,-4,-14,27]
s = Solution()
print(s.minimumAbsDifference(arr))
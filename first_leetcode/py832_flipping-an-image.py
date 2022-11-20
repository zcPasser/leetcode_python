"""
descript:
    1、Given an n x n binary matrix image。
    2、flip the image horizontally, then invert it.

return:
    the resulting image.

"""


class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n = len(image)
        half_n = (n + 1) // 2
        for i in range(n):
            for j in range(half_n):
                image[i][j], image[i][n - 1 - j] = 1 - image[i][n - 1 - j], 1 - image[i][j]

        return image


image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
so = Solution()
print(so.flipAndInvertImage(image))
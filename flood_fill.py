from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        main_color = image[sr][sc]
        row_size = len(image)
        col_size = len(image[0])
        visited = [[0 for x in range(col_size)] for x in range(row_size)]

        print(row_size, col_size)
        def dfs(self, cr, cc):
            if cr < 0 or cr >= row_size or cc < 0 or cc >= col_size:
                return
            if visited[cr][cc]:
                return
            if image[cr][cc] != main_color:
                return

            image[cr][cc] = color
            visited[cr][cc] = 1

            dfs(self, cr + 1, cc)
            dfs(self, cr - 1, cc)
            dfs(self, cr, cc + 1)
            dfs(self, cr, cc - 1)

        dfs(self, sr, sc)
        return image


image = [[0,0,0],
          [0,0,0]]
sr, sc, color = 0, 0, 0

Solution().floodFill(image, sr, sc, color)
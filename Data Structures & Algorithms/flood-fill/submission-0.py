class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        q = deque()
        q.append([sr, sc])
        visited = set()
        visited.add((sr, sc))
        init = image[sr][sc]
        image[sr][sc] = color

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for rd, cd in directions:
                    r = row + rd
                    c = col + cd
                    if r in range(rows) and c in range(cols) and image[r][c] == init and (r, c) not in visited:
                        image[r][c] = color
                        visited.add((r, c))
                        q.append([r, c])
        return image


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        result = 0
        
        def bfs(row, col):

            queue = deque()
            queue.append((row,col))

            while queue:
                curr = queue.popleft()
                r, c = curr[0], curr[1]
                if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == "0" or (r, c) in visited:
                    continue

                # print(visited, (r, c), grid[row][col])
                
                visited.add((r,c))
                # print(visited, r, c)
                # print(visited)

                dirs = ([1,0], [0, 1], [-1, 0], [0, -1])

                for way in dirs:
                    queue.append((r+way[0], c+way[1]))

            return 1


        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] != "0":
                    result += bfs(row, col)

        return result
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        queue = deque()
        queue.append([sr, sc])
        dirs = [[0, 1], [1,0], [-1, 0], [0, -1]] 
        rows, cols = len(image), len(image[0])
        visited = set()
        starting_color = image[sr][sc]

        while queue:

            currr, currc = queue.popleft()

            image[currr][currc] = color
            visited.add((currr, currc))

            for dirr, dirc in dirs:
                new_r, new_c = dirr+currr, dirc+currc 
                if new_r in range(rows) and new_c in range(cols):
                    if image[new_r][new_c] == starting_color and (new_r, new_c) not in visited:
                        queue.append([new_r, new_c])

        return image

            
            

"""
image=
[[1,1,1],
 [1,1,0],
 [1,0,1]]

[[2,2,2]
,[2,2,0],
 [2,0,1]]


[[2,2,1],
 [2,2,0],
 [1,0,1]]


# Output: [[2,2,2],[2,2,0],[2,0,1]]
[[2,2,2],
 [2,2,0],
 [2,0,1]]
"""
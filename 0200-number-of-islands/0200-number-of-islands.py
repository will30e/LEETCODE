#use bfs to solve this
#first check if the grid is there if not return 0
#create rows and cols
#create a visit set and an island count
#define the bfs function and add the rows and cols
#create a q and add the r and c to the queue and the visit
#while the q is not empty, q.popleft()
#create directions a list of list
#for each direction in dirrection
#if r in range and c in range and the grid location == 1 and r,c not in vist set
#then we append to the queue and the visit
#check the adjacent position of popped r c in the queue



from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if (0 <= new_r < rows and
                        0 <= new_c < cols and
                        grid[new_r][new_c] == "1" and
                        (new_r, new_c) not in visit):
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands

            
        
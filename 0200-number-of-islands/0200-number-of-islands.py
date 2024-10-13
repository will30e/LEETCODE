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

from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()  # To track visited cells.
        islands = 0  # Counter for the number of islands.

        # BFS function to explore the connected land ("1") from (r, c).
        def bfs(r, c):
            q = deque()  # Initialize a queue for BFS.
            visit.add((r, c))  # Mark the starting cell as visited.
            q.append((r, c))  # Add it to the queue.

            # Explore all connected cells.
            while q:
                row, col = q.popleft()  # Correctly call popleft().

                # Define directions for moving up, down, left, and right.
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                # Check all four directions.
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc  # New row and column.
                    # If the new cell is within bounds, is land, and not visited.
                    if (nr in range(rows) and 
                        nc in range(cols) and 
                        grid[nr][nc] == "1" and (nr, nc) not in visit):
                        q.append((nr, nc))  # Add the new cell to the queue.
                        visit.add((nr, nc))  # Mark it as visited.

        # Iterate through the grid to find all islands.
        for r in range(rows):
            for c in range(cols):
                # If the cell is land ("1") and not visited, start a new BFS.
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)  # Perform BFS from this cell.
                    islands += 1  # Increment the island counter.

        return islands  # Return the total number of islands.

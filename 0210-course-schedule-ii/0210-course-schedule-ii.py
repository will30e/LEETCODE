class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list to store the prerequisites for each course
        prereq = { c : [] for c in range(numCourses)}

        # Fill the adjacency list with prerequisites
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
            
        # Output list to store the topological order of courses
        output = []
        # Set to track visited nodes (courses)
        visit = set()
        # Set to track nodes in the current path (to detect cycles)
        cycle = set()
        
        # DFS function to perform topological sort
        def dfs(crs):
            # If the course is already in the cycle set, a cycle is detected
            if crs in cycle:
                return False

            # If the course is already visited, it means it's already processed
            if crs in visit:
                return True
            
            # Mark the course as part of the current cycle
            cycle.add(crs)
            
            # Visit all the prerequisites for this course
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            
            # Remove from cycle set as we have finished exploring this path
            cycle.remove(crs)
            # Mark the course as visited
            visit.add(crs)
            # Append the course to the output list (in reverse order of processing)
            output.append(crs)
            
            return True
        
        # Call DFS for every course
        for c in range(numCourses):
            if not dfs(c):
                return []  # If a cycle is detected, return an empty list
        
        # Return the reversed output list since courses were added in post-order
        return output

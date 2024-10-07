class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        
        def dfs(output,node,path):
            if node == end:
                output.append(path)
                
                
            for nx in graph[node]:
                dfs(output,nx,path+[nx])
                
                         
                
        output = []
        dfs(output,0,[0])
        return output
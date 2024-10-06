class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        s, e = 0, 0
        F = len(firstList)
        S = len(secondList)
        
        
        output = []
        
        
        while (s < F and e < S):
            start = max(firstList[s][0],secondList[e][0])
            end = min(firstList[s][1],secondList[e][1])
            if start <= end:
                output.append([start,end])
            
            
            if firstList[s][1] < secondList[e][1]:
                s += 1
                
            else:
                e += 1
                
            
            
        return output
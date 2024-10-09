class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the intervals
        #create an output with the first interval inside
        #check for every start end interval starting from the second interval
        #get the last end 
        #if the lastend is <= current start then we will change the outputend output[-1][1]  by getting the max 
        #between the lastend and current end
        
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        
        for start,end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])
            
        return output
        
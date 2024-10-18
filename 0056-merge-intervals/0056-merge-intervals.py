        #sort the intervals sort.key = lambda i: i[0]
        #create an output with the first interval inside
        # for every (interval[1:]) start ,end in interval starting from the second interval 
        #get the last end of the output output[-1][1]
        # if the start is less than the lastEnd merge the intervals by adding a new end to the interval which is the max if the         two numbers output[-1][1] = max(lastEnd,end)
        #else append the current start and end to the output
        #return output
        

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        
        output = [intervals[0]]
        
        
        for start,end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
                
        return output
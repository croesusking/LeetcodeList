class Solution:
    def insert(self, ins: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        #LC 57 - Insert Interval
        N = len(ins) # number of intervals
        i = 0 # index of current interval
        res = [] # result list of intervals
        # add non-overlapping intervals before new_interval to res
        while i < N and ins[i][1] < new_interval[0]: # if current interval ends before new_interval starts
            res.append(ins[i])
            i += 1

        # merge overlapping intervals with new_interval
        res.append(new_interval) # add new_interval to res
        while i < N and min(res[-1][1], ins[i][1]) >= max(ins[i][0], res[-1][0]): # if current interval overlaps with new_interval
            res[-1] = min(res[-1][0], ins[i][0]), max(res[-1][1], ins[i][1]) # merge current interval with new_interval`
            i += 1

        # add rest of the non-overlapping intervals to res
        while i < N: # if current interval starts after new_interval ends
            res.append(ins[i])
            i += 1
        
        return res
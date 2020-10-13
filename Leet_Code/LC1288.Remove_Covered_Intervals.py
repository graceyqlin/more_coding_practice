# LC1288.Remove_Covered_Intervals.py
# Topics: Greedy, Sort, Line Sweep
# Given a list of intervals, remove all intervals that are covered by another interval in the list.

# Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

# After doing so, return the number of remaining intervals.

 

# Example 1:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]):
        intervals.sort(key = lambda x: (x[0], -x[1]))
        stack = []
        for interval in intervals:
            if len(stack) == 0:
                stack.append(interval)
            else:
                last = stack[-1]
                if last[1] >= interval[1]:
                    continue
                else:
                    stack.append(interval)
            
        return len(stack)
        

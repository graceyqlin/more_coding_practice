#LC252.Meeting_Rooms.py

# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

# Topics: Sort

# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

def canAttendMeetings(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return True
    
    intervals = sorted(intervals, key = lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
        
    return True

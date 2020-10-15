# LC253.Meeting_Rooms_II.py
# Topics: heap, greedy, sort

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1

def minMeetingRooms(intervals):
        if len(intervals) == 0:
            return 0
        
        import heapq
        
        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        
        stack = []
        
        room_required = 1
        
        for interval in intervals:
            if len(stack) == 0:
                heapq.heappush(stack, interval[1])
                
            else:
                last_end = heapq.heappop(stack)

                if last_end > interval[0]:
                    room_required += 1

                    # be careful!! we only add back the last end when we add a room and have not used the last room end
                    heapq.heappush(stack, last_end)
				
				# be careful!! we always add back current room add
                heapq.heappush(stack, interval[1])
                

                    
        return room_required
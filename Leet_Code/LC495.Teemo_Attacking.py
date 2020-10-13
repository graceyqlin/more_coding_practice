#LC495.Teemo_Attacking
## Topic: Array

# In LOL world, there is a hero called Teemo and his attacking 
# can make his enemy Ashe be in poisoned condition. 
# Now, given the Teemo's attacking ascending time series towards 
# Ashe and the poisoning time duration per Teemo's attacking, 
# you need to output the total time that Ashe is in poisoned condition.

# You may assume that Teemo attacks at the very beginning of a 
# specific time point, and makes Ashe be in poisoned condition immediately.


# Example 1:

# Input: [1,4], 2
# Output: 4
# Explanation: At time point 1, Teemo starts attacking Ashe 
# and makes Ashe be poisoned immediately. 
# This poisoned status will last 2 seconds until the end of time point 2. 
# And at time point 4, Teemo attacks Ashe again, and causes Ashe to be 
# in poisoned status for another 2 seconds. 

# So you finally need to output 4.

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        
        if len(timeSeries) ==1:
            return duration
        
        # make all attacking times
        
        begin_end_times = [[time, time+duration] for time in timeSeries]
        
        # merge intervals
        temp = []
        
        for time in begin_end_times:
            if len(temp) == 0:
                temp.append(time)
            else:
                if temp[-1][1] >= time[0]:
                    temp[-1][1] = max(temp[-1][1], time[1])
                else:
                    temp.append(time)
        return sum([time[1] - time[0] for time in temp])
        
        
#LC495.Teemo_Attacking
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
        
        
#LC346.Moving_Average_from_Data_Stream.py

#Topics: Design, Queue
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example:

# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        import collections
        self.result = collections.deque([])
        self.size = size
        

    def next(self, val: int) -> float:
        if self.size < 1:
            return None
        
        self.result.append(val)
        
        while len(self.result) > self.size:
            self.result.popleft()
        
        return sum(self.result)/len(self.result)
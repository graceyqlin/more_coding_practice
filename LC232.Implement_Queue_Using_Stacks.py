#LC232.Implement_Queue_Using_Stacks.py

# Topics: Stack, Design
# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.


class MyQueue:
    def __init__(self):
        self.instack = []
        self.outstack = []
        
    def move(self):
        if len(self.outstack) == 0:
            while len(self.instack) != 0:
                self.outstack.append(self.instack.pop())
                
        # not the following. because we want to always want to move all elements from instack first when outstack is empty. otherwise it may mess up the orders.
        # while len(self.instack) != 0:
        #     self.outstack.append(self.instack.pop())
                
                
            
    def enqueue(self, x):
        self.instack.append(x)
        
        
        
    def dequeue(self):
        self.move()
        if len(self.outstack) == 0:
            return None
        else:
            return self.outstack.pop()
    
    def peek(self):
        self.move()
        if len(self.outstack) == 0:
            return None
        else:
            return self.outstack[-1]
        
    def isempty(self):
        return len(self.instack) == len(self.outstack) == 0
    
        
    
        
# test1   
# q = MyQueue()
# print(q.enqueue(1))
# print(q.enqueue(2))
# print(q.enqueue(3))
# print(q.dequeue())
# print(q.peek())
# print(q.isempty())


# test2   
# q2 = MyQueue()
# print(q2.dequeue())
# print(q2.peek())
# print(q2.isempty())


# test3
# q3 = MyQueue()
# for i in range(1000000):
#     q3.enqueue(i)
# print(q3.dequeue())
# print(q3.peek())
# print(q3.isempty())


# test4
import random

q4 = MyQueue()
for i in range(1000):
    random_i = random.randint(0, 1000)
    q4.enqueue(random_i)
    
print(q4.outstack[0])    
print(q4.dequeue())

print(q4.instack[0])
print(q4.peek())

print(len(q4.outstack), len(q4.instack))
print(q4.isempty())

import random
## Stack Minimum
# How do you design a stack which - in addition to `push` and `pop`, has a function `min` which returns the lowest element in the set.

#LC155.Min_Stack.py
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
## Stack Minimum
# How do you design a stack which - in addition to `push` and `pop`, has a function `min` which returns the lowest element in the set.

# my solution:
class stack:
	def __init__(self):
		self.internal_list = []
		
	def push(self, x):
		if len(self.internal_list) == 0 or self.internal_list[-1][1] > x:
			self.internal_list.append((x, x))
		else:
			self.internal_list.append((x, self.internal_list[-1][1]))
		
		
	def pop(self):
		if len(self.internal_list) > 0:
			return self.internal_list.pop()[0]
		else:
			return None
		
	def get_min(self):
		if len(self.internal_list) > 0:
			return self.internal_list[-1][1]
		else:
			return None


# s1 = stack()

# print(s1.push(1))
# print(s1.push(2))
# print(s1.pop())
# print(s1.get_min())


# test2:
# s2 = stack()
# print(s2.pop())
# print(s2.get_min())
# print(s2.push(2))
# print(s2.pop())
# print(s2.get_min())

#test3:
# s3 = stack()
# for i in range(100000):
#    randomInt = random.randint(0, 100000)
#    s3.push(randomInt)    
# print(s3.pop())
# print(s3.get_min(), min([a[0] for a in s3.internal_list]))

# test4:
s4 = stack()
s4.push(5)
s4.push(12)
s4.push(6)
s4.push(18)
s4.push(2)
print(s4.get_min())
s4.pop()
s4.push(4)
print(s4.get_min())

# lessons learned:
# 1. multiple pieces of persistent state with the same data is a problem. (persistent means staying alive for a long time)
# 2. avoid many nested ifs (branching logic)
# 3. write down each states of the chaging steps
# 4. have tests so to have confidence the codes can work
# 5. it's important to have functional tests that the code like a client.



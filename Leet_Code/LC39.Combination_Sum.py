
#LC39.Combination_Sum.py


class Solution(object):
	def combinationSum(self, candidates, target):
		ret = []
		self.dfs(candidates, target, [], ret)
		return ret
	
	def dfs(self, nums, target, path, ret):
		if target < 0:
			return 
		if target == 0:
			ret.append(path)
			return 
		for i in range(len(nums)):
			# nums = nums[i:]
			target -= nums[i]
			path += [nums[i]]
			# print('i', i)
			# print('nums', nums)
			# print('target', target)
			# print('path', path)
			# print('ret', ret)
			self.dfs(nums[i:], target, path, ret)


s = Solution()
candidates = [1,2,3]
target = 7
print(s.combinationSum(candidates, target))



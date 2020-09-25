class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        for i in range(len(str_nums), 0, -1):
            for j in range(i-1):
                if str_nums[j] + str_nums[j+1] <= str_nums[j+1] + str_nums[j]:
                    str_nums[j], str_nums[j+1] = str_nums[j+1], str_nums[j]
        return str(int(''.join(str_nums)))
        

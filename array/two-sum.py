class Solution(object):
    def twoSum(self, nums, target): 
        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            for j in range(1+i, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i,j]
        
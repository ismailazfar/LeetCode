class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_streak = 0
        current_streak = 0
        for i in nums:
            if i == 1:
                current_streak += 1
                if current_streak > max_streak:
                    max_streak = current_streak
            else:
                current_streak = 0
        return max_streak

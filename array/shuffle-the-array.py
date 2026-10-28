class Solution(object):
    def shuffle(self, nums, n):
        left = nums[:n]
        right = nums[n:]
        ans = []

        for i in range(n):
            ans.append(left[i])
            ans.append(right[i])

        return ans
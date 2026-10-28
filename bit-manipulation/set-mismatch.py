class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        
        # 1. Calculate the 'Gap' using your sum logic
        # Expected sum of 1 to n
        expected_sum = n * (n + 1) // 2 
        actual_sum = sum(nums)
        
        # 2. Find the duplicate using a Set (The fast way)
        seen = set()
        duplicate = -1
        for num in nums:
            if num in seen:
                duplicate = num
                break # We found it! No need to keep looking.
            seen.add(num)
            
        # 3. Use your logic: missing = duplicate + (expected - actual)
        # Because: expected_sum = (actual_sum - duplicate) + missing
        missing = expected_sum - (actual_sum - duplicate)
        
        return [duplicate, missing]
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        t = nums1 + nums2
        t.sort()
        t1 = len(nums1) + len(nums2)

        if t1 <= 1:
            return t[0]

        if t1%2 != 0:
            return float(t[t1//2])
        else:
            x = t[t1/2] + t[t1/2 - 1]
            return x/2.0

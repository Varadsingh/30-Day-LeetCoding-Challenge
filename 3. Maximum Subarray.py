# Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        A = nums
        mx = A[0]
        su = A[0]
        for i in range(1,len(A)):
            if su + A[i] > A[i]:
                su = su + A[i]
            else:
                su = A[i]
            if mx is None or mx < su:
                mx = su
        return(mx)
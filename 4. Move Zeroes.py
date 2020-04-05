# Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = 1
        zcnt = 0
        firstz = None
        for i in range(0,len(nums)):
            if nums[i] == 0 and prev == 1:
                prev = 0
                zcnt = zcnt + 1
                continue
            elif nums[i] != 0 and prev == 0 and zcnt == 1:
                tmp = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = tmp
                prev = 0
            elif nums[i] == 0 and prev == 0:
                if firstz is None and zcnt == 1:
                    firstz = i - 1
                zcnt = zcnt + 1
            elif nums[i] != 0 and prev == 0 and zcnt > 1:
                tmp = nums[i]
                nums[i] = nums[firstz]
                nums[firstz] = tmp
                firstz = firstz + 1
                prev = 0
            else:
                pass
        return(nums)
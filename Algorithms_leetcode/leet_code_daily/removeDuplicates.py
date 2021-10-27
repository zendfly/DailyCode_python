class Solution:
    def removeDuplicates(self, nums):
        i,j = 0,1
        while j <len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i,j = i+1,j+1

        return len(nums)


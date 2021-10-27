"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例：
    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]


思路：使用双指针，一个指针进行链表遍历，一个用于记录非零部分的下标
"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1

        return nums

if __name__ == '__main__':
    l = [0,1,0,3,12]
    print(Solution().moveZeroes(l))
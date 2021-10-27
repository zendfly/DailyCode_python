class Solution:
    def MaxSubArray(self,nums):
        tmp = nums[0]       #保存当前和
        max_ = tmp          #最大值
        n = len(nums)
        for i in range(1, n):
            if tmp + nums[i] > nums[i]:
                #当前位置加上此时的元素大于tmp时，进行保存
                max_ = max(max_,tmp+nums[i])
                tmp = tmp + nums[i]
            else:
                #tmp（当前和）小于当前位置值时，当前最大序列到此为止。并以该位置为起点继续寻找最大子序列
                max_ = max(max_,tmp,tmp+nums[i],nums[i])
                tmp = nums[i]
        return max_


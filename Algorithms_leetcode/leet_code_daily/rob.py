"""

"""

class Solution:
    def rob(self, nums):
        total = 0
        for i in range(0,len(nums),2):
            total += nums[i]

        return total

if __name__ == '__main__':
    l = [2,7,9,3,1]
    print(Solution().rob(l))
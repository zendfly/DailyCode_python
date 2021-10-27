# """
# 使用字典对结果进行保存
# """
#
# class solution:
#     def twoSum(self,num,target):
#         hashmap = {}
#         for index,i in enumerate(num):
#             anthor_num = target - i
#             if anthor_num in hashmap:
#                 return [hashmap[anthor_num],index]
#             hashmap[i] = index
#         return None
#
#
# #使用字典来模拟hash表，遍历num中没一个元素，将对应的other_num保存到hash表中，
# #判断other_num是否在hash表中
#

class Solution:

    def __init__(self,num,target):
        self.num = num
        self.target = target


    def twosun(self):
        hasmap = {}
        for index,i in enumerate(num):
            target_num = target - i
            if target_num in hasmap:
                return [hasmap[target_num],index]
            else:
                hasmap[i] = index
        return None


if __name__ == '__main__':
    num = [2,7,11,15]
    target = 9
    res = Solution(num,target).twosun()
    print(res)

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次,找出那个只出现了一次的元素。
思路：
    1、对数组进行排序
    2、找出单个的元素

思路：
    1、新建一个数组new_list
    2、遍历元素，如果没有在new_list中出现过，则append到new_list中
    3、如果在new_list中出现过，就删除该元素

"""
class Solution:

    def quick(self,list):

        if len(list) <= 1:
            return list

        pivot = list[0]
        left = Solution().quick([x for x in list[1:] if x <= pivot])
        right = Solution().quick([x for x in list[1:] if x > pivot])

        return left + [pivot] + right

    # def singleNumber(self,list):
    #
    #     new_list = Solution().quick(list)
    #     for i in new_list:

    def new_singleNumber(self,list):

        new_list = []
        for i in list:
            if i not in new_list:
                new_list.append(i)
            else:new_list.remove(i)

        return new_list.pop()

if __name__ == '__main__':
    list = [1]
    res = Solution().new_singleNumber(list)
    print(res)
    print(type(res))


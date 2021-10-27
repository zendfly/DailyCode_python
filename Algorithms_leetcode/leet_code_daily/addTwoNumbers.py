"""
合并两个有序列表(list_a,list_b)
    循环结束条件是 L1和L2都循环到最后一个节点
"""

class Solution():
    """
    合并两个列表（list)
    :return new_list 一个新的列表
    """
    def __init__(self,list_a,list_b):
        #初始化全局参数
        self.list_a = list_a
        self.list_b = list_b

    def add_two_link(self):

        new_list = []
        list_a_length = len(self.list_a)
        list_b_length = len(self.list_b)
        i,j = 0,0
        while i < list_a_length and j < list_b_length:

            if self.list_a[i] < self.list_b[j]:
                new_list.append(self.list_a[i])
                #self.list_a.pop(i)
                i += 1
            else:
                new_list.append(self.list_b[j])
                #self.list_b.pop(j)
                j += 1

        if i <= list_a_length:
            for ii in self.list_a[i:]:
                new_list.append(ii)

        if j <= list_b_length:
            for jj in self.list_b[j:]:
                new_list.append(jj)

        return new_list


if __name__ == '__main__':
    list1 = [1, 5, 7, 7, 19, 75]
    list2 = [5, 7, 9, 64, 186, 879]
    res = Solution(list1,list2).add_two_link()
    print(res)

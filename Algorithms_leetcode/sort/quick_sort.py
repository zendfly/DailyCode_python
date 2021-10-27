"""
快排（qucik sort）
1、选定一个pivot，将大于pivot的元素放在右边（right）,小于pivot的放在左边（left）

O(N^2)
"""

#递归
def quick_sort(list):
    #递归终止条件
    if len(list) <=1:
        return list

    pivot = list[0]
    #递归调用
    left = quick_sort([x for x in list[1:] if x < pivot])
    right = quick_sort([x for x in list[1:] if x > pivot])

    return left + [pivot] + right

#实验
def quick_sort_a(list):

    left = []
    right = []
    pivot = list[0]
    for i in list[1:]:
        if i < pivot:
            left.append(i)
        else:right.append(i)
    return left+[pivot]+right

class Solution():

    def __init__(self,list):
        self.list = list

    def quick_sort(self):
        if len(self.list) == 1:
            return self.list

        pivot = self.list[0]
        left = quick_sort(
            [x for x in self.list[1:] if x < pivot]
        )
        right = quick_sort(
            [x for x in self.list[1:] if x > pivot]
        )

        return left + pivot + right

if __name__ == '__main__':
    list = [6,5,4,3,2,1]
    list1 = [3,5,2,7,8,3,2]
    # result = quick_sort_a(list)
    # print(result)
    pivot = list[0]
    print([x for x in list[1:] if x < pivot])

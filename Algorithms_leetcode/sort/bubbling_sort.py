"""
冒泡排序（bubbling sort）
1、重复对列表进行排序，比较相邻的两个元素；如果顺序错误，就交换位置。
2、每重复一次，未排序的部分中的最大（最小）元素被'冒泡'到最后链表末端
3、重复进行'冒泡'排序，直到列表不再需要交换。

属性：
    稳定排序
    O(1)空间复杂度
    O(n^2)时间复杂度
"""
def bubbkling_sort(list):
    if list is None:
        return None

    list_len = len(list)

    #两个循环，第一个循环是控制循环整个list
    # for i in range(list_len):
    #     for j in range(0,list_len-i-1):
    #         if list[j] > list[j+1]:   #j和j+1进行比较时，j的区间是0到list_len-i-1
    #             list[j],list[j+1] = list[j+1],list[j]

    for i in range(list_len):
        for j in range(1,list_len-i):   #j和j-1进行比较时，j的区间是1到list_len-i
            if list[j-1] > list[j]:
                list[j],list[j-1] = list[j-1],list[j]
    return list


if __name__ == '__main__':
    list = [6,5,4,3,2,1]
    result = bubbkling_sort(list)
    print(result)
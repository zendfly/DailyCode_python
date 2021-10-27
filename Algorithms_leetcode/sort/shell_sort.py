"""
希尔排序（shell_sort）
1、对插入排序的扩展，对大规模的数据进行排序非常有效率
2、将待排序的列表分割成若干个子序列分别进行插入排序
3、使用每个元素间隔（增量）进行分组，相同间隔（增量）的元素为一组进行插入排序
4、随着增量不断减小，每组包含的元素越多，当增量为1时，整个列表被分为1组，算法终止

增量初始值为list长度，每次以1/2的速度递减
"""

def shell_sort(list):
    if list is None:
        return None

    gap = len(list)     #增量，初始增量为len(list)
    length = len(list)
    # print(gap)
    while gap>0:
        for i in range(gap,length):     #分组
            for j in range(i,gap-1,-gap):       #组内排序
                if list[j-gap] > list[j]:
                    list[j-gap],list[j] = list[j],list[j-gap]
            print('list%s'%(list))
        if gap == 2:
            gap =1
        else:gap = gap//2       #增量不断减小，以2倍速度
        print('-------------------------------')
    return list

#练习
def shell_sort_b(list):

    len_list = len(list)

    grap = len_list
    while grap > 0:
        for i in range(grap,len_list):
            for j in range(i,grap-1,-grap):
                if list[j-grap] > list[j]:
                    list[j-grap],list[j] = list[j],list[j-grap]

        if grap == 2:
            grap =1
        else:grap = grap//2

    return list


def shellSort(arr):
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        #从后往前找
        for i in range(gap,len(arr)):
            temp = arr[i]       #当前需要插入的元素
            j = i-gap       #temp元素前gap步长的元素
            while j >= 0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

if __name__ == '__main__':
    list = [6,5,4,3,2,1]
    result = shellSort(list)
    print(result)
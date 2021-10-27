"""
归并排序（merge sort）
1、对待排序列表进行划分
2、对划分后的列表进行排序
3、合并排序后的列表

属性：
    稳定
    O(n)空间复杂度
    O(nlgn)时间复杂度
"""

#合并两个有序列表
def merge(list1,list2):
    if list1 is None or list2 is None:
        return None

    new_list = []
    i,j = 0,0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

    while i < len(list1):
        new_list.append(list1[i])
        i += 1
    while j < len(list2):
        new_list.append(list2[j])
        j += 1
    return new_list

#合并列表（merge list）
def merge_a(list1,list2):
    if list1 is None or list2 is None:
        return None

    new_list_a = []
    i,j = 0,0
    while len(list1) > 0 and len(list2):
        if list1[i] > list2[j]:
            new_list_a.append(list2[j])
            list2.remove(list2[j])
            j += 1
        else:
            new_list_a.append(list1[i])
            list1.remove(list1[i])
            i += 1

    new_list_a += list1
    new_list_a += list2

    return new_list_a

#归并排序
def merge_sort(list):
    if len(list) <= 1:
        return list

    #递归
    m = len(list)//2
    a = merge_sort(list[:m])
    b = merge_sort(list[m:])

    return merge(a,b)


if __name__ == '__main__':
    list = [6,5,4,3,2,1]
    result = merge_sort(list)
    print(result)
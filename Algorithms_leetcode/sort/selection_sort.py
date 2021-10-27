"""
选择排序（selection_sort）
1、重复遍历列表
2、记录最小（最大）元素的下标
3、当遍历完后，把记录的元素与未排序列表末端进行交换

属性：
    不稳定
    O(1)空间复杂度
    O(n^2)时间复杂度
"""

def selection_sort(list):
    if list is None:
        return None

    #预设最小值下标'i'
    for i in range(len(list)):
        min_index = i
        #寻找最小值下标
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i],list[min_index] = list[min_index],list[i]
    return list


class Sulution():

    def __init__(self,list):
        self.list = list


    def selection_sort(self):
        for i in range(len(self.list)):
            min_indxe = i

            for j in range(i,len(self.list)):
                if self.list[j] < self.list[min_indxe]:
                    min_indxe = j
            self.list[i],self.list[min_indxe] = self.list[min_indxe],self.list[i]
        return self.list



if __name__ == '__main__':
    list = [6,5,4,3,2,1]
    result = selection_sort(list)
    res = Sulution(list).selection_sort()
    print(res)
    print(result)
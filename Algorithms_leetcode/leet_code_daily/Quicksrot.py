#快排，选取一个pivot（基准）进行比较
#1、大于pivot的放入右边，
#2、小于的放入左边
# 1和2 操作一个就行
# 在进行交换时，以小于pivot交换到左边为例，当遇见小于pivot的元素时从下标为0的元素进行交换

#使用
def partition(arr,low,high):
    i = (low-1)     #i用来计数，交换的位置
    pivot = arr[high]       #pivot取数组最后一位
    for j in range(low,high):
        if arr[j]<= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]     #将pivot放入i+1的位置
    return i+1

#递归调用交换函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print(arr)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    # partition(arr,0,5)
    quickSort(arr, 0, n - 1)
    # print("排序后的数组:")
    # for i in range(n):
    #     print("%d" % arr[i])
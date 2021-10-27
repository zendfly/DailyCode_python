#在有重复有序的数组中查找一个区间
#使用二分查找，运行两次，分别查找最左和最右两个目标

def binary_search_exit_2(arr,item):
    if len(arr) == 0:
        return -1
    #查找最左边的数
    left,right = 0,len(arr)-1
    while left +1 <right:
        mid = left + (right-left)+1
        if arr[mid] == item:
            right = mid

        if arr[mid] > item:
            left = mid
        elif arr[mid] < item:
            right = mid
    if arr[left] == item:
        lboundl = left
    elif arr[right] == item:
        lboundl = right
    else:return (-1,-1)

    #查找最右边的数
    left1,right1 = 0,len(arr)-1
    while left1 + 1 < right1:
        mid = left1 + (right1 - left1) + 1
        if arr[mid] == item:
            left1 = mid

        if arr[mid] > item:
            left1 = mid
        elif arr[mid] < item:
            right1 = mid
    if arr[left1] == item:
        rboundl = left
    elif arr[right1] == item:
        rboundl = right1
    else:
        return (-1,-1)
    return (lboundl,rboundl)




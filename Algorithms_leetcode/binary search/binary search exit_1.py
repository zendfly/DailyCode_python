# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array
# 在已排序的数组中，查找一个targe，如果不存在则返回应插入的位置


def search_insert_position(arr,targe):
    if len(arr) == 0:
        return -1

    left,right = 0,len(arr)-1
    while left+1 < right:
        mid = left+(right-left)//2
        if arr[mid] == targe:
            return mid

        if arr[mid] < targe:
            right = mid
        elif arr[mid] > targe:
            left = mid

    if arr[left] >= targe:
        return left
    if arr[right] <= targe:
        return right

    return right+1
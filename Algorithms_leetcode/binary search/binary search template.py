"""
二分搜索
    1、查找的List是已排好序

属性
    O(n)时间复杂度

"""

def binary_search_template(alist,item):
    #边界条件判断
    if len(alist) == 0:
        return -1

    left,right = 0,len(alist)-1
    while left + 1 < right:#while停止条件：当left、right 相交或者错位时
        mid = left + (right-left)//2
        if alist[mid] == item:#当alist中有重复的数字时，取最左边的数字
            #当alist[mid]==item时，更新right值时，也更新了mid的值，使mid不断向左边靠拢，直到alist[mid]不等item为止
            #虽然alist[mid]不等item，但alist[right]==item
            #故，取得时重复序列中最左边的一个
            right = mid
        elif alist[mid] < item:
            left = mid
        elif alist[mid] > item:
            right = mid

    if alist[left] == item:
        return left
    elif alist[right] == item:
        return right

    return -1

if __name__ == '__main__':
    arr = [1,2,2,2,3,4,5,6,7]
    print(binary_search_template(arr,2))
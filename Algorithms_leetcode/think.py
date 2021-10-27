
def shell_sort(list):
    if list is None:
        return None

    gap = 5
    length = len(list)

    while gap > 0:
        for i in range(gap,length):
            temp = list[i]
            j = i - gap
            while j >= 0 and list[j] > temp:
                list[j+gap] = list[j]
                j -= gap
            list[j+gap] = temp
        gap = gap//3

    return list

def innsertion_sort(list):
    if list is None:
        return None

    for i in range(1,len(list)):
        temp = list[i]
        j = i-1
        while j >= 0 and  list[j] > temp:
            list[j+1] = list[j]
            j -= 1

        list[j+1] = temp

    return list

if __name__ == '__main__':
    list = [6, 5, 4, 3, 2, 1]
    result = shell_sort(list)
    result_innertion = innsertion_sort(list)
    print(result)
    print(result_innertion)
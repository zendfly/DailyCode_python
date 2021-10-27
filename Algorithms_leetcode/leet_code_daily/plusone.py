"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
涉及进位
"""
#倒序遍历数组，判断每个元素是否需要进位
def plusone(digits):
    i = -1
    digits[i] = digits[i]+1     #最低位加1

    while digits[i] == 10:      #如果digits[-1] == 10，进位
        # 对i是否是高位进行判断
        if i != -len(digits):       #如果不是，进位
            digits[i] = 0       #i为0，i-1的位置加1
            digits[i-1] = digits[i-1]+1
            i -=1   #i位置向前移动一位
        #如果是高位
        else:
            #当最高位需要进位时，其它为都应该为0
            if digits[i] == 10:     #最高位是否需要进位
                digits[0] = 1       #最高位为1
                digits.append(0)    #在数组末尾添加0
    return digits


def plusone_a(digtis):
    digtis = digtis[::-1]       #反转数组
    index = 0
    n = len(digtis)
    c = 1
    while c == 1 and index < n:     #C=1时，说明index需要进位，c表示digits[index]的进位
        t = (digtis[index] + c) % 10        #求余
        c = (digtis[index] + c) // 10       #取整，判断是否需要进位
        digtis[index] = t       #更新元素，
        index += 1
    if c == 1:     #这里C等于1时，说明每个最高位需要进位
        digtis.append(1)
    return digtis[::-1]

if __name__ == '__main__':
    n = [9,9]
    print(plusone(n))


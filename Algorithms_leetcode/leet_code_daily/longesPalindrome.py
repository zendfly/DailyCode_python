"""
最长回文数，一个list -> s,
    顺读和逆读，都是一样
F1:暴力法，O(N^3)
1、枚举所有子串
    枚举子串时，可以自枚举大于已确定最大子串长度
2、判断子串回文
"""
class Solutions:
    def longesPalinderome(self,s):

        size = len(s)
        if size <= 1:
            return s

        max_len = 1     #当前最大子串长度
        res = s[0]      #保存最大子串

        for i in range(size-1):
            for j in range(i+1,size):
                if j - i + 1 > max_len and self.__Palinde(s,j,i):   #当子串大于已确定的最大子串 和 是回文时，
                    max_len = j - i + 1
                    res = s[i,j+1]

        return res

    # 回文判断
    def __Palinde(self,s,j,i):

        while i < j:

            if s[i] != s[j]:
                return False

            j -= 1
            i += 1
        return True
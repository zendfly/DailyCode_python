"""
无重复最长子串
找出给定字符串中的不含有重复字符的最长子串的长度
返回长度以及最长子串

1、新建一个集合lookup，用于占时存放不重复的串
2、用left来标记添加到lookup中的第一个元素，在s的位置。
3、遍历s，如果s[i]在lookup中，则移除lookup中所有的元素，否者添加到lookup
"""
class Solution:
    def lengthOflongestSubstring(self,s):
        if not s:return 0
        left = 0    #标记lookup中的第一个元素在s的位置，用于移除lookup中的元素
        lookup = set()      #使用集合来存放子串
        n = len(s)
        max_len = 0     #初始最长子串的长度
        cur_len = 0     #当前最长子串的长度
        for i in range(n):
            cur_len += 1
            #判断s[i]是否在lookup中，如果存在则把重复元素前的所有元素移除（包括重复的元素）
            while s[i] in lookup:
                lookup.remove(s[left])
                #left表示滑窗的左边界，当出现重复元素时，移动左边界
                left +=1    #用来表示要移除元素的下标，因为依次添加，故需要依次移除
                cur_len -=1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len

#查找两个链表的交集
#两个不同长度的链表，有一段相同的链表，相同部分结束与两个链表的尾部
from Linked_list.Link_list import  LinkedList
from Linked_list.Link_list import Node


def get_Interscetion_TLL(L1,L2):
    #计算两个链表长度差K，让长链表先移动K步，然后两个链表同步移动
    if not L1 or not L2:
        return 0
    len_L1,len_L2 = 0,0
    curL1,curL2 = L1,L2
    while curL1 is not None:
        len_L1 +=1
        curL1 = curL1.next

    while curL2 is not None:
        len_L2 +=1
        curL2 = curL1.next

    curL1, curL2 = L1, L2
    if len_L2>len_L1:
        for i in range(len_L2-len_L1):
            curL2= curL2.next
    elif len_L2<len_L1:
        for i in range(len_L1-len_L2):
            curL1 = curL1.next
    while curL1.value != curL1.value:
        curL1 = curL1.next
        curL2 = curL2.next
    return curL1


#不计算链表长度
def get_Interscetion_TLL_A(L1,L2):
    if L1 and L2:
        L_1,L_2 = L1,L2
        while L_1 != L_2:
            #当两个链表移动到链尾时，接着另一个链表进行移动
            L_1 = L_1.next if L_1 else L_2
            L_2 = L_2.next if L_2 else L_1
    return L_1

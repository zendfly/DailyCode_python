#合并两个以排好序的链表
from Linked_list.Link_list import LinkedList
from Linked_list.Link_list import Node

def mergeTwolist(L1,L2):
    dummy = cur = Node(0)       #创建一个新的List
    while L1 and L2:
        if L1.value < L2.value:
            cur.next = L1.value
            L1 = L1.next
        else:
            cur.next = L2.value
            L2 = L2.next

        cur = cur.next
    cur.next = L1 or L2
    return dummy.next

#不适用额外的空间
def mergeTwolist_A(L1,L2):

    while L1 and L2:
        if L1.value < L2.value:
            L1 = L1.next
        else:
            L2.value.next = L1
            L1.next = L2.value
            L2 = L2.next

    L1.next = L2

    return L1


#recursively(递归)
def mergeTwolist_recursively(L1,L2):

    if not L1 or not L2:
        return L1 or L2
    if L1.value < L2.value:
        L1.next = mergeTwolist_recursively(L1.next,L2)
        return L1
    else:
        L2.next = mergeTwolist_recursively(L1,L2.next)
        return L2



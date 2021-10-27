"""
链表反转
    1、额外定义个节点pre，当前链表指针cur
    2、tep保存当前节点的下一个节点，即cur.next
    3、将cur.next指向pre
    4、将pre 和cur 向前移动，pre = cur,cur = tep
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):

        # 定义两个节点
        pre = None
        cur = head
        while cur:
            # tep 保存cur节点的next
            tep = cur.next
            # 将cur.next 指向pre
            cur.next = pre

            # 将pre 和 cur 向前移动
            pre = cur
            cur = tep
        return pre




        head = head.next

        return


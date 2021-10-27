#寻找单向有环链表中的环开始处

from Linked_list.Link_list import LinkedList
def find_begin(head):

    if head is None:
        return None

    slow = head
    fast = head

    while fast is not None and slow is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:        #第一次相遇
            fast = head
            break

    if fast is None or fast.next is None:
        return None

    while fast != slow:         #单步向前，相遇时退出
        fast = fast.next
        slow = slow.next

    return slow
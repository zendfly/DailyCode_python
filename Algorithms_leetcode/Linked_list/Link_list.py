"""
实现一个链表
包含 Node、LinkerList两类
Node用于创建节点
LinkedList用于前后关联，主要功能包括：
    添加（add)
        add_first
        add_last
    删除（remove）
        remove_first
        remove_last
        remove_at
"""

class Node:#创建一个Node类
    #使用__init__方式，添加Node类必要的参数
    def __init__(self,value = None, next = None):#value、next默认为None
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = Node()      #头结点
        self.size = 0
    #在链尾添加节点，O(n)
    def add_last(self,value):
        new_node = Node(value)  #创建一个节点，使用new_node与node进行区分
        node = self.head    #node值头结点
        while node.next != None:     #循环，当node节点为链尾时退出
            node = node.next
        node.next = new_node    #添加节点
        self.size += 1
    #在链头添加节点,O(1)
    def add_first(self,value):
        node = Node(value,None)     #调用Node类创建一个节点
        node.next = self.head.next      #node的next指向head.next
        self.head.next = node       #head.next指向node
        self.size += 1
    #移除头节点,返回移除节点的value
    def remove_first(self):
        node = self.head.next
        self.head.next = node.next
        self.size -=1
        return node.value
    #移除链尾节点，返回移除节点的value
    #使用两个节点，prve和node
    def remove_last(self):
        prev = self.head
        node = self.head.next
        while node.next != None:
            prev = prev
            node = prev.next
        node.next = None
        self.size -= 1
        return node.value
    #移除相匹配的节点
    def remove_at(self,target):
        prev = self.head
        node = self.head.next
        while node.value != target:
            prev = node
            node = node.next
        prev.next = node.next
        self.size -= 1
    #输出链表
    def Linkedlist_print(self):
        node = self.head
        while node.next != None:    #循环链表，在node.next为空时退出，即 链尾时退出
            node = node.next
            #print(node,end=" ")     #链表是一个连续的物理地址
            print(node.value,end=" ")
        print('')

if __name__ == '__main__':
    ll = LinkedList()
    ll.add_first(1)
    ll.add_last(3)
    ll.add_first(2)
    ll.remove_at(3)
    ll.Linkedlist_print()
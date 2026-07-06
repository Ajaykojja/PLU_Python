class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
l=Linked_list()
l.insert(50)
l.insert(40)
l.insert(30)
l.insert(20)
l.insert(10)
l.inbet(25,30)
l.dis()
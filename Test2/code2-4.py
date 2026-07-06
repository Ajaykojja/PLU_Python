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
    def count(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        print(count)
l=Linked_list()
l.insert(50)
l.insert(40)
l.insert(30)
l.insert(20)
l.insert(10)
l.count()
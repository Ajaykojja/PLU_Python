class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def add(self, data):
        new = node(data)

        if self.head == None:
            self.head = new
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next


l = linkedlist()

l.add(10)
l.add(20)
l.add(30)
l.add(40)
l.add(50)

l.display()
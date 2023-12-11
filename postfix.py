class Node:
     def __init__(self, data):
         self.data=data
         self.data=Node
class Queue:
    def __init__(self):
        self.head=Node
        self.tail=Node
    def insert(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def delete(self):
        if self.head is Node:
            return Node
        else:
            temp=self.head
            self.head=self.head.next
            return temp.data
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
s=Queue()
s.insert(45)
s.insert(26)
s.insert(62)
s.delete()
s.printlist()
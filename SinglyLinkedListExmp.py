class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__=='__main__':

    lList=LinkedList()
    lList.head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)
    fifth=Node(5)
    sixth=Node(6)
    lList.head.next=second
    second.next=third
    third.next=fourth
    fourth.next=fifth
    fifth.next=sixth
    lList.printList()

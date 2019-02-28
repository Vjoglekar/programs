class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self,head=None):

        self.head=head
        self.size=0

    def enqueue(self,value):

        temp = Node(value)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def dequeue(self):
        
        current = self.head
        while current.next.next != None:
            current = current.next
        else:
            a = current.next.data
            current.next = current.next.next
            self.size -= 1
            
            return a
        

    def isEmpty(self):

        if (self.size == 0):

            return True
        else:
            return False
    def sizeofqueue(self):
        return self.size

    def printqueue(self):

        current = self.head
        while current != None:
            print("--->",current.data, end="")
            current = current.next

        print("\n")
        
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.printqueue()
b=q.sizeofqueue()
print(b)
c=q.dequeue()
print("Poped Element is:",c)
b=q.sizeofqueue()
print(b)
a=q.isEmpty()
print(a)


q.printqueue()


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    

    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def push(self,item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def pop(self):

        a = self.head.data
        self.head = self.head.next
        self.size -= 1
        return a

    def peek(self):

        temp = self.head
        return (temp.data)

    def isEmpty(self):

        if(self.size==0):
            return True
        else:
            return False
    def SizeOfStack(self):

        return(self.size)

    def printStack(self):
        current = self.head
        while current != None:
            print("--->",current.data, end="")
            current = current.next

        print("\n")

s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
a=s.pop()
print("Value poped is:",a)
b=s.SizeOfStack()
print("Size is :",b)
c=s.isEmpty()
print(c)
s.printStack()
d=s.peek()
print(d)
    

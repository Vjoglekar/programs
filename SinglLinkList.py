class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        if(head==None):
            self.size = 0
        else:
            self.size = 1

    def push(self,value):
        temp = Node(vlaue)
        temp.next = self.head
        self.head = temp

    def insert(self,position,value):
        
        temp=Node(value)
        p=1
        tempn=self.head
        while(p < position):
           
          tempn=tempn.next
          
        else:
          
          tempn=temp
          self.size=self.size+1




        
        

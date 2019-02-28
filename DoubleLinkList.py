class Node:

    def __init__(self,data):

        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkList:

    def __init__(self):

        self.head = None
        self.size = 0

    def push(self,value):

        temp = Node(value)
        temp.next = self.head

        if self.head is not None:
            self.head.prev = temp

        else:
            self.head = temp
            self.size = self.size + 1

    def print(

    

                
                

        

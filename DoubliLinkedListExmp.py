class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


    def push(self,new_Data):
        new_node=Node(data=new_Data)
        new_node.next=self.head
        new_node.prev=None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insertA(self,prev_node,New_data):
        if prev_node is None:
            print("Previous Node can not be Null.")

        return

    new_node = Node(New_data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    new_node.prev = prev_node

    if new_node.next is not None:
        new_node.next.prev = new_node


        

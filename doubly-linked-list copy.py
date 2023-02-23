from os import remove


class Node:
    def __init__(self,data,next,prev):
        self.data = data
        self.next = next
        self.prev = prev

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def AtBegining(self,newdata):
        if self.isEmpty():
            print("isempty")
            self.head = self.tail = Node(newdata,None,None) 
        else:
            self.head.prev= Node(newdata,None,self.head)
            self.head = self.head.prev
        self.size = self.size + 1
        print(self.size)

    def AtEnd(self,newdata):
        if self.isEmpty():
            self.head = self.tail = Node(newdata,None,None) 
        else:
            self.tail.next = Node(newdata,self.tail,None)
            self.tail = self.tail.next
        self.size = self.size +1 

    def peekFirst(self):
        if self.isEmpty():
            print("list is empty")
        return self.head.data

    def peekLast(self):
        if self.isEmpty():
            print("list is empty")
        return self.tail.data

    def removeFirst(self):
        if self.isEmpty():
            print("list is empty")

        self.head = self.head.next
        self.size = self.size -1

    def removeLast(self):
        if self.isEmpty():
            print("list is empty")
        
        self.tail = self.tail.prev
        self.size = self.size -1

    def remove(self,node):
        
        if node.prev is None :
            self.removeFirst()
        elif node.next is None:
            self.removeLast()
        
        prevnode = node.prev
        nextnode = node.next

        prevnode.next = nextnode
        nextnode.prev = prevnode

        self.size = self.size - 1 

    # time complexity is o(n)
    def removeIndex(self,index):

        if index < 0 or index > self.size():
            print("index out of bound")
        
        #search for index in first half of ll
        if index <  self.size()/2:
            i = 0
            trav = self.head
            while i!=index :
                i = i +1
                trav = trav.next
            print(trav)
        else:
            i = self.size() - 1
            trav = self.tail
            while i!=index  & index > self.size()/2:
                i = i - 1
                trav = trav.prev
            print(trav)

        self.remove(trav)

    def indexOf(self,obj):
        

     
    
    # def Insert(self,prev_node,newval):
    #     NewNode = Node(newval)
    #     nextnode = prev_node.next
        
    #     NewNode.next = nextnode
    #     nextnode.prev = NewNode
        
    #     prev_node.next = NewNode
    #     NewNode.prev = prev_node

    

    # def InBetween(self,middle_node,newdata):

    #     if middle_node is None:
    #         print("middle node is null")
    #         return 
    #     NewNode = Node("Sat")
    #     NewNode.next = middle_node.next
    #     middle_node.next = NewNode

    # def RemoveNode(self,removenode):
    #     if removenode is None:
    #         print("middle node is null")
    #         return 
    #     curr = self.head
    #     prev = self.head
    #     while curr is not None:
    #         if curr.data == removenode:
    #             break
    #         else:
    #             prev = curr
    #             curr = curr.next
        
    #     nextnode = curr.next
    #     prev.next = nextnode

    def printll(self):
        printvalue = self.head
        while printvalue is not None:
            print(printvalue.data)
            print(printvalue.prev)
            print(printvalue.next)
            printvalue = printvalue.next
        


list1 = SLinkedList()
#list1.head = Node ("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
# list1.head.next = e2
# e2.next = e3

#insert at the begining
list1.AtBegining("Sun")
list1.AtBegining("Mon")
list1.printll()

print("-----")
#insert
# list1.Insert(list1.head,"Sun1")
# list1.printll()

# # at the end
# list1.AtEnd("Thur")
# list1.printll()

# # in between 

# list1.InBetween(list1.head,"Sat")
# list1.printll()

# # remove node
# print("-----")
# list1.RemoveNode("Sat")
# list1.printll()
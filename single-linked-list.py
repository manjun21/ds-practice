from os import remove


class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        curr = self.headval
        while curr is not None:            
            if curr.nextval is None:
                break
            curr = curr.nextval
        curr.nextval = NewNode

    def InBetween(self,middle_node,newdata):

        if middle_node is None:
            print("middle node is null")
            return 
        NewNode = Node("Sat")
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def RemoveNode(self,removenode):
        if removenode is None:
            print("middle node is null")
            return 
        curr = self.headval
        prev = self.headval
        while curr is not None:
            if curr.dataval == removenode:
                break
            else:
                prev = curr
                curr = curr.nextval
        
        nextnode = curr.nextval
        prev.nextval = nextnode

    def printll(self):
        printvalue = self.headval
        while printvalue is not None:
            print(printvalue.dataval)
            printvalue = printvalue.nextval
        


list1 = SLinkedList()
list1.headval = Node ("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3

#insert at the begining
list1.AtBegining("Sun")
list1.printll()

# at the end
list1.AtEnd("Thur")
list1.printll()

# in between 
print("-----")
list1.InBetween(list1.headval,"Sat")
list1.printll()

# remove node
print("-----")
list1.RemoveNode("Sat")
list1.printll()
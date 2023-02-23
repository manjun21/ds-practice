#https://leetcode.com/problems/min-stack/
import math
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minval=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.minval) == 0:
            self.minval.append(x)
            self.stack.append(x)
        elif (x < self.minval[-1]):
            self.minval.append(x)
            self.stack.append(x)
        else:
            self.stack.append(x)
            self.minval.append(self.minval[-1])
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minval.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval[-1]

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
r = obj.getMin()
print(r)
obj.pop()
print(obj.top())
r = obj.getMin()
print(r)
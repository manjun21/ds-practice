class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return len(self.A)

    def __getitem__(self,k):
        return self.A[k]

    def append(self,ele):
        if self.__len__() + 1 <= self.capacity:
            self.A.append(ele)
        else:
           B = self.make_array(self.capacity *2) 
           # copy the elements from A to B
           for elem in self.A:
               B[elem] = self.A[elem]

        self.A = B
                
    def insertAt(self,item,index):

    def delete (self):


    def removeAt(self,index):


    def _resize(self,new_cap):

    def make_array(self,new_cap):
        return [new_cap]




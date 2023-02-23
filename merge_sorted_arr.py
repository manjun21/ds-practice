def arrayMerger(array1,array2):
  array3= [] #Array3 will contain merged sorted elements of both array1 and array2
  i=0 #Counter variables
  j=0 
  k=0
  size1 = len(array1)
  size2 = len(array2)
  
  while i < size1 and j < size2:
    #Comparing the elements of both arrays and storing in new array
      if array1[i] < array2[j]:
          array3.append(array1[i])
          i += 1
             
      else:
          array3.append(array2[j])
          j += 1
                   
  #Store remaining elements of first array
  print(i)
  print(j)
  print(array3)
  while i < size1:
        array3.append(array1[i])
        i += 1
 
  #Store remaining elements of second array
  
  while j < size2:
      array3.append(array2[j])
      j += 1
 
# Driver code
array1 = [2,5,8]
array2 = [1,3,4]

arrayMerger(array1, array2)
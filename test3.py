#For arr = [1, 2, 1, 2, 1], the output should be solution(arr) = 10.
#All contiguous subarrays containing at least two elements satisfy the condition of problem. There are 10 possible contiguous subarrays containing at least two elements, so the answer is 10.


#
#1, 2
#2,1
#1,2,1

#2,1
#1,2
#2,1,2

#1,2
#2,1
#1,2,1
# all done the take one more


#arr = [1, 2, 1, 2, 1]
arr = [9, 8, 7, 6, 5]
output = []
print('len:'+str(len(arr)))
cnt_order = True
for j in range(1,len(arr)-1):
    left = False
    right = False
    print('j'+str(j))
    print(output)
    if arr[j] > arr[j-1] or arr[j] < arr[j-1]:
        output.append([arr[j-1],arr[j]])
        left= True
    
    if arr[j] > arr[j+1] or arr[j] < arr[j+1]:
        output.append([arr[j],arr[j+1]])
        right = True
    
    if arr[j] == arr[j-1] or arr[j] == arr[j+1]:
        cnt_order = False
       
    if left and right:
        output.append([arr[j-1],arr[j],arr[j+1]])
    
    j = j +1

if cnt_order:
    output.append(arr)

print('---')
print(output)

        

        


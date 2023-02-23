#code = [5,7,1,4], k = 3
# replace 5 with sum(7,1,4) = 12
# replace 7 with sim(1,4) = 5
# replace 1 with 4 = 1
#[2,4,9,3]
##[4,9,3,2]
# 12 = 3 +9
#[4,9,3,2]
#[9,3,2,4]
#[3,2,4,9]

# code = [5,7,1,4]
# k = 3
code = [2,4,9,3]
k = -2
if k > 0:
    newArr = []
    i = 0
    while i < len(code):
        v = code.pop(i)
        sum = 0
        for j in code:
            sum = sum + j
        newArr.append(sum)
        code.insert(i,v)
        i = i +1
    print(newArr)
elif k == 0:
    newArr = []*len(code)
    print(newArr)
elif k < 0:
    newArr = []
    i = len(code)
    while i > 0:
        sum = 0
        for j in range(len(code)-1,abs(k)-1,-1):
            sum = sum + code[j]
        newArr.append(sum)
        v = code.pop(0)
        code.append(v)
        i = i - 1
    print(newArr)
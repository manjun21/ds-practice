n = 234
res = 0 
mask = 1
for i in range(0,32):
    if n & mask:
        res = res + 1
    if i !=31:
        res <<=1
    mask <<=1
print(res)
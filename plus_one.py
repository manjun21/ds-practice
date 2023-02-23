
def plusOne(digits) -> list:

    output = []
    carry = 1 
    while digits or carry:
        rval = digits.pop() if digits else 0
        sum = rval + carry
        num = sum %10
        carry = sum //10
        output.append(num)
        digits = digits if digits!=None and len(digits)> 0 else None
    return output[::-1]




digits = [9]
#Output: [1,2,4]
print(plusOne(digits))

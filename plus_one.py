#https://leetcode.com/problems/plus-one/

def plusOne(digits: list[int]) -> list[int]:
    carry = 1
    output = [] 
    while digits or carry:
        rightVal = digits.pop() if digits else 0
        print(rightVal)
        sum = rightVal + carry
        rem = sum %10
        carry = sum //10
        output.append(rem)
        print(output)
        digits = digits if digits!=None and len(digits)!=0 else None

    return output[::-1]

digits = [1,2,3]
print(plusOne(digits))

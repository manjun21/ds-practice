class Solution:
    def plusOne(self,digits: List[int]) -> List[int]:

        digits = digits[::-1]
        i = 0
        carry = 1
        while carry == 1:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] = digits[i] +1
                    carry = 0
            else:
                digits.append("1")
                carry = 0

            i = i +1
        return digits[::-1]
    
#https://leetcode.com/problems/license-key-formatting/

def licenseKeyFormatting(s: str, k: int) -> str:
        
        firstDashIndex = s.index("-")
        output = s[0:firstDashIndex] + '-'
        count = 0
        for i in range(firstDashIndex+1,len(s)):
            print(s[i])
            if s[i] == "-":
                continue
            if count < k: 
                if s[i].isalpha():
                    output = output + s[i].upper()
                else:
                    output = output + s[i]
                count = count + 1
            else:
                count = 0
                output= output + '-'
                if s[i].isalpha():
                    output = output + s[i].upper()
                else:
                    output = output + s[i] 
                
        return output

s = "2-5g-3-J"
k = 2
print(licenseKeyFormatting(s,k))
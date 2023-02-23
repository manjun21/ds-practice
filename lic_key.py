def licenseKeyFormatting(s: str, k: int) -> str:
    s1 = s.replace('-','')
    output = []
    s1 = s1[::-1]
    i =0
    while i < len(s1):
        output.append(s1[i:i+k])  
        i = i +k
    output = '-'.join(output)

s = "2-5g-3-J"
k = 2
#Output: "2-5G-3J"
licenseKeyFormatting(s,k)
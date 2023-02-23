
#you'll compare them based on how many times they occur in their respective initial strings 
# map of index of characters
#fewer occurrences means the character is considered smaller
# If the number of occurrences are equal, 
# then the characters should be compared in the usual lexicographical way
#If both number of occurences and characters are equal, 
# you should take the characters from the first string to the result

# s1 = "dce"
#s2 = "cccbd",

# l1 = []
# for i in s1:
#     l1.add(i)

# l2 =[]
# for i in s2:
#     l2.add(i)

# i = 0
# j = 0
# output = ""

# inter_set = set(l1).intersection(set(l2))
# if len(inter_set) == 0 :
#     output = s1 +s2
# else:

#     for n in inter_set:
#         v1 = l1.count(n)
#         print(v1)
#         v2 = l2.count(n)
#         print(v2)

#         if v1 == 0:
#             output = output + s1[i]
#             i = i +1
#         elif v2 == 0:
#             output = output + s2[j]
#             j = j +1
#         elif v1 < v2:
#             output = output + s1[i]
#             i = i +1
#         elif v1 > v2:
#             output = output + s2[j]
#             j = j +1
#         else:
#             print('occurance  are equal')
#             if ord(s1[i]) < ord(s2[j]):
#                 output = output+ s1[i]
#                 i = i +1
#             elif ord(s1[i]) > ord(s2[j]):
#                 output = output+ s2[j]
#                 j = j +1
#             else:
#                 print('both char and occurance are equal')
#                 output = output+ s1[i]
#                 i = i +1
 # record appear times
def mergeStrings(s1, s2):
    
    # record appear times
    record1 = {}
    record2 = {}
    for ch in s1:
        record1[ch] = record1.get(ch,0)+1
    for ch in s2:
        record2[ch] = record2.get(ch,0)+1
    
    # merge with two pointers
    pt1 = 0
    pt2 = 0
    len1 = len(s1)
    len2 = len(s2)
    res = []
    while pt1 < len1 and pt2 < len2:
        if record1[s1[pt1]] < record2[s2[pt2]]:
            res.append(s1[pt1])
            pt1 += 1
        elif record1[s1[pt1]] > record2[s2[pt2]]:
            res.append(s2[pt2])
            pt2 += 1
        else:
            # if equal times
            print(s1[pt1])
            print(s2[pt2])
            if s1[pt1] <= s2[pt2]:
                res.append(s1[pt1])
                pt1 += 1
            elif s1[pt1] > s2[pt2]:
                res.append(s2[pt2])
                pt2 += 1
                
    # continue with the remaining characters
    while pt1 < len1:
        res.append(s1[pt1])
        pt1 += 1
    
    while pt2 < len2:
        res.append(s2[pt2])
        pt2 += 1
    print(res)
    return "".join(res)

s1 = "dce"
s2 = "cccbd"

print(mergeStrings(s1,s2))
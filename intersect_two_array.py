
def intersect(nums1, nums2) -> list:
    nums1.sort()
    nums2.sort()
    i = 0 
    j = 0 
    output = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i = i +1
        elif nums1[i] > nums2[j]:
            j = j +1
        else:
            output.append(nums1[i])
            i = i +1
            j = j +1
    return output

#Input: 
nums1 = [1,2,2,1]
nums2 = [2,2]
#Output: [2,2]

print(intersect(nums1, nums2))
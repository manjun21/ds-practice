def subsets(nums: list[int]) -> list[list[int]]:
        subsets = []
        # start by adding the empty subset
        subsets.append([])
        for currentNumber in nums:
            # we will take all existing subsets and insert the current number in them to create new subsets
            n = len(subsets)
            for i in range(n):
                # create a new subset from the existing subset and insert the current element to it
                set1 = list[subsets[i]]
                set1.append(currentNumber)
                subsets.append(set1)

        return subsets
      
def main():
    v = [1,2,3]
    print(subsets(v))

main()
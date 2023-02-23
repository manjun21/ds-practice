import collections
import math
def sumFourDivisors(nums: list[int]) -> int:
        answer = 0
        divisors = collections.defaultdict(list)
        for index, num in enumerate(nums):
            i =  1
            print('math.sqrt(num)'+str(num) + "value is"+str(math.sqrt(num)))
            while i <= math.sqrt(num):
                if num % i == 0:
                    if num//i != i:
                        divisors[(index,num)].append(num//i)
                    divisors[(index,num)].append(i)
                i += 1
        print(divisors)
        for key, val in divisors.items():
            if len(val) == 4:
                answer += (sum(val))
        return answer

sumFourDivisors([21,4,7])
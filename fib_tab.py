def calculateFibonacci(n):
  dp = [0, 1]
  for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])
  print(dp)
  return dp[n]


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  # print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  # print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()
def Fibonacci(n):
  if (n <= 1):
      return n
  else:
      return Fibonacci(n - 1) + Fibonacci(n - 2)


# Main code
result = Fibonacci(6)
print(f"The 6th Fibonacci number is: {result}")
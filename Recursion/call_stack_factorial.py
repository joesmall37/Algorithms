# Write a factorial that, given a positive integer as input, returns the product of every integer from 1 up to the input. If the input is less than 2, return 1.

def factorial(n):
    # base case
  if n <= 1:
    return 1
  else:
    #   remove one input from the stack and call the function recursively 
    return n * factorial(n - 1)


print(factorial(3))

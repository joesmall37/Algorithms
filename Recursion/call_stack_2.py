# Write a function that takes an integer as an input and returns the sum of all numbers from the input down to 0.

def sum_to_zero(n):
    # print base case
    if n == 0:
        return n
    # if we are not at the base case - if n is not yet zero, then
    print("This is a recursive function with input {0}".format(n))
    # call the fnction recursively and remove one number from the stack to reach the base case
    return n + sum_to_zero(n - 1)


# call the function with an input
print(sum_to_zero(10))

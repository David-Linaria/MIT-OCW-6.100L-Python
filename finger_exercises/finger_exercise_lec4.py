# Assume you are given a positive integer variable named N.
# Write a piece of Python code that finds the cube root of N. T
# the code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube.
# Hint: use a loop that increments a counter—you decide when the counter should stop.

N = int(input('Please put in a positive integer and we will find out if it is a perfect cube: '))
num = 0
while num ** 3 < N:
    num += 1
if num ** 3 == N:
    print(f'{num} is the cube root of {N}.')
else:
    print(f'{N} is not a perfect square.')
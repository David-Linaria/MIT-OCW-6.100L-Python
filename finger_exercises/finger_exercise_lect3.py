# Assume you are given a positive integer variable named N.
# Write a piece of Python code that prints hello world on separate lines, N times.
# You can use either a while loop or a for loop.

N = int(input('Please put in an positive integer: '))
for i in range(0,N,1):
    print(f'Hello world')
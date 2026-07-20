# Assume you are given an integer 0<=N<=100  .
# Write a piece of Python code that uses bisection search to guess N.
# The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N.
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

N = int(input('Please put in a positive integer N that is bellow 100: '))
low = 0
high = 100
guess = (low + high) // 2
count = 0

while guess != N:
    count += 1
    if guess > N:
        high = guess
    else:
        low = guess
    guess = (low + high) // 2

print(f'It takes {count} times to guess N.')
print(f'N is {guess}.')
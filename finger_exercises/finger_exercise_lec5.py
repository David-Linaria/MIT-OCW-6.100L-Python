# Assume you are given a string variable named my_str.
# Write a piece of Python code that prints out a new string containing the even indexed characters of my_str.
# For example, if my_str = "abcdefg" then your code should print out aceg.

text = input('Please put in a string of texts: ')
output = ''
count = 0
for i in text:
    if not count % 2:
        output += i
    count += 1
print(f'even indexed characters: {output}.')
# # Whether the variable in the for loop is isolated from the main codes
# n = 3
# print(f'Before the loop, n is {n}')
# print(f'\nLoop starts:\n')
# for n in range(10):
#     print(f'{n}')
# print(f'\nAfter the loop, n is {n}')
# # It shows that n is exactly the n in the main block. However, n will starts at 0 despite its initial value.

# # How return functions in python
# def main():
#     x = int(input('Please put in a number and we will check if it is a perfect square: '))
#     guess = 0
#     while guess ** 2 < x:
#         guess += 1
#     if guess ** 2 == x:
#         print(f'{x} is the square of {guess}')
#         return
#     print(f'{x} is not a perfect square.')
#
# main()
# # oh now i am clear about how main function works. great.

# """ What if the function returns a string? can it be used in print()?"""
# def return_str():
#     x = 3
#     return f'{x} it can be printed'
#
# return_str()
# print(return_str())
# # from this example we can see that returning a sentence is valid in python, and it could be called in print().

# tup1 = [9, 3, 3, 1]
# tup2 = [1, 4, 6, 4]
# for i in range(len(tup1)):
#     temp = tup1[i] * tup2[i]
#     print(temp)
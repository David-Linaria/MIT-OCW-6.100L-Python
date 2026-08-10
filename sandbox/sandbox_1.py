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

# line = 'abcdefg'
# # newl = line[6::-1]
# # print(f'{newl}')
#
# def sum_digits(s):
#     total = 0
#     for char in s:
#         if char in '0123456789':
#             total += int(char)
#     return total
#
# def sum_digits(s):
#     total = 0
#     for char in s:
#         try:
#             charinint = int(char)
#             total += charinint
#         except:
#             print(f'Invalid input: {char}')
#             continue
#         else:
#             print('No error occurred.')
#         finally:
#             print('Present Loop Finished.')
#     return total
#
# sum_digits('1234')
# print(sum_digits('shi34h5u'))

# def sum_digits_except(s):
#     """ s is a non-empty string containing digits
#     Returns sum of all characters that are digits """
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except:
#             print("couldn't convert character", char)
#             # will iterate as usual, not breaking
#     return total
#
# print(sum_digits_except("123"))
# print(sum_digits_except("123abc"))

# def list_add(l1):
#     """
#     :param l1: a list with only integer as elements, but we do not know the inside structure. for example, it can be a list containing lists.
#     :return: the sum of all integers in list l1.
#     """
#     if len(l1) == 0:
#         return 0
#     else:
#         try:
#             return l1[0] + list_add(l1[1:len(l1):1])
#         except:
#             return list_add(l1[0]) + list_add(l1[1:len(l1):1])
#
# print(list_add([[2, [1, 0, 3]], 1, [5, 2, 2]]))

print(0.631 % 0.01)
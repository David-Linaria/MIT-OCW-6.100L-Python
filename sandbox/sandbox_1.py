# Whether the variable in the for loop is isolated from the main codes
n = 3
print(f'Before the loop, n is {n}')
print(f'\nLoop starts:\n')
for n in range(10):
    print(f'{n}')
print(f'\nAfter the loop, n is {n}')
# It shows that n is exactly the n in the main block. However, n will starts at 0 despite its initial value.


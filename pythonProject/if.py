import math

user_input = input()
if user_input == 'square':
    num = float(input())
    size = num * num
    result = f'{size:.3f}'
    print(result)
elif user_input == 'rectangle':
    num1 = float(input())
    num2 = float(input())
    size = 2 * ( num1 + num2 )
    result = f'{size:.3f}'
    print(result)
elif user_input == 'circle':
    r = float(input())
    size = round(math.pi * r * r, 3)
    result = f'{size:.3f}'
    print(result)
elif user_input == 'triangle':
    num1 = float(input())
    num2 = float(input())
    size = (num1 * num2) / 2
    result = f'{size:.3f}'
    print(result)


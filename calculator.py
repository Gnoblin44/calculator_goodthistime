
# first calculator
print('Your choices are: add, sub, mult, div, pow\n')

def calculator(x, y):
    operator = input("Enter a operation: ")
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mult':
        return x * y
    elif operator == 'div':
        return x / y
    elif operator == 'pow':
        return x ** y
    else:
        print('This is not the right operator ')
print(calculator(3, 8))
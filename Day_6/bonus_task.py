operation = input("Please Enter the operation you want to do \nadd\nsubtract\nmultiply\ndivide\nYour choice: ")
numbers = input("Please Enter numbers separated by spaces: ")
list_of_numbers = list(map(float, numbers.split()))

add = lambda list_of_numbers: sum(list_of_numbers)
subtract = lambda list_of_numbers: list_of_numbers[0] - sum(list_of_numbers[1:])
def multiply(list_of_numbers):
    result = 1
    for number in list_of_numbers:
        result *= number
    return result
def divide(list_of_numbers):
    result = list_of_numbers[0]
    try:
        if 0 in list_of_numbers[1:]:
            result = list_of_numbers[0]

        for number in list_of_numbers[1:]:
            result /= number
        return result
    except ZeroDivisionError:
        print("You Dividing by zero!!!")
        return None

def calculator(list_of_numbers, operation):
    if operation == 'add':
        result = add(list_of_numbers)
    elif operation == 'sub':
        result = subtract(list_of_numbers)
    elif operation == 'mul':
        result = multiply(list_of_numbers)
    elif operation == 'div':
        result = divide(list_of_numbers)
    else:
        print("Invalid operation selected.")
        return None
    return result

result = calculator(list_of_numbers, operation)
if result is not None:
    print("Result is:", result)

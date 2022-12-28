def add(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


def sub(numbers):
    dif = 0
    for i in numbers:
        dif -= i
    return dif


def divide(numbers):
    numbers = sorted(numbers, reverse=True)
    div = numbers[0]
    i = numbers[1]
    for i in numbers:
        div /= i
    return div


def multiply(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product


operations = input("Enter the operation you want to perform: +, -, *, / :")
numbers = []
print("Enter the Operands, if finished(enter done)")
while True:
    operand = input("->")
    if operand == 'done' or operand == 'Done' or operand == 'DONE':
        break
    numbers.append(int(operand))

if operations == '+':
    print("The sum is:", add(numbers))
elif operations == "-":
    print("The difference is: ", sub(numbers))
elif operations == '*':
    print("The product is: ", multiply(numbers))
elif operations == '/':
    print("After division the answer is: ", divide(numbers))
else:
    print("INVALID OPERATIONS!! TRY AGAIN")

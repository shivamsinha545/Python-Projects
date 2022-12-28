def sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


def sub(numbers):
    ans = 0
    for i in numbers:
        ans -= i
    return ans


def mul(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product


def div(numbers):
    numbers = sorted(numbers, reverse=True)
    div = numbers[0]
    i = 1
    for i in numbers:
        div /= i
    return div


operation = input("Enter the operation you want to perform: * , /, +, -: ")
numbers = []
print("Enter Operands(when finish enter done): ")
while True:
    operand = str(input("->"))
    if operand == "done":
        break
    numbers.append(int(operand))

if operation == "*":
    print(mul(numbers))
elif operation == "/":
    print(div(numbers))
elif operation == '+':
    print(sum(numbers))
elif operation=='-':
    print(sub(numbers))
else:
    print("invalid option!!! try again")

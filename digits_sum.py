def sum_of_digits(number):
    sum = 0
    while (number > 0):
        lastdigit = number % 10
        sum += lastdigit
        number = number // 10
    return sum


number = 12345
result = sum_of_digits(number)
print(f"The sum of digits {number} is: {result}")

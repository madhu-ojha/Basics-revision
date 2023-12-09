# Program to find Nth Fibonacci Number

def fibonacci(number):
    fterm = 0
    sterm = 1
    if number < 0:
        print("Error! Enter number greater than 0.")
    elif number == 1:
        print(fterm)
    elif number == 2:
        print(sterm)
    else:
        for i in range(2, number):
            term = fterm + sterm
            fterm = sterm
            sterm = term
        print(term)


number = int(input("Enter nth fibonacci number you want to print: "))
fibonacci(number)

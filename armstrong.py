# program to check whether the given number is Armstrong’s number or not

def armstrong(num):
    st_num = str(num)
    number = num
    sum = 0
    length = len(st_num)
    while number > 0:
        lastdigit = number % 10
        a = pow(lastdigit, length)
        sum += a
        number //= 10
    # print(sum)
    # print(num)
    if (sum == num):
        print("The number is Armstrong's number.")
    else:
        print("The number is not Armstrong's number.")


armstrong(153)

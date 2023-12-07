# takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.

def sum_even_odd(numbers):
    sum_even = 0
    sum_odd = 0

    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return [sum_even, sum_odd]


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input(f"Enter element [{i}]: "))
    # adding the element
    my_lst.append(ele)

result = sum_even_odd(my_lst)
print(result)

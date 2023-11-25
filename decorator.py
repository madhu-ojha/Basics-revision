# def my_function(fx):
#     def result():
#         fx()
#         print("Hi")
#     return result


# @my_function
# def sen():
#     print("Hey! this is a function")


# sen()

def sum(fx):

    def result(*args):
        fx(*args)
        print("Decorated!!")
    return result


@sum
def add(a, b):
    print("Sum is :", a+b)


add(2, 3)

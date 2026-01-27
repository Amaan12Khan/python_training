# 1. Write a python program to create a simple function which prints “TasiNCoder”.

def print_name():
    print("TasiNCoder")

print_name()
# 2. Write a python program to create a function which expects two arguments and print them.

def print_two(a, b):
    print("First argument:", a)
    print("Second argument:", b)

print_two(10, 20)


# 3. Write a python program to create a function which expects an unknown number of arguments.

def print_args(*args):
    print("Arguments received:", args)

print_args(1, 2, 3, 4, 5)


# 4. Write a python program to create a function which expects keyword arguments (**kwargs)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_kwargs(name="Amaan", age=18, city="Delhi")


# 5. Write a python program to create a function which expects a list as an argument.


def print_list(lst):
    print("List elements are:")
    for item in lst:
        print(item)

print_list([10, 20, 30, 40])


# 6. Write a python program to create a function that finds the maximum of four numbers.


def max_of_four(a, b, c, d):
    return max(a, b, c, d)

print("Maximum number:", max_of_four(10, 25, 5, 40))


# 7. Write a python program to sum all the numbers in a list.


def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

print("Sum of list:", sum_of_list([1, 2, 3, 4, 5]))

# 8. Write a python program to multiply all the numbers in a list.

def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

print("Multiplication of list:", multiply_list([1, 2, 3, 4]))


# 9. Write a python program to create a function to check whether a number falls in a given range.

def check_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

print("Number in range:", check_range(5, 1, 10))


# 10. Write a python program to create a function to check whether a given number is even or odd.


def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number is:", even_or_odd(7))

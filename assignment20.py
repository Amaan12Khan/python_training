# 1. Write a python program to create a function that takes a list and returns a new list with unique elements.
def unique_list(lst):
    return list(set(lst))

print(unique_list([1, 2, 2, 3, 4, 4, 5]))


# 2. Write a python program to create a function that takes a number and checks if it is prime or not.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))

# 3. Write a python program to create a function that prints the even numbers from a given list.

def print_even(lst):
    for num in lst:
        if num % 2 == 0:
            print(num, end=" ")

print_even([1, 2, 3, 4, 5, 6, 7, 8, 9])
print()

# 4. Write a python program to create a function that checks whether a string is palindrome or not.


def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))


# 5. Write a python program to create a function to find the minimum of three numbers.


def min_of_three(a, b, c):
    return min(a, b, c)

print(min_of_three(10, 5, 20))


# 6. Write a python program to create a function and print a list of squares from 1 to 30.

def square_list():
    return [x**2 for x in range(1, 31)]

print(square_list())

# 7. Write a python program to access a function inside a function.

def outer_function():
    def inner_function():
        print("Inner function called")
    inner_function()

outer_function()


# 8. Write a python program to create a function that accepts a string and counts upper and lower case letters.

def count_case(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_case("Hello World")


# 9. Write a python program to create a function to check whether a string is a pangram or not.
def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(s.lower()))

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello World"))


# 10. Write a python program to create a function to check whether a string is an anagram or not.

def is_anagram(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

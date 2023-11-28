#!/usr/bin/env python3

def happy_new_year():
    number = 10
    while number >= 1:
        print(number)
        number -= 1
    print("Happy New Year!")

# Call the function to execute the code
happy_new_year()

def square_integers(int_list):
    squared_elements = list()
    for integer in int_list:
        squared_element = integer ** 2
        squared_elements.append(squared_element)
    return squared_elements

        


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

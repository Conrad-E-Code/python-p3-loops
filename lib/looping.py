#!/usr/bin/env python3
import ipdb

def happy_new_year():
    # code goes here!
    timer = 10
    while timer > 0:
         print(timer)
         timer -= 1
         if timer ==0:
             print("Happy New Year!")
    pass



def square_integers(int_list):
    # code goes here!
    squared_list = [my_root * my_root for my_root in int_list ]
    return squared_list
    pass

def fizzbuzz():
    # code goes here!
    myhundred = range(1, 101)
    for num in myhundred:
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 ==0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    pass
# ipdb.set_trace()
#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Jan 2022
# This program calculates average of 10 random numbers

import random


def main():
    # this function displays 10 random number with the array

    my_numbers = []
    average = 0

    for loop_counter in range(0, 10):
        a_number = random.randint(1, 100)
        my_numbers.append(a_number)
        average = average + my_numbers[loop_counter]
        print(
            "The random number is: {0} ".format(my_numbers[loop_counter]), end="" + "\n"
        )
    print("")
    average = average / 10
    print("The average is {0}".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()

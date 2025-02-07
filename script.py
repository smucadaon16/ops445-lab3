#!/usr/bin/env python3
"""
This script creates an indexable, mutable iterable named colours with at least four items. It also defines a function called firsts
that returns the first letter of each item in a list. The function is then called with the colours list to verify its functionality.
"""

# Creating an indexable, mutable iterable named colours
colours = ["red", "blue", "green", "yellow"]

def firsts(lst):
    """
    This function takes a list as a parameter and returns a list of the first letters of each item in the list.

    :param lst: List of strings
    :return: List of first letters of each string in the input list
    """
    return [item[0] for item in lst]

# Call the function with colours and verify its functionality
print(firsts(colours))

cafeteria_food = ("sausage", "hotdog", "cake", "macaroni salad", "soup")

for food in cafeteria_food:
	answer = input("Do you like " + food + "? (yes/no):")

# Answers:
# To save the user's response to each prompt and associate the response with the food in question. We use the dictionary data type.

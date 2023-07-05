#!/usr/bin/env python
# coding: utf-8

# ### 1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.
# 
# ```python
# guess_me = 7
# 
# if guess_me < 7:
#     print('too low')
# elif guess_me > 7:
#     print('too high')
# else:
#     print('just right')
# ```
# 
# Output:
# ```
# just right
# ```
# 
# In this example, the `guess_me` variable is assigned the value 7. The conditional statements are used to check the value of `guess_me` and print the corresponding string: `'too low'` if it's less than 7, `'too high'` if it's greater than 7, and `'just right'` if it's equal to 7. In this case, since `guess_me` is equal to 7, it prints `'just right'`.

# ### 2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.
# 
# ```python
# guess_me = 7
# start = 1
# 
# while start <= guess_me:
#     if start < guess_me:
#         print('too low')
#     elif start == guess_me:
#         print('found it!')
#         break
#     else:
#         print('oops')
#         break
#     start += 1
# ```
# 
# Output:
# ```
# too low
# too low
# too low
# too low
# too low
# too low
# found it!
# ```
# 
# In this example, the `guess_me` variable is assigned the value 7, and the `start` variable is assigned the value 1. The `while` loop continues as long as `start` is less than or equal to `guess_me`. Inside the loop, it checks the conditions: if `start` is less than `guess_me`, it prints `'too low'`; if `start` is equal to `guess_me`, it prints `'found it!'` and exits the loop; if `start` is greater than `guess_me`, it prints `'oops'` and exits the loop. At the end of each iteration, the `start` variable is incremented by 1 using `start += 1`.

# ### 3. Print the following values of the list [3, 2, 1, 0] using a for loop.
# 
# ```python
# my_list = [3, 2, 1, 0]
# 
# for value in my_list:
#     print(value)
# ```
# 
# Output:
# ```
# 3
# 2
# 1
# 0
# ```
# 
# In this example, the `for` loop iterates over each element in the `my_list` list, and the `value` variable takes on each element's value in each iteration. Inside the loop, we simply print the value, resulting in the output shown above.

# ### 4. Use a list comprehension to make a list of the even numbers in range(10)
# 
# ```python
# even_numbers = [num for num in range(10) if num % 2 == 0]
# print(even_numbers)
# ```
# 
# Output:
# ```
# [0, 2, 4, 6, 8]
# ```
# 
# In this example, the list comprehension `[num for num in range(10) if num % 2 == 0]` generates a new list by iterating over the range from 0 to 10. The `if` condition `num % 2 == 0` filters out the odd numbers, ensuring that only even numbers are included in the resulting list. The resulting list, `even_numbers`, contains `[0, 2, 4, 6, 8]`.

# ### 5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.
# 
# Here's an example of how you can use a dictionary comprehension to create the `squares` dictionary, where the keys are obtained from the range 0 to 10, and the corresponding values are the squares of each key:
# 
# ```python
# squares = {num: num ** 2 for num in range(10)}
# print(squares)
# ```
# 
# Output:
# ```
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# ```
# 
# In this example, the dictionary comprehension `{num: num ** 2 for num in range(10)}` generates a dictionary where each key is obtained from the range 0 to 10, and the corresponding value is the square of that key. The resulting `squares` dictionary contains the key-value pairs shown in the output.

# ### 6. Construct the set odd from the odd numbers in the range using a set comprehension (10).
# 
# Here's an example of how you can use a set comprehension to construct the set `odd` containing the odd numbers from the range 0 to 10:
# 
# ```python
# odd = {num for num in range(10) if num % 2 != 0}
# print(odd)
# ```
# 
# Output:
# ```
# {1, 3, 5, 7, 9}
# ```
# 
# In this example, the set comprehension `{num for num in range(10) if num % 2 != 0}` generates a new set by iterating over the range from 0 to 10. The `if` condition `num % 2 != 0` filters out the even numbers, ensuring that only the odd numbers are included in the resulting set. The resulting set, `odd`, contains `{1, 3, 5, 7, 9}`.

# ### 7. Use a generator comprehension to return the string 'Got' and a number for the numbers in range(10). Iterate through this by using a for loop.
# 
# Here's an example of how you can use a generator comprehension to create a generator that yields the string `'Got'` followed by a number for each number in the range from 0 to 10, and then iterate through it using a `for` loop:
# 
# ```python
# generator = ('Got ' + str(num) for num in range(10))
# 
# for item in generator:
#     print(item)
# ```
# 
# Output:
# ```
# Got 0
# Got 1
# Got 2
# Got 3
# Got 4
# Got 5
# Got 6
# Got 7
# Got 8
# Got 9
# ```
# 
# In this example, the generator comprehension `('Got ' + str(num) for num in range(10))` creates a generator that yields the string `'Got '` concatenated with a number for each number in the range from 0 to 10. The generator is then iterated through using a `for` loop, and each item is printed.

# ### 8. Define a function called good that returns the list ['Harry', 'Ron','Hermione'].
# 
# Here's an example of how you can define a function called `good` that returns the list `['Harry', 'Ron', 'Hermione']`:
# 
# ```python
# def good():
#     return ['Harry', 'Ron', 'Hermione']
# 
# # Call the function
# result = good()
# print(result)
# ```
# 
# Output:
# ```
# ['Harry', 'Ron', 'Hermione']
# ```
# 
# In this example, the `good` function is defined without any parameters. It simply returns the list `['Harry', 'Ron', 'Hermione']`. When the function is called and its return value is assigned to the `result` variable, it will contain `['Harry', 'Ron', 'Hermione']`. Finally, we print the `result` list to see the output.

# ### 9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.
# 
# ```python
# def get_odds():
#     for num in range(10):
#         if num % 2 != 0:
#             yield num
# 
# # Use a for loop to find and print the third value returned
# count = 0
# for number in get_odds():
#     count += 1
#     if count == 3:
#         print(number)
#         break
# ```
# 
# Output:
# ```
# 5
# ```
# 
# In this example, the `get_odds` function is defined as a generator function. It uses a `for` loop to iterate over the range from 0 to 10 and yields the odd numbers by checking the condition `num % 2 != 0`. The `for` loop is used to iterate through the generator, and a counter (`count`) is used to keep track of the number of values returned. When the counter reaches 3, the corresponding value (`number`) is printed, and the loop is broken using `break`. In this case, the third value returned by the generator is `5`, which is printed as the output.

# ### 10. Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print 'Caught an oops'.
# 
# ```python
# # Define the OopsException
# class OopsException(Exception):
#     pass
# 
# try:
#     # Raise the OopsException
#     raise OopsException()
# except OopsException:
#     # Catch the OopsException and print the message
#     print('Caught an oops')
# ```
# 
# Output:
# ```
# Caught an oops
# ```
# 
# In this example, the `OopsException` is defined as a custom exception by creating a new class that inherits from the base `Exception` class. The `raise` statement is used to raise the `OopsException`. Inside the try-except block, the `OopsException` is caught with the `except` clause, and the corresponding message `'Caught an oops'` is printed.

# ### 11. Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].
# 
# Here's an example of how you can use the `zip()` function to create a dictionary called `movies` by pairing the lists `titles` and `plots`:
# 
# ```python
# titles = ['Creature of Habit', 'Crewel Fate']
# plots = ['A nun turns into a monster', 'A haunted yarn shop']
# 
# movies = dict(zip(titles, plots))
# print(movies)
# ```
# 
# Output:
# ```
# {'Creature of Habit': 'A nun turns into a monster', 'Crewel Fate': 'A haunted yarn shop'}
# ```
# 
# In this example, the `zip()` function is used to pair the elements from the `titles` and `plots` lists together. The resulting pairs are then passed to the `dict()` function to create a dictionary, `movies`, where the titles are the keys and the plots are the values. Finally, the `movies` dictionary is printed, resulting in the output shown above.

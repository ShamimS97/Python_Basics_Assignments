#!/usr/bin/env python
# coding: utf-8

# # 1. What does an empty dictionary's code look like?
# 
# An empty dictionary in Python is represented by a pair of curly braces `{}`. Here's how the code for an empty dictionary looks like:
# 
# ```python
# my_dict = {}
# ```
# 
# In this code, `my_dict` is an empty dictionary that doesn't contain any key-value pairs. The curly braces `{}` denote the dictionary literal syntax, indicating an empty dictionary.

# # 2. What is the value of a dictionary value with the key 'foo' and the value 42?
# 
# The value of a dictionary with the key `'foo'` and the value `42` would be represented as follows:
# 
# ```python
# my_dict = {'foo': 42}
# ```
# 
# In this code, `my_dict` is a dictionary that contains a single key-value pair. The key `'foo'` is associated with the value `42`. So, accessing `my_dict['foo']` would give you the value `42`.

# # 3. What is the most significant distinction between a dictionary and a list?
# 
# The most significant distinction between a dictionary and a list in Python is the way they store and retrieve data:
# 
# 1. Data Organization:
#    - List: A list is an ordered collection of items that can be of any data type. It stores elements in a sequential manner, and each element is assigned an index based on its position in the list.
#    - Dictionary: A dictionary is an unordered collection of key-value pairs. It associates a unique key with each value, allowing efficient lookup and retrieval of values based on their corresponding keys.
# 
# 2. Accessing Data:
#    - List: In a list, elements are accessed using their indices. You can retrieve elements by their position in the list, starting from index 0.
#    - Dictionary: In a dictionary, elements are accessed using their keys. Instead of indices, you use unique keys to retrieve corresponding values. Dictionary keys can be of immutable data types such as strings, numbers, or tuples.
# 
# 3. Data Mutability:
#    - List: Lists are mutable, meaning you can modify their elements by assigning new values to specific indices. You can add, remove, or modify elements within a list after it's created.
#    - Dictionary: Dictionaries are also mutable. You can add, remove, or modify key-value pairs within a dictionary after it's created. However, the keys themselves are typically immutable.
# 
# 4. Data Ordering:
#    - List: Lists maintain the order of elements as they are inserted. The order of elements in a list is preserved, allowing you to access elements in the same order they were added.
#    - Dictionary: Dictionaries do not guarantee any specific order of key-value pairs. The order of elements in a dictionary is not fixed and may vary during iterations or operations.
# 
# 5. Duplicate Keys:
#    - List: Lists allow duplicate elements. You can have multiple occurrences of the same value within a list.
#    - Dictionary: Dictionary keys must be unique. Each key within a dictionary is associated with a single value, and duplicate keys are not allowed.
# 
# In summary, while both dictionaries and lists are used to store and organize data, dictionaries provide a way to access values using unique keys, whereas lists use indices to access elements in a specific order. Dictionaries excel at efficient lookup and retrieval of values based on keys, while lists are suited for ordered collections of elements.

# # 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# 
# If you try to access `spam['foo']` and `spam` is `{'bar': 100}`, you will encounter a `KeyError` because the key `'foo'` does not exist in the dictionary `spam`.
# 
# Here's an example:
# 
# ```python
# spam = {'bar': 100}
# value = spam['foo']  # This line will raise a KeyError
# ```
# 
# Running this code will result in a `KeyError` with the message `'foo'`. This error occurs because the dictionary `spam` does not have a key `'foo'`, so attempting to access it raises an exception.
# 
# To avoid a `KeyError`, you can use the `get()` method of dictionaries, which allows you to provide a default value to be returned if the key is not found:
# 
# ```python
# spam = {'bar': 100}
# value = spam.get('foo', 'default value')
# print(value)  # Output: 'default value'
# ```
# 
# In this case, since the key `'foo'` is not present in the dictionary `spam`, the `get()` method returns the default value `'default value'` instead of raising a `KeyError`.

# # 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# 
# The expressions `'cat' in spam` and `'cat' in spam.keys()` are slightly different in terms of what they check within the dictionary `spam`:
# 
# 1. `'cat' in spam`:
#    This expression checks whether the key `'cat'` exists in the dictionary `spam`. It returns a Boolean value of `True` if the key is found in the dictionary, and `False` otherwise. It checks for the presence of the key directly within the dictionary's keys.
# 
#    Example:
#    ```python
#    spam = {'cat': 42, 'dog': 17}
#    print('cat' in spam)  # Output: True
#    print('snake' in spam)  # Output: False
#    ```
# 
# 2. `'cat' in spam.keys()`:
#    This expression checks whether the key `'cat'` exists among the keys of the dictionary `spam`. It retrieves the keys of the dictionary using the `keys()` method and then checks if `'cat'` is present in that list of keys. It also returns a Boolean value of `True` if the key is found, and `False` otherwise.
# 
#    Example:
#    ```python
#    spam = {'cat': 42, 'dog': 17}
#    print('cat' in spam.keys())  # Output: True
#    print('snake' in spam.keys())  # Output: False
#    ```
# 
# In practice, both expressions will give the same result because the `in` operator automatically checks the keys of a dictionary. Therefore, `'cat' in spam` is equivalent to `'cat' in spam.keys()`. However, explicitly using `spam.keys()` can be useful when you want to emphasize that you are specifically checking the keys of the dictionary.

# # 6. What is a shortcut for the following code? 
# # if 'color' not in spam: 
# # spam['color'] = 'black'
# 
# A shortcut for the given code can be achieved using the `dict.setdefault()` method. This method allows you to set a default value for a key if it doesn't already exist in the dictionary. Here's the shortcut code:
# 
# ```python
# spam.setdefault('color', 'black')
# ```
# 
# This line of code checks if the key `'color'` is present in the `spam` dictionary. If the key is found, it returns the corresponding value. If the key is not found, it adds the key-value pair `'color': 'black'` to the dictionary.
# 
# Using `setdefault()` eliminates the need for an explicit `if` statement to check the key's presence and set a default value manually.

# # 7. How do you 'pretty print' dictionary values using which module and function?
# 
# To "pretty print" dictionary values in Python, you can use the `pprint` module and its `pprint()` function. The `pprint` module provides a more readable and formatted output for complex data structures like dictionaries. Here's how you can use it:
# 
# ```python
# import pprint
# 
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# pprint.pprint(my_dict)
# ```
# 
# In this code, we import the `pprint` module and create a dictionary `my_dict` containing some key-value pairs. Then, we call `pprint.pprint()` function, passing the dictionary as the argument. This function pretty prints the dictionary, displaying it in a well-organized and visually appealing format.
# 
# The `pprint()` function automatically formats the output, adds line breaks, and indents nested structures to improve readability. It's particularly useful when dealing with large or complex dictionaries or other data structures.

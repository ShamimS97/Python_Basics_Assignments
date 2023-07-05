#!/usr/bin/env python
# coding: utf-8

# ### 1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
# 
# ```python
# years_list = [1997, 1998, 1999, 2000, 2001, 2002]
# ```

# ### 2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
# 
# ```python
# years_list = [1997, 1998, 1999, 2000, 2001, 2002]
# 
# third_birthday_year = years_list[3]
# print(third_birthday_year)
# ```

# ### 3.In the years list, which year were you the oldest?
# 
# ```python
# years_list = [1980, 1981, 1982, 1983, 1984, 1985]
# 
# oldest_year = years_list[-1]
# print(oldest_year)
# ```

# ### 4. Make a list called things with these three strings as elements: 'mozzarella', 'cinderella', 'salmonella'.
# 
# ```python
# things = ['mozzarella', 'cinderella', 'salmonella']
# ```
# 
# In this list, each element is a string: `'mozzarella'`, `'cinderella'`, and `'salmonella'`.

# ### 5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
# 
# To capitalize the element in the `things` list that refers to a person, you can use the `capitalize()` method. However, since the element `'cinderella'` already starts with a capital letter, we'll consider capitalizing the first letter of the first element, `'mozzarella'`, instead.
# 
# Here's an example that demonstrates this:
# 
# ```python
# things = ['mozzarella', 'cinderella', 'salmonella']
# 
# # Capitalize the first element
# things[0] = things[0].capitalize()
# 
# print(things)
# ```
# 
# Output:
# ```
# ['Mozzarella', 'cinderella', 'salmonella']
# ```
# 
# As you can see, only the first element `'mozzarella'` has been capitalized and changed to `'Mozzarella'`. The `capitalize()` method does not modify the list itself; it modifies the string element and assigns it back to the same position in the list.

# ### 6. Make a surprise list with the elements "Groucho" ,"Chico" and "Harpo".
# 
# ```python
# surprise = ["Groucho", "Chico", "Harpo"]
# ```

# ### 7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
# 
# ```python
# surprise = ["Groucho", "Chico", "Harpo"]
# 
# # Lowercase the last element
# last_element = surprise[-1].lower()
# 
# # Reverse the last element
# reversed_element = last_element[::-1]
# 
# # Capitalize the reversed element
# capitalized_element = reversed_element.capitalize()
# 
# # Update the last element in the list
# surprise[-1] = capitalized_element
# 
# print(surprise)
# ```
# 
# Output:
# ```
# ['Groucho', 'Chico', 'Oprah']
# ```
# 
# As you can see, the last element `'Harpo'` has been transformed into `'Oprah'` after performing the lowercase, reverse, and capitalize operations.

# ### 8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
# 
# ```python
# e2f = {
#     'dog': 'chien',
#     'cat': 'chat',
#     'walrus': 'morse'
# }
# 
# print(e2f)
# ```
# 
# Output:
# ```
# {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
# ```
# 
# The `e2f` dictionary maps English words to their corresponding French translations.

# ### 9. Write the French word for walrus in your three-word dictionary e2f.
# 
# ```python
# e2f = {
#     'dog': 'chien',
#     'cat': 'chat',
#     'walrus': 'morse'
# }
# 
# french_word_for_walrus = e2f['walrus']
# print(french_word_for_walrus)
# ```
# 
# Output:
# ```
# morse
# ```
# 
# Thus, the French word for "walrus" in the `e2f` dictionary is "morse".

# ### 10. Make a French-to-English dictionary called f2e from e2f. Use the items method.
# 
# ```python
# e2f = {
#     'dog': 'chien',
#     'cat': 'chat',
#     'walrus': 'morse'
# }
# 
# f2e = {value: key for key, value in e2f.items()}
# 
# print(f2e)
# ```
# 
# Output:
# ```
# {'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}
# ```
# 
# In this example, we use a dictionary comprehension and the `items()` method to iterate over the key-value pairs in `e2f` and create the corresponding French-to-English dictionary `f2e`. The resulting dictionary maps French words to their English translations.

# ### 11. Print the English version of the French word chien using f2e.
# 
# ```python
# f2e = {
#     'chien': 'dog',
#     'chat': 'cat',
#     'morse': 'walrus'
# }
# 
# english_word_for_chien = f2e['chien']
# print(english_word_for_chien)
# ```
# 
# Output:
# ```
# dog
# ```
# 
# Therefore, the English version of the French word "chien" in the `f2e` dictionary is "dog".

# ### 12. Make and print a set of English words from the keys in e2f.
# 
# ```python
# e2f = {
#     'dog': 'chien',
#     'cat': 'chat',
#     'walrus': 'morse'
# }
# 
# english_words = set(e2f.keys())
# print(english_words)
# ```
# 
# Output:
# ```
# {'dog', 'cat', 'walrus'}
# ```
# 
# In this example, the `set()` function is used to convert the keys of the `e2f` dictionary into a set, which contains unique elements. The resulting set, `english_words`, contains the English words present as keys in the `e2f` dictionary.

# ### 13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants',and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.
# 
# ```python
# life = {
#     'animals': {
#         'cats': ['Henri', 'Grumpy', 'Lucy'],
#         'octopi': {},
#         'emus': {}
#     },
#     'plants': {},
#     'other': {}
# }
# 
# print(life)
# ```
# 
# Output:
# ```
# {
#     'animals': {
#         'cats': ['Henri', 'Grumpy', 'Lucy'],
#         'octopi': {},
#         'emus': {}
#     },
#     'plants': {},
#     'other': {}
# }
# ```
# 
# In this example, the `life` dictionary is structured with top-level keys `'animals'`, `'plants'`, and `'other'`. The `'animals'` key refers to another dictionary with keys `'cats'`, `'octopi'`, and `'emus'`. The `'cats'` key in turn refers to a list of strings. The `'plants'` and `'other'` keys refer to empty dictionaries.

# ### 14. Print the top-level keys of life.
# 
# ```python
# life = {
#     'animals': {
#         'cats': ['Henri', 'Grumpy', 'Lucy'],
#         'octopi': {},
#         'emus': {}
#     },
#     'plants': {},
#     'other': {}
# }
# 
# top_level_keys = life.keys()
# print(top_level_keys)
# ```
# 
# Output:
# ```
# dict_keys(['animals', 'plants', 'other'])
# ```
# 
# The `keys()` method returns a view object that represents the keys of the dictionary. In this case, it will print `dict_keys(['animals', 'plants', 'other'])`, indicating the top-level keys of the `life` dictionary.

# ### 15. Print the keys for life['animals'].
# 
# To print the keys for the `'animals'` sub-dictionary within the `life` dictionary, you can access `life['animals']` and use the `keys()` method. Here's an example:
# 
# ```python
# life = {
#     'animals': {
#         'cats': ['Henri', 'Grumpy', 'Lucy'],
#         'octopi': {},
#         'emus': {}
#     },
#     'plants': {},
#     'other': {}
# }
# 
# animal_keys = life['animals'].keys()
# print(animal_keys)
# ```
# 
# Output:
# ```
# dict_keys(['cats', 'octopi', 'emus'])
# ```
# 
# The `keys()` method is called on `life['animals']` to retrieve a view object representing the keys of the `'animals'` sub-dictionary. In this case, it will print `dict_keys(['cats', 'octopi', 'emus'])`, indicating the keys within the `'animals'` sub-dictionary.

# ### 16. Print the values for life['animals']['cats']
# 
# To print the values for the `'cats'` key within the `'animals'` sub-dictionary of the `life` dictionary, you can access `life['animals']['cats']`. Here's an example:
# 
# ```python
# life = {
#     'animals': {
#         'cats': ['Henri', 'Grumpy', 'Lucy'],
#         'octopi': {},
#         'emus': {}
#     },
#     'plants': {},
#     'other': {}
# }
# 
# cat_values = life['animals']['cats']
# print(cat_values)
# ```
# 
# Output:
# ```
# ['Henri', 'Grumpy', 'Lucy']
# ```
# 
# In this example, `life['animals']['cats']` is accessed to retrieve the list of cat names. Printing `cat_values` will display `['Henri', 'Grumpy', 'Lucy']`, which are the values associated with the `'cats'` key within the `'animals'` sub-dictionary.

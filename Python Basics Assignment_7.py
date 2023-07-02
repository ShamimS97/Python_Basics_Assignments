#!/usr/bin/env python
# coding: utf-8

# # 1. What is the name of the feature responsible for generating Regex objects?
# 
# The name of the feature responsible for generating Regex objects in Python is the `re` module. The `re` module provides functions and methods for working with regular expressions in Python. It allows you to create Regex objects and perform various operations such as pattern matching, searching, and replacing within strings.

# # 2. Why do raw strings often appear in Regex objects?
# 
# Raw strings (prefixed with `r`) are often used in Regex objects because they treat backslashes (`\`) as literal characters rather than escape characters. In regular expressions, backslashes are commonly used to escape special characters with special meaning, such as `\d` for matching digits or `\s` for matching whitespace.
# 
# By using raw strings, you can write regular expressions more conveniently without having to escape backslashes multiple times. This is particularly useful in regex patterns that contain a lot of backslashes, as it helps avoid confusion and makes the pattern more readable.
# 
# For example, consider a regular expression pattern that matches a backslash followed by a digit:
# 
# ```python
# import re
# 
# pattern = r'\\(\d)'
# text = r'\7'
# 
# match = re.search(pattern, text)
# if match:
#     print(match.group(1))  # Output: 7
# ```
# 
# In this example, both the regex pattern (`r'\\(\d)'`) and the input text (`r'\7'`) are raw strings. The double backslash `\\` in the pattern is treated as a literal backslash, and the `\d` matches a digit. The input text `r'\7'` contains a backslash followed by the digit `7`. The `re.search()` function is used to search for a match, and the captured group (`match.group(1)`) retrieves the digit `7`.
# 
# Using raw strings with regular expressions helps avoid unnecessary escape characters and makes the pattern more readable and easier to understand.

# # 3. What is the return value of the search() method?
# 
# The return value of the `search()` method from the `re` module in Python is an object of the `Match` class if a match is found, or `None` if no match is found.
# 
# The `Match` object represents the match found by the `search()` method and provides various methods and attributes to retrieve information about the match. Some commonly used methods and attributes of the `Match` object include `group()`, `start()`, `end()`, and `span()`.
# 
# Here's an example that demonstrates the usage of `search()` and accessing the match information:
# 
# ```python
# import re
# 
# pattern = r'(\d+)-(\d+)-(\d+)'  # Pattern to match a date in the format "yyyy-mm-dd"
# text = 'Today is 2023-06-16, and it is a sunny day.'
# 
# match = re.search(pattern, text)
# if match:
#     print('Match found!')
#     print('Full match:', match.group(0))
#     print('Year:', match.group(1))
#     print('Month:', match.group(2))
#     print('Day:', match.group(3))
# else:
#     print('No match found.')
# ```
# 
# In this example, the `search()` method is used to find a match for the date pattern in the given text. If a match is found, it enters the `if` block and retrieves information about the match using the `group()` method. The `group(0)` returns the full match, and `group(1)`, `group(2)`, and `group(3)` return the captured groups representing the year, month, and day, respectively.
# 
# If no match is found, it enters the `else` block and prints a message indicating no match was found.
# 
# Remember that the `search()` method only finds the first occurrence of a match in the text. If you need to find multiple matches, you can use the `finditer()` method or apply the `search()` method iteratively.

# # 4. From a Match item, how do you get the actual strings that match the pattern?
# 
# From a `Match` object, you can retrieve the actual strings that match the pattern using the `group()` method. The `group()` method allows you to access the matched substrings based on their capture groups or the entire match itself.
# 
# Here's an example that demonstrates how to retrieve the matched strings:
# 
# ```python
# import re
# 
# pattern = r'(\d+)-(\d+)-(\d+)'  # Pattern to match a date in the format "yyyy-mm-dd"
# text = 'Today is 2023-06-16, and it is a sunny day.'
# 
# match = re.search(pattern, text)
# if match:
#     print('Full match:', match.group(0))
#     print('Year:', match.group(1))
#     print('Month:', match.group(2))
#     print('Day:', match.group(3))
# else:
#     print('No match found.')
# ```
# 
# In this example, the `search()` method is used to find a match for the date pattern in the given text. If a match is found, it retrieves the matched strings using the `group()` method. The `group(0)` returns the entire match, and `group(1)`, `group(2)`, and `group(3)` return the captured groups representing the year, month, and day, respectively.
# 
# The `group()` method can also accept multiple arguments to retrieve multiple capture groups in a single call. For example, `match.group(1, 2)` would return a tuple containing the matched strings of capture group 1 and capture group 2.
# 
# If you want to retrieve all the captured groups as a list, you can use the `groups()` method, which returns all the captured groups in the order they appear.
# 
# Remember to check if a match was found before accessing the matched strings to avoid `AttributeError` exceptions.

# # 5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover? Group 2? Group 1?
# 
# In the regex pattern `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`:
# 
# - Group zero (`group(0)`) covers the entire match of the pattern, including both capture groups. It represents the full matched string.
# 
# - Group two (`group(2)`) covers the second capture group in the pattern, which is `(\d\d\d-\d\d\d\d)`. It represents the portion of the string that matches the second set of parentheses.
# 
# - Group one (`group(1)`) covers the first capture group in the pattern, which is `(\d\d\d)`. It represents the portion of the string that matches the first set of parentheses.
# 
# Here's an example demonstrating the usage of these groups:
# 
# ```python
# import re
# 
# pattern = r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
# text = 'Phone number: 123-456-7890'
# 
# match = re.search(pattern, text)
# if match:
#     print('Full match:', match.group(0))
#     print('Group 1:', match.group(1))
#     print('Group 2:', match.group(2))
# ```
# 
# Output:
# ```
# Full match: 123-456-7890
# Group 1: 123
# Group 2: 456-7890
# ```
# 
# In this example, the regex pattern is used to search for a phone number in the given text. The `search()` method finds the first match, and then the `group()` method is used to access the matched strings. `group(0)` returns the full match, `group(1)` returns the first capture group (area code), and `group(2)` returns the second capture group (remaining digits of the phone number).
# 
# Note that group indexing starts from 1, where group 0 represents the full match.

# # 6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex that you want it to fit real parentheses and periods?
# 
# In standard regular expression syntax, parentheses and intervals have special meanings for grouping and specifying repetition, respectively. If you want to match literal parentheses or periods in a regular expression, you can use the backslash `\` character to escape them.
# 
# To match a literal parentheses `(` or `)`, you can use `\(` and `\)`, respectively.
# 
# To match a literal period `.`, you can use `\.`.
# 
# Here's an example that demonstrates how to use the backslash to escape parentheses and periods in a regular expression:
# 
# ```python
# import re
# 
# text = 'I have (parentheses) and a period.'
# 
# # Matching literal parentheses and period
# pattern = r'\(parentheses\)\.'
# match = re.search(pattern, text)
# if match:
#     print('Match found:', match.group())
# else:
#     print('No match found.')
# ```
# 
# Output:
# ```
# Match found: (parentheses).
# ```
# 
# In this example, the regular expression pattern `\(` matches the literal opening parenthesis, `\)` matches the literal closing parenthesis, and `\.` matches the literal period. The backslash `\` escapes the special meaning of these characters and treats them as literal characters to match.
# 
# By using the backslash to escape parentheses and periods, you can explicitly tell the regex engine that you want to match the real parentheses and periods instead of interpreting them as special characters with their respective meanings in regular expressions.

# # 7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?
# 
# The `findall()` method in Python's regular expression module `re` returns either a list of strings or a list of string tuples based on the presence of capturing groups in the regular expression pattern.
# 
# If the regular expression pattern contains one or more capturing groups defined by parentheses, `findall()` returns a list of string tuples. Each tuple represents a match, and each element in the tuple corresponds to a capturing group in the pattern.
# 
# If the regular expression pattern does not contain any capturing groups, `findall()` returns a list of strings. Each string in the list represents a complete match found in the input string.
# 
# Here's an example to illustrate the behavior:
# 
# ```python
# import re
# 
# text = 'The numbers are 123 and 456.'
# 
# # Pattern with capturing groups
# pattern_with_groups = r'(\d+) and (\d+)'
# matches_with_groups = re.findall(pattern_with_groups, text)
# print('Matches with groups:', matches_with_groups)
# 
# # Pattern without capturing groups
# pattern_without_groups = r'\d+'
# matches_without_groups = re.findall(pattern_without_groups, text)
# print('Matches without groups:', matches_without_groups)
# ```
# 
# Output:
# ```
# Matches with groups: [('123', '456')]
# Matches without groups: ['123', '456']
# ```
# 
# In this example, the input string contains two numbers. The first pattern `(\d+) and (\d+)` has two capturing groups, so `findall()` returns a list of string tuples with each tuple representing a match and each element in the tuple representing the captured group. The second pattern `\d+` has no capturing groups, so `findall()` returns a list of strings, with each string representing a complete match.
# 
# By including or excluding capturing groups in the regular expression pattern, you can control the format of the returned result from `findall()`.

# # 8. In standard expressions, what does the | character mean?
# 
# In standard regular expressions, the `|` character is known as the pipe or alternation operator. It is used to specify multiple alternative patterns to match.
# 
# The `|` character functions as a logical OR operator within the regular expression pattern. It allows you to define multiple patterns separated by `|`, and the regex engine will try to match any of the alternative patterns. If any of the patterns match, the overall match is considered successful.
# 
# Here's an example to demonstrate the usage of the `|` operator:
# 
# ```python
# import re
# 
# text = 'cat dog tiger lion'
# 
# # Pattern with alternation operator
# pattern = r'cat|dog'
# matches = re.findall(pattern, text)
# print(matches)
# ```
# 
# Output:
# ```
# ['cat', 'dog']
# ```
# 
# In this example, the pattern `cat|dog` is used with the `findall()` function to find matches in the input text. The `|` operator separates the two alternative patterns `cat` and `dog`. The regex engine tries to match either `cat` or `dog`, and in this case, it finds both matches in the input string.
# 
# The `|` operator can be used to specify more complex alternatives as well. For example, `pattern = r'red|green|blue'` would match any occurrence of 'red', 'green', or 'blue' in the input text.
# 
# Note that the alternation operator `|` has a lower precedence than other regular expression constructs like grouping `( )` or repetition `*`, `+`, `?`, so if you want to use alternation with other operators, you may need to use parentheses for proper grouping and precedence.

# # 9. In regular expressions, what does the character stand for?
# 
# In regular expressions, the character "." (dot) is called a "wildcard" and it represents any single character except for a newline character. It matches any character in the input string, regardless of what specific character it is. For example, the regular expression "c.t" would match "cat," "cot," "cut," and so on. The dot can be useful when you want to match any character in a specific position within a pattern, but you don't care about the exact value of that character.

# # 10.In regular expressions, what is the difference between the + and * characters?
# 
# In regular expressions, the "+" and "*" characters are known as quantifiers and are used to specify the number of occurrences of a preceding element in a pattern. The main difference between them is as follows:
# 
# 1. "+" (Plus): The plus symbol "+" specifies that the preceding element must occur one or more times, but not zero times. It requires at least one occurrence of the preceding element for a match. For example, the regular expression "ca+t" would match "cat," "caat," "caaat," and so on, but it would not match "ct" because the "+" requires at least one "a" after "c".
# 
# 2. "*" (Asterisk): The asterisk symbol "*" specifies that the preceding element can occur zero or more times. It allows for zero or more occurrences of the preceding element. For example, the regular expression "ca*t" would match "ct," "cat," "caat," "caaat," and so on because the "*" allows for zero or more "a" characters after "c".
# 
# To summarize, the "+" quantifier requires at least one occurrence of the preceding element, while the "*" quantifier allows for zero or more occurrences of the preceding element.

# # 11. What is the difference between {4} and {4,5} in regular expression?
# 
# In regular expressions, the curly braces "{ }" are used as quantifiers to specify the exact or minimum and maximum number of occurrences of a preceding element. The difference between "{4}" and "{4,5}" is as follows:
# 
# 1. "{4}": The curly braces with a single value inside, such as "{4}", specify the exact number of occurrences of the preceding element. It means the preceding element must occur exactly four times for a match. For example, the regular expression "a{4}" would match "aaaa" but not "aa" or "aaaaa".
# 
# 2. "{4,5}": The curly braces with two values separated by a comma, such as "{4,5}", specify a range of occurrences for the preceding element. It means the preceding element must occur at least four times and at most five times for a match. For example, the regular expression "a{4,5}" would match "aaaa" and "aaaaa" but not "aa" or "aaaaaa".
# 
# To summarize, "{4}" specifies an exact number of occurrences, while "{4,5}" specifies a range of minimum and maximum occurrences for the preceding element.

# # 12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?
# 
# In regular expressions, the shorthand character classes "\d", "\w", and "\s" have specific meanings:
# 
# 1. "\d": This shorthand character class represents any digit from 0 to 9. It is equivalent to the character range [0-9]. It is commonly used to match numeric digits in a string. For example, the regular expression "\d+" would match one or more consecutive digits in a string.
# 
# 2. "\w": This shorthand character class represents any alphanumeric character, including letters (both uppercase and lowercase) and digits. It is equivalent to the character range [a-zA-Z0-9_]. It can be used to match variable names, identifiers, or alphanumeric sequences. For example, the regular expression "\w+" would match one or more consecutive alphanumeric characters in a string.
# 
# 3. "\s": This shorthand character class represents any whitespace character, including spaces, tabs, and newline characters. It is equivalent to the character range [\t\n\f\r\p{Z}]. It can be used to match and handle whitespace in a string. For example, the regular expression "hello\sworld" would match "hello world" where the "\s" matches the space between "hello" and "world".
# 
# It's important to note that these shorthand character classes match single characters. If you want to match multiple occurrences of these character classes, you can use quantifiers like "+" or "*". For example, "\d+" would match one or more consecutive digits, and "\w*" would match zero or more alphanumeric characters.

# # 13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?
# 
# In regular expressions, the shorthand character classes "\D", "\W", and "\S" have meanings that are opposite to their counterparts (\d, \w, and \s):
# 
# 1. "\D": This shorthand character class represents any character that is not a digit. It matches any character that is not in the range [0-9]. For example, the regular expression "\D+" would match one or more consecutive non-digit characters in a string.
# 
# 2. "\W": This shorthand character class represents any character that is not a word character. It matches any character that is not in the range [a-zA-Z0-9_]. It can be used to match non-alphanumeric characters or symbols. For example, the regular expression "\W+" would match one or more consecutive non-word characters in a string.
# 
# 3. "\S": This shorthand character class represents any character that is not a whitespace character. It matches any character that is not in the range [\t\n\f\r\p{Z}]. It can be used to match non-whitespace characters in a string. For example, the regular expression "\S+" would match one or more consecutive non-whitespace characters in a string.
# 
# These shorthand character classes are useful when you want to match specific types of characters or exclude certain types of characters from a pattern.

# # 14. What is the difference between .*? and .*?
# 
# The difference between `.*?` and `.*` lies in their behavior in regular expressions, specifically in terms of greediness.
# 
# 1. `.*?`: The `.*?` pattern is a non-greedy or lazy quantifier. It matches zero or more occurrences of any character (except newline) in a non-greedy manner. It means it matches as few characters as possible to satisfy the overall pattern. This quantifier is often used when you want to capture the shortest possible substring that satisfies the pattern. For example, in the string "abcde", the regular expression "a.*?e" would match "abcde" rather than the entire string.
# 
# 2. `.*`: The `.*` pattern is a greedy quantifier. It matches zero or more occurrences of any character (except newline) in a greedy manner. It means it matches as many characters as possible to satisfy the overall pattern. This quantifier is often used when you want to capture the longest possible substring that satisfies the pattern. For example, in the string "abcde", the regular expression "a.*e" would match the entire string "abcde" because it greedily captures all characters between "a" and "e".
# 
# In summary, the `.*?` pattern matches as few characters as possible, while `.*` matches as many characters as possible. The addition of the question mark in `.*?` makes the quantifier non-greedy or lazy.

# # 15. What is the syntax for matching both numbers and lowercase letters with a character class?
# 
# To match both numbers and lowercase letters using a character class in regular expressions, you can use the following syntax:
# 
# ```regex
# [0-9a-z]
# ```
# 
# In this syntax, the character class `[ ]` allows you to define a set of characters to match. The range `0-9` matches any digit from 0 to 9, and `a-z` matches any lowercase letter from a to z. Combining them within the same character class `[0-9a-z]` will match any digit or lowercase letter.
# 
# Here are a few examples:
# 
# - The regular expression `[0-9a-z]+` would match one or more consecutive occurrences of any digit or lowercase letter.
# - The regular expression `[0-9a-z]{3}` would match exactly three characters, where each character can be a digit or a lowercase letter.
# - The regular expression `^[0-9a-z]+$` would match an entire string that consists only of digits and lowercase letters.
# 
# Note that the character class is case-sensitive by default, so `[0-9a-z]` matches lowercase letters only. If you want to match both uppercase and lowercase letters, you can use the case-insensitive flag (e.g., `/[0-9a-z]/i` in JavaScript or `re.compile('[0-9a-z]', re.IGNORECASE)` in Python).

# # 16. What is the procedure for making a normal expression in regax case insensitive?
# 
# To make a regular expression case insensitive, you can use the appropriate flag or option depending on the programming language or tool you are using. Here are some common methods for making a regular expression case insensitive in different contexts:
# 
# 1. Using Flags or Options:
#    - JavaScript: Add the `i` flag after the regular expression pattern. For example: `/pattern/i`.
#    - Python: Use the `re.IGNORECASE` flag as an argument to the `re.compile()` function or include the `re.I` flag directly in the regular expression pattern. For example: `re.compile("pattern", re.IGNORECASE)` or `re.compile("(?i)pattern")`.
#    - Java: Include the `Pattern.CASE_INSENSITIVE` flag as an argument to the `Pattern.compile()` method. For example: `Pattern.compile("pattern", Pattern.CASE_INSENSITIVE)`.
#    - .NET (C#): Use the `RegexOptions.IgnoreCase` option as the second argument to the `Regex.Match()` or `Regex.Replace()` methods. For example: `Regex.Match(input, pattern, RegexOptions.IgnoreCase)`.
# 
# 2. Using Inline Modifiers:
#    - Some regular expression flavors support inline modifiers within the pattern itself. For example, in Perl or PHP, you can include `(?i)` at the beginning of the pattern to make it case insensitive. For example: `/(?i)pattern/`.
# 
# By applying the appropriate flag, option, or inline modifier, you can make the regular expression match case-insensitively, allowing it to match both uppercase and lowercase characters without distinction.

# # 17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?
# 
# By default, the "." (dot) character in regular expressions matches any character except for a newline character ("\n"). It matches a single character from the input string, regardless of what specific character it is. For example, the regular expression "c.t" would match "cat," "cot," "cut," and so on.
# 
# However, if the `re.DOTALL` flag is passed as the second argument to `re.compile()` in Python, it changes the behavior of the dot character. When `re.DOTALL` is used, the dot matches any character, including newline characters. This flag essentially makes the dot match everything, including newlines.
# 
# Here's an example to illustrate the difference:
# 
# ```python
# import re
# 
# pattern = re.compile("a.b")
# text1 = "a\nb"
# text2 = "a b"
# 
# match1 = pattern.search(text1)
# match2 = pattern.search(text2, flags=re.DOTALL)
# 
# print(match1)  # None
# print(match2)  # <re.Match object; span=(0, 3), match='a\nb'>
# ```
# 
# In the example above, the pattern "a.b" is used to search for a sequence that starts with "a," followed by any character, and then ends with "b". When searching "a\nb" without the `re.DOTALL` flag, the newline character ("\n") causes the dot to fail to match. However, when the `re.DOTALL` flag is used, the dot matches the newline character as well, and the pattern produces a match.
# 
# Note that the `re.DOTALL` flag can also be represented by `re.S`.

# # 18. If numReg = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?
# 
# If `numReg = re.compile(r'\d+')`, and you apply `numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hens')`, it will return the following string:
# 
# `'X drummers, X pipers, five rings, X hens'`
# 
# Explanation:
# The regular expression pattern `\d+` matches one or more consecutive digits. In the given input string, there are three instances of consecutive digits: '11', '10', and '4'. The `sub()` method in the `re` module is used to substitute matches of the pattern with a specified replacement string, which in this case is 'X'.
# 
# Thus, the output of `numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hens')` will replace the matches of `\d+` with 'X', resulting in `'X drummers, X pipers, five rings, X hens'`.

# # 19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?
# 
# Passing `re.VERBOSE` as the second argument to `re.compile()` in Python allows you to write more readable and organized regular expressions by enabling verbose mode. When using verbose mode, you can include whitespace and comments within the regular expression pattern without affecting its functionality.
# 
# Here's how `re.VERBOSE` affects regular expressions:
# 
# 1. Ignoring Whitespace: In verbose mode, whitespace characters within the regular expression pattern are ignored. This allows you to add indentation, line breaks, and extra spaces to make the pattern more visually structured. It helps improve the readability and maintainability of complex regular expressions.
# 
# 2. Adding Comments: You can include comments within the regular expression pattern using the "#" symbol. Comments are useful for documenting and explaining the different parts of the pattern, making it easier to understand the logic behind it. Comments are ignored by the regular expression engine.
# 
# 3. Handling Line Endings: When using verbose mode, the `^` and `$` anchors in the pattern match the beginning and end of a line, respectively, in addition to matching the start and end of the entire input string.
# 
# Here's an example to illustrate the usage of `re.VERBOSE`:
# 
# ```python
# import re
# 
# pattern = re.compile(r"""
#     \d{3}      # Match three digits
#     [-\s]?     # Match a hyphen or space (optional)
#     \d{4}      # Match four digits
#     """, re.VERBOSE)
# 
# text = "Phone numbers: 123-4567, 456 7890, 9876543"
# 
# matches = pattern.findall(text)
# print(matches)
# ```
# 
# In the example above, the regular expression pattern matches phone numbers in the format "123-4567" or "456 7890" or "9876543". By using `re.VERBOSE`, the pattern is written in a more readable and organized manner, with comments explaining each part. The whitespace and comments are ignored, and the pattern functions as if they were not present.

# # 20. How would you write a regex that match a number with comma for every three digits? It must match the given following:
# #### '42'
# #### '1,234'
# #### '6,368,745'
# 
# #### but not the following:
# #### '12,34,567' (which has only two digits between the commas)
# #### '1234' (which lacks commas)
# To write a regular expression that matches a number with commas for every three digits, but excludes numbers with incorrect comma placement, you can use the following pattern:
# 
# ```regex
# ^\d{1,3}(,\d{3})*$
# ```
# 
# Explanation of the pattern:
# - `^` asserts the start of the string.
# - `\d{1,3}` matches one to three digits at the beginning.
# - `(,\d{3})*` matches zero or more occurrences of a comma followed by exactly three digits.
# - `$` asserts the end of the string.
# 
# This pattern ensures that the number starts with one to three digits and can have additional sets of three digits separated by commas.
# 
# Examples of matching strings:
# - `'42'`
# - `'1,234'`
# - `'6,368,745'`
# 
# Examples of non-matching strings:
# - `'12,34,567'` (incorrect comma placement)
# - `'1234'` (lacks commas)
# 
# You can use this pattern with the `re` module in Python or any other programming language/tool that supports regular expressions to match numbers with the desired format.

# # 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word thatbegins with a capital letter. 
# ### The regex must match the following:
# #### 'Haruto Watanabe'
# #### 'Alice Watanabe'
# #### 'RoboCop Watanabe'
# ###  but not the following:
# #### 'haruto Watanabe'(where the first name is not capitalized)
# #### 'Mr. Watanabe'(where the preceding word has a nonletter character)
# #### 'Watanabe'(which has no first name)
# #### 'Haruto watanabe'(where Watanabe is not capitalized)
# 
# To write a regular expression that matches the full name of someone whose last name is "Watanabe" while ensuring the first name is capitalized, you can use the following pattern:
# 
# ```regex
# ^[A-Z][a-zA-Z]*\sWatanabe$
# ```
# 
# Explanation of the pattern:
# - `^` asserts the start of the string.
# - `[A-Z]` matches an uppercase letter, ensuring the first letter of the first name is capitalized.
# - `[a-zA-Z]*` matches zero or more lowercase or uppercase letters, allowing for the possibility of multiple letters in the first name.
# - `\s` matches a whitespace character to separate the first and last name.
# - `Watanabe` matches the exact string "Watanabe".
# - `$` asserts the end of the string.
# 
# Examples of matching strings:
# - `'Haruto Watanabe'`
# - `'Alice Watanabe'`
# - `'RoboCop Watanabe'`
# 
# Examples of non-matching strings:
# - `'haruto Watanabe'` (first name is not capitalized)
# - `'Mr. Watanabe'` (preceding word has a non-letter character)
# - `'Watanabe'` (no first name)
# - `'Haruto watanabe'` (last name is not capitalized)
# 
# This pattern ensures that the first name is a single word starting with a capital letter, followed by a whitespace character, and then the last name "Watanabe".

# # 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob,or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs;and the sentence ends with a period? This regex should be case-insensitive. 
# ### It must match the following:
# #### 'Alice eats apples.'
# #### 'Bob pets cats.'
# #### 'Carol throws baseballs.'
# #### 'Alice throws Apples.'
# #### 'BOB EATS CATS.'
# ### but not the following:
# #### 'RoboCop eats apples.'
# #### 'ALICE THROWS FOOTBALLS.'
# ####  'Carol eats 7 cats.'
# 
# To write a case-insensitive regular expression that matches a sentence with specific word patterns, you can use the following pattern:
# 
# ```regex
# ^(Alice|Bob|Carol)\s+(eats|pets|throws)\s+(apples|cats|baseballs)\.$
# ```
# 
# Explanation of the pattern:
# - `^` asserts the start of the string.
# - `(Alice|Bob|Carol)` matches one of the given names in a case-insensitive manner.
# - `\s+` matches one or more whitespace characters to separate the words.
# - `(eats|pets|throws)` matches one of the given action words in a case-insensitive manner.
# - `(apples|cats|baseballs)` matches one of the given objects in a case-insensitive manner.
# - `\.` matches a period (.), escaping it since it has a special meaning in regular expressions.
# - `$` asserts the end of the string.
# 
# Examples of matching sentences:
# - `'Alice eats apples.'`
# - `'Bob pets cats.'`
# - `'Carol throws baseballs.'`
# - `'Alice throws Apples.'`
# - `'BOB EATS CATS.'`
# 
# Examples of non-matching sentences:
# - `'RoboCop eats apples.'` (name is not Alice, Bob, or Carol)
# - `'ALICE THROWS FOOTBALLS.'` (action or object word is not in the given options)
# - `'Carol eats 7 cats.'` (unexpected additional content in the sentence)
# 
# This pattern ensures that the sentence follows the specified structure and includes the provided words in a case-insensitive manner.

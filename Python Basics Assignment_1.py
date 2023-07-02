#!/usr/bin/env python
# coding: utf-8

# # 1. In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
*
'hello'
-87.8
-
/
+
6
Values:

'hello' (string value)
-87.8 (floating-point value)
6 (integer value)

Expressions:

* (multiplication operator)
- (subtraction operator)
/ (division operator)
+ (addition operator)
# # 2. What is the difference between string and variable?
# 
# A string and a variable are two different concepts in programming:
# 
# String:
# 
# - A string is a sequence of characters, such as letters, numbers, or symbols, enclosed within quotation marks (either single or double).
# - It represents textual data and is used to store and manipulate text in a program.
# Examples of strings: "Hello, world!", "12345"
# 
# Variable:
# 
# - A variable is a symbolic name or identifier that represents a value stored in the computer's memory.
# - It is used to store and manipulate data within a program.
# - Variables can hold various types of data, including strings, numbers, Boolean values, and more.
# - Variables provide a way to refer to and access data throughout a program by using the variable's name.
# - They can have different values assigned to them at different points in the program's execution.
# 
# Example of a variable: name = "John", where the variable name is assigned the string value "John".

# # 3. Describe three different data types.
# 
# 1 - Integer:
# 
# An integer data type represents whole numbers without any fractional or decimal part.
# It can be positive or negative, including zero.
# Examples: -5, 0, 10, 100.Floating-Point:
# 
# Floating-Point:
# 
# A floating-point data type, also known as a "float" or "double," represents numbers with fractional parts.
# It can represent both small and large numbers with decimal points.
# Examples: -3.14, 0.5, 2.71828, 1000.99.
#     
# String:
# 
# A string data type represents a sequence of characters.
# It is used to store and manipulate textual data.
# Strings are typically enclosed in quotation marks (single or double) to differentiate them from other data types.
# Examples: "Hello, World!","12345".

# # 4. What is an expression made up of? What do all expressions do?
# 
# An expression is a combination of values, variables, operators, and function calls that are evaluated to produce a result. It can be as simple as a single value or can involve complex calculations involving multiple values and operations.
# 
# Components of an expression:
# 
# 1 - Values: These are the basic building blocks of an expression and can include literals (e.g., numbers, strings) or variables (e.g., placeholders that hold values).
# 
# 2 - Operators: These are symbols or keywords that perform specific operations on values or variables. Common operators include arithmetic operators (+, -, *, /), comparison operators (==, <, >), logical operators (&&, ||), and more.
# 
# 3 - Function calls: Expressions can involve calling functions that perform specific tasks or computations and return a value. Functions can take arguments (input values) and produce a result based on those arguments.
# 
# What expressions do:
# 
# - Expressions are the fundamental units used to compute values or perform operations in programming.
# 
# - They are evaluated by the programming language's interpreter or compiler to produce a resulting value.
# 
# - The resulting value can be assigned to a variable, used in further calculations, or used in control flow statements to make decisions in a program.
# 

# # 5. This assignment statements, like spam = 10. What is the difference between an
# expression and a statement?
# 
# In programming, there is a distinction between expressions and statements:
# 
# Expression:
# 
# - An expression is a combination of values, variables, operators, and function calls that produces a value.
# - It can be evaluated to obtain a result.
# - Examples of expressions: 2 + 3, x * 5, "Hello" + "World", sqrt(16).
# 
# Statement:
# 
# - A statement is a complete instruction or action that performs a specific task in a program.
# - It usually does not produce a value but instead executes a sequence of operations or controls the flow of the program.
# - Examples of statements: variable assignment, conditional statements (if-else), loops (for, while), function declarations, and more.
# - Statements are typically terminated with a semicolon (;) in many programming languages.
# 
# The key difference between expressions and statements lies in their primary purpose:
# 
# - Expressions are used to compute values or produce results.
# - Statements are used to perform actions or control the flow of execution.
# 
# In the specific example you provided, "spam = 10" is an assignment statement. It assigns the value 10 to the variable "spam". It is not an expression because it does not produce a value. However, the right-hand side of the assignment, "10", is an expression because it represents a value.
# 
# 
# 
# 
# 

# # 6. After running the following code, what does the variable bacon contain?
# # bacon = 22
# The variable bacon will still contain the value 22.
# # bacon + 1
# In the second line bacon + 1, an expression bacon + 1 is evaluated, which adds 1 to the value of bacon. However, since the result is not assigned to any variable, it is not stored anywhere. Therefore, the original value of bacon remains unchanged at 22. If you want to update the value of bacon to the result of the expression, you need to assign it back to the variable, like this:
# 
# bacon = bacon + 1
# 
# Or using the shorthand notation:
# 
# bacon += 1
# 
# These statements would update the value of bacon to 23.

# # 7. What should the values of the following two terms be? 
# 'spam'+'spamspam'
# 'spam'*3
# 
# The values of the two terms would be as follows:
# 
# 1. 'spam' + 'spamspam':
#    - The `+` operator, when used with two strings, performs string concatenation, which means it combines the two strings into a single string.
#    - In this case, 'spam' + 'spamspam' would result in the string 'spamspamspam'.
# 
# 2. 'spam' * 3:
#    - The `*` operator, when used with a string and an integer, performs string repetition. It repeats the given string a specified number of times.
#    - In this case, 'spam' * 3 would result in the string 'spamspamspam', as the string 'spam' is repeated three times.
# 
# So, the values of the two terms are:
# - 'spam' + 'spamspam' = 'spamspamspam'
# - 'spam' * 3 = 'spamspamspam'

# # 8. Why is eggs a valid variable name while 100 is invalid?
# 
# In most programming languages, including Python, variable names must follow certain rules and conventions. Here's why 'eggs' is a valid variable name while '100' is invalid:
# 
# 1. Valid variable names:
# - Variable names can consist of letters (both lowercase and uppercase), digits (0-9), and underscores (_).
# - However, variable names cannot start with a digit.
# - They should be descriptive and follow a naming convention that makes the code more readable.
# - Examples of valid variable names: eggs, spam, my_variable, count_1, totalSum, etc.
# 
# 2. Invalid variable names:
# 
# - Variable names cannot start with a digit. They must begin with a letter or underscore.
# - Naming a variable starting with a digit may confuse the interpreter because it can be mistaken for a number or a different type of token.
# - Examples of invalid variable names: 100, 1stPlace, 3_14159, 99Bottles, etc.
# 
# #### In the specific case you mentioned, 'eggs' is a valid variable name because it starts with a letter and contains only letters. On the other hand, '100' is invalid because it starts with a digit. It's important to follow the naming rules of the programming language to ensure clarity, readability, and avoid syntax errors.

# # 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

# In[6]:


# Integer conversion: int()

#int() The int() function can be used to convert a value into an integer. It truncates any fractional part and returns the integer representation of the value.
#Example:

value = 10.5
integer_value = int(value)
print(integer_value)  # Output: 10


# In[7]:


#Floating-point conversion: float()

#The float() function can be used to convert a value into a floating-point number. It converts the value into a floating-point representation if it contains a fractional part.
# Example:

value = "3.14"
float_value = float(value)
print(float_value)  # Output: 3.14


# In[8]:


#String conversion: str()

#The str() function can be used to convert a value into a string. It returns the string representation of the value.
#Example:

value = 42
string_value = str(value)
print(string_value)  # Output: "42"


# # 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten'+ 99 +' burritos'
# 
# The expression 'I have eaten' + 99 + ' burritos' causes an error because it attempts to concatenate a string with an integer value directly. In many programming languages, including Python, concatenation is only allowed between strings or variables that represent strings.
# 
# To fix the error, you need to ensure that all the values being concatenated are converted to strings before performing the concatenation. 
# 
# Here's one way to fix it:
# 
# ### 'I have eaten ' + str(99) + ' burritos'
# 
# In this fixed expression, the integer value 99 is converted to a string using the str() function before concatenating it with the other strings. This ensures that all the operands are strings and can be concatenated correctly. The output will be 'I have eaten 99 burritos'.

#!/usr/bin/env python
# coding: utf-8

# # 1.What are the two values of the Boolean data type? How do you write them?
# 
# The Boolean data type represents a logical value and has two possible values: true and false. In most programming languages, these values are typically written as the keywords "true" and "false" respectively. These values are used to represent the truth or falsity of a condition or a logical expression.

# # 2. What are the three different types of Boolean operators?
# 
# The three different types of Boolean operators are:
# 
# 1. AND Operator: The AND operator returns true if both operands or conditions are true, and false otherwise. It is usually represented by the symbol "&&" or the keyword "AND". For example, in the expression "A && B", the result is true only if both A and B are true.
# 
# 
# 2. OR Operator: The OR operator returns true if at least one of the operands or conditions is true, and false if both operands are false. It is usually represented by the symbol "||" or the keyword "OR". For example, in the expression "A || B", the result is true if either A or B (or both) are true.
# 
# 
# 3. NOT Operator: The NOT operator, also known as the negation operator, is a unary operator that reverses the logical value of its operand. It returns true if the operand is false, and false if the operand is true. It is usually represented by the exclamation mark "!" or the keyword "NOT". For example, in the expression "!A", the result is true if A is false, and false if A is true.
# 
# These Boolean operators are commonly used in programming and logic to manipulate and evaluate logical expressions and conditions.

# # 3. Make a list of each Boolean operators truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# 
# Apologies for the confusion. Here are the correct truth tables for each Boolean operator:
# 
# 1. AND Operator (&&):
# 
# | Operand A | Operand B | Result |
# |-----------|-----------|--------|
# |   false   |   false   | false  |
# |   false   |   true    | false  |
# |   true    |   false   | false  |
# |   true    |   true    | true   |
# 
# 
# 2. OR Operator (||):
# 
# | Operand A | Operand B | Result |
# |-----------|-----------|--------|
# |   false   |   false   | false  |
# |   false   |   true    | true   |
# |   true    |   false   | true   |
# |   true    |   true    | true   |
# 
# 
# 3. NOT Operator (!):
# 
# | Operand | Result |
# |---------|--------|
# |  false  |  true  |
# |  true   | false  |
# 
# In the truth tables above, the operands A and B can take the values of either true or false, and the operators evaluate the logical combinations of these values to produce the resulting Boolean value.

# # 4. What are the values of the following expressions?
# (5 &gt; 4) and (3 == 5)
# not (5 &gt; 4)
# (5 &gt; 4) or (3 == 5)
# not ((5 &gt; 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)
# 
# Let's evaluate the given expressions:
# 
# 1. (5 > 4) and (3 == 5)
#    - (5 > 4) is true
#    - (3 == 5) is false
#    - true and false is false
# 
# 2. not (5 > 4)
#    - (5 > 4) is true
#    - not true is false
# 
# 3. (5 > 4) or (3 == 5)
#    - (5 > 4) is true
#    - (3 == 5) is false
#    - true or false is true
# 
# 4. not ((5 > 4) or (3 == 5))
#    - (5 > 4) is true
#    - (3 == 5) is false
#    - true or false is true
#    - not true is false
# 
# 5. (True and True) and (True == False)
#    - True and True is true
#    - True == False is false
#    - true and false is false
# 
# 6. (not False) or (not True)
#    - not False is true
#    - not True is false
#    - true or false is true
# 
# Therefore, the values of the given expressions are:
# 
# 1. False
# 2. False
# 3. True
# 4. False
# 5. False
# 6. True

# # 5. What are the six comparison operators?
# 
# The six comparison operators are:
# 
# 1. Equal to (==): This operator checks if two values are equal and returns true if they are, and false otherwise.
# 
# 2. Not equal to (!=): This operator checks if two values are not equal and returns true if they are not, and false if they are equal.
# 
# 3. Greater than (>): This operator checks if the left operand is greater than the right operand and returns true if it is, and false otherwise.
# 
# 4. Less than (<): This operator checks if the left operand is less than the right operand and returns true if it is, and false otherwise.
# 
# 5. Greater than or equal to (>=): This operator checks if the left operand is greater than or equal to the right operand and returns true if it is, and false otherwise.
# 
# 6. Less than or equal to (<=): This operator checks if the left operand is less than or equal to the right operand and returns true if it is, and false otherwise.
# 
# These comparison operators are commonly used to compare values in programming and logical expressions to determine relationships or conditions.

# # 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

# In[1]:


x = 5  # Assignment operator - assigns the value 5 to the variable x

if x == 5:  # Equal to operator - checks if the value of x is equal to 5
    print("x is equal to 5")
else:
    print("x is not equal to 5")


# # 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam &gt; 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')

# In[3]:


spam = 0
# Block 1:
if spam == 10:
    print('eggs') #This block is an if statement that checks if the variable spam is equal to 10. If the condition is true, it will execute the print('eggs') statement.
    
# Block 2:

if spam > 5:
    print('bacon') #This block is another if statement that checks if the variable spam is greater than 5. If the condition is true, it will execute the print('bacon') statement.

# Block 3:

else:
    print('ham') #This block contains an else statement. If the condition in Block 2 (spam > 5) is false, it will execute the print('ham') statement. Additionally, it will always execute the following three statements: print('spam'), print('spam'). These statements are not indented, so they are outside the if-else structure and will always be executed.
print('spam')
print('spam') 


# # 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints,Greetings! if anything else is stored in spam. 

# In[23]:


spam = int(input("Enter Number Between 1 to 10: "))  # Replace this with the value you want to store in spam

if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# # 9.If your programme is stuck in an endless loop, what keys you’ll press?
# 
# If your program is stuck in an endless loop and you want to interrupt its execution, you can typically press the following key combination depending on the operating system and the development environment:
# 
# 1. **Ctrl + C** (Windows/Linux): This key combination sends an interrupt signal to the running program, causing it to terminate. It is a commonly used keyboard shortcut to break out of an infinite loop or stop the execution of a program.
# 
# Please note that while these key combinations are commonly used to terminate a program, the effectiveness may vary depending on the specific environment and the nature of the program itself. In some cases, you might need to use different key combinations or methods to terminate a program that is stuck in an endless loop.

# # 10. How can you tell the difference between break and continue?
# 
# The "break" and "continue" statements are used in loops to control the flow of execution. Here's how you can tell the difference between them:
# 
# 1. "break" statement:
#    - When encountered in a loop, the "break" statement immediately terminates the loop and resumes execution at the next statement after the loop.
#    - It is used to completely exit out of the loop, regardless of any remaining iterations.
#    - After the "break" statement is executed, the loop condition is no longer checked, and the program continues executing from the point immediately after the loop.
#    - Typically, "break" is used when you want to prematurely exit a loop based on a certain condition.
# 
# 2. "continue" statement:
#    - When encountered in a loop, the "continue" statement skips the remaining code within the loop for the current iteration and moves to the next iteration.
#    - It is used to skip specific iterations of the loop based on a certain condition, without completely exiting the loop.
#    - After the "continue" statement is executed, the loop condition is re-evaluated, and the next iteration starts if the condition is still true.
#    - Typically, "continue" is used when you want to skip some part of the loop's code for certain iterations and continue with the next iteration.

# In[24]:


# Here's an example to illustrate the difference:

# Example using break statement
for num in range(1, 6):
    if num == 4:
        break
    print(num)

# Output: 1 2 3

# Example using continue statement
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# Output: 1 2 4 5


# In the first example, the "break" statement is encountered when num is equal to 4. The loop is immediately terminated, and only the numbers 1, 2, and 3 are printed.
# 
# In the second example, the "continue" statement is encountered when num is equal to 3. The remaining code for that iteration is skipped, and the loop continues to the next iteration. Therefore, the number 3 is not printed, but the loop continues to print the numbers 1, 2, 4, and 5.

# #  11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
# In a for loop, the expressions range(10), range(0, 10), and range(0, 10, 1) all represent different ways to generate a sequence of numbers. However, they have slight differences in terms of their arguments. Let's break it down:
# 
# 1. range(10): This expression generates a sequence of numbers starting from 0 (inclusive) up to, but not including, 10. It is equivalent to range(0, 10, 1), where the step argument is implicitly set to 1. The default step value for range() is 1 if not specified.

# In[25]:


#Example
for i in range(10):
    print(i)


# range(0, 10): This expression generates a sequence of numbers starting from the specified start value (0 in this case) up to, but not including, the specified end value (10 in this case). The step value is not explicitly mentioned, so it defaults to 1.

# In[26]:


#Example
for i in range(0, 10):
    print(i)


# range(0, 10, 1): This expression generates a sequence of numbers starting from the specified start value (0 in this case) up to, but not including, the specified end value (10 in this case), incrementing by the specified step value (1 in this case). The step value determines the difference between each consecutive number in the sequence.

# In[27]:


#Example
for i in range(0, 10, 1):
    print(i)


# # 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[28]:


# Using a for loop
for num in range(1, 11):
    print(num)


# In[29]:


# Using a while loop
num = 1
while num <= 10:
    print(num)
    num += 1


# # 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# After importing the module spam, you can call the function bacon() using the module name as a prefix followed by the function name. Here's how you would do it:
# 
# import spam
# 
# spam.bacon()
# 
# In this code, spam is the module name, and bacon() is the function name. By using the dot notation spam.bacon(), you are specifying that you want to call the function bacon() which is defined inside the spam module.

# 

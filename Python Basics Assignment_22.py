#!/usr/bin/env python
# coding: utf-8

# ### 1. What is the result of the code, and explain?
# 
# #### >>>X = 'iNeuron'
# #### >>>def func():
# #### print(X)
# 
# #### >>>func()
# 
# The code provided will result in a `NameError` because the code block within the `func()` function is not indented properly.
# 
# ```python
# X = 'iNeuron'
# 
# def func():
#     print(X)
# 
# func()
# ```
# 
# Explanation:
# - The variable `X` is assigned the string value `'iNeuron'`.
# - The function `func()` is defined.
# - Within the `func()` function, the `print()` statement is used to print the value of the variable `X`.
# - Finally, the function `func()` is called, which will print the value of `X`, resulting in the output: `iNeuron`.

# ### 2. What is the result of the code, and explain?
# 
# #### X = 'iNeuron'
# #### def func():
# #### X = 'NI!'
# 
# #### func()
# #### print(X)
# 
# The code will result in the output `'iNeuron'`.
# 
# Explanation:
# - The variable `X` is assigned the string value `'iNeuron'`.
# - The function `func()` is defined.
# - Within the `func()` function, a new local variable `X` is assigned the string value `'NI!'`. This local variable `X` is different from the global variable `X` defined outside the function.
# - The `func()` function is called, but it does not print anything.
# - After the function call, the `print(X)` statement outside the function is executed. It refers to the global variable `X`, which has not been modified by the `func()` function. Therefore, it prints `'iNeuron'`.
# - Hence, the final output is `'iNeuron'`.

# ### 3. What does this code print, and why?
# 
# #### X = 'iNeuron'
# #### def func():
# #### X = 'NI'
# #### print(X)
# 
# #### func()
# #### print(X)
# 
# The code will print:
# ```
# NI
# iNeuron
# ```
# 
# Explanation:
# - The variable `X` is initially assigned the value `'iNeuron'`.
# - The function `func()` is defined, and within the function, a new local variable `X` is assigned the value `'NI'`. This creates a separate local variable `X` within the function's scope, which does not affect the global variable `X`.
# - Inside the function `func()`, the `print(X)` statement is executed, which prints the value of the local variable `X`, resulting in the output: `NI`.
# - After calling the function, when `print(X)` is executed outside the function, it refers to the global variable `X`, which retains its original value `'iNeuron'`. Thus, it prints `'iNeuron'` as the output.

# # 4. What output does this code produce? Why?
# 
# X = 'iNeuron'
# def func():
# global X
# X = 'NI'
# 
# func()
# print(X)
# 
# The output of the code will be:
# ```
# NI
# ```
# 
# Explanation:
# - The variable `X` is initially assigned the value `'iNeuron'`.
# - The function `func()` is defined, and within the function, the `global` keyword is used to declare that the variable `X` refers to the global variable `X`, not a local variable.
# - Inside the function, the value of the global variable `X` is changed to `'NI'` by the assignment statement `X = 'NI'`.
# - When the function `func()` is called, it modifies the global variable `X`.
# - After calling the function, when `print(X)` is executed, it refers to the modified global variable `X`, which now has the value `'NI'`. Thus, it prints `'NI'` as the output.

# #### 5. What about this code—what’s the output, and why? X = 'iNeuron'
# def func():
# X = 'NI'
# def nested():
# print(X)
# nested()
# 
# func()
# X
# 
# The output of the code will be:
# ```
# iNeuron
# ```
# 
# Explanation:
# - The variable `X` is initially assigned the value `'iNeuron'`.
# - The function `func()` is defined, and within the function, a new local variable `X` is assigned the value `'NI'`. This creates a separate local variable `X` within the function's scope.
# - Inside the `func()` function, another nested function `nested()` is defined.
# - Inside the `nested()` function, the `print(X)` statement is executed. However, since the local variable `X` is not defined within the `nested()` function, Python looks for the variable `X` in the next enclosing scope, which is the `func()` function. It finds the local variable `X` with the value `'NI'` in the `func()` function's scope and uses that value.
# - When the `func()` function is called, the `nested()` function is also called within it.
# - Inside the `nested()` function, `print(X)` prints the value of the local variable `X` in the `func()` function, which is `'NI'`.
# - After the function calls, when `print(X)` is executed outside the `func()` function, it refers to the global variable `X` with the value `'iNeuron'`. Thus, it prints `'iNeuron'` as the output.

# # 6. How about this code: what is its output in Python 3, and explain?
# 
# def func():
# X = 'NI'
# def nested():
# nonlocal X
# X = 'Spam'
# nested()
# print(X)
# 
# func()
# 
# In Python 3, the code will produce the following output:
# 
# ```
# Spam
# ```
# 
# Explanation:
# - The `func()` function is defined.
# - Inside the `func()` function, a local variable `X` is assigned the value `'NI'`.
# - Another nested function `nested()` is defined within the `func()` function.
# - Inside the `nested()` function, the `nonlocal` keyword is used to indicate that the variable `X` refers to the nearest enclosing scope where `X` is defined, which is the `func()` function in this case.
# - Inside the `nested()` function, the value of `X` is updated to `'Spam'`.
# - The `nested()` function is called within the `func()` function.
# - After the execution of `nested()`, the `print(X)` statement is executed within the `func()` function.
# - Since the value of `X` was updated to `'Spam'` within the `nested()` function using the `nonlocal` keyword, the `print(X)` statement will output `'Spam'`.
# 
# Note: The `nonlocal` keyword is used to indicate that a variable in an inner nested function refers to the nearest enclosing scope where the variable is defined, allowing modifications to that variable within the nested function.

#!/usr/bin/env python
# coding: utf-8

# # 1. Create an assert statement that throws an AssertionError if the variable spam is a negative integer.
# 
# Certainly! Here's an example of an assert statement that throws an `AssertionError` if the variable `spam` is a negative integer in Python:
# 
# ```python
# assert spam >= 0, "spam should not be a negative integer"
# ```
# 
# If the value of `spam` is a negative integer, this statement will raise an `AssertionError` with the specified error message: "spam should not be a negative integer".

# # 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
# 
# To trigger an `AssertionError` if the variables `eggs` and `bacon` contain strings that are the same, disregarding their cases, you can use the `lower()` method to convert the strings to lowercase and then compare them. Here's an example of an assert statement that achieves this:
# 
# ```python
# assert eggs.lower() != bacon.lower(), "eggs and bacon should not have the same value"
# ```
# 
# If the values of `eggs` and `bacon` are the same when converted to lowercase, this statement will raise an `AssertionError` with the specified error message: "eggs and bacon should not have the same value".

# # 3. Create an assert statement that throws an AssertionError every time.
# 
# If you want to create an assert statement that throws an `AssertionError` every time, you can simply use the `assert` statement with a condition that always evaluates to `False`. Here's an example:
# 
# ```python
# assert False, "This assert statement always throws an AssertionError"
# ```
# 
# In this case, the condition `False` is always false, so the `assert` statement will raise an `AssertionError` with the specified error message: "This assert statement always throws an AssertionError".

# # 4. What are the two lines that must be present in your software in order to call logging.debug()?
# 
# In order to call `logging.debug()` in your software, you need to include the following two lines:
# 
# ```python
# import logging
# logging.basicConfig(level=logging.DEBUG)
# ```
# 
# The first line imports the logging module, which provides the logging functionality in Python. The second line sets up the basic configuration for logging, specifically setting the logging level to `DEBUG`. This configuration allows you to use `logging.debug()` and log messages at the debug level.
# 
# Please note that this basic configuration may need to be adjusted further depending on your specific logging needs, such as specifying a file to write logs to or formatting options.

# # 5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
# 
# To have `logging.debug()` send a logging message to a file named "programLog.txt," you need to include the following two lines in your program:
# 
# ```python
# import logging
# 
# logging.basicConfig(filename='programLog.txt', level=logging.DEBUG)
# ```
# 
# The first line imports the logging module, which provides the logging functionality in Python. The second line sets up the basic configuration for logging, where the `filename` parameter specifies the name of the file to which the logs will be written (`programLog.txt` in this case), and the `level` parameter is set to `logging.DEBUG` to allow debug-level log messages to be recorded.
# 
# With these two lines included, you can use `logging.debug()` to send logging messages, and they will be written to the specified file "programLog.txt".

# # 6. What are the five levels of logging?
# 
# In the logging module of Python, there are five levels of logging, listed below in ascending order of severity:
# 
# 1. `DEBUG`: Detailed information for diagnostic purposes, typically useful during development and debugging stages.
# 2. `INFO`: General information about the progress of the application. It confirms that things are working as expected.
# 3. `WARNING`: Indicates potential issues or unexpected situations that may cause problems but are not necessarily critical.
# 4. `ERROR`: Indicates errors that caused a particular function or operation to fail, but the application can still continue running.
# 5. `CRITICAL`: Indicates critical errors that may prevent the application from functioning correctly or lead to its termination.
# 
# These levels allow you to categorize and prioritize the importance of different log messages based on their severity.

# # 7. What line of code would you add to your software to disable all logging messages?
# 
# To disable all logging messages in your software, you can add the following line of code:
# 
# ```python
# logging.disable(logging.CRITICAL)
# ```
# 
# This line of code uses the `disable()` function provided by the logging module to disable all logging messages with a level of `CRITICAL` or lower. Since `CRITICAL` is the highest severity level, disabling it effectively disables logging of all levels.

# # 8.Why is using logging messages better than using print() to display the same message?
# 
# Using logging messages is generally considered better than using `print()` to display messages for several reasons:
# 
# 1. **Logging Levels and Granularity**: Logging provides different levels of granularity (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL) to categorize and prioritize messages based on their severity. This allows you to control which messages are displayed based on the desired level of detail. With `print()`, you don't have built-in levels, so all messages are displayed regardless of their importance.
# 
# 2. **Flexibility and Configurability**: Logging offers more flexibility and configurability compared to `print()`. You can configure logging to write messages to different outputs (such as a file, console, or network) and define custom formatting. It allows you to control the output destination, format, and level of verbosity without modifying the code. With `print()`, you have limited control over where the messages go and how they are formatted.
# 
# 3. **Runtime Control**: Logging messages can be dynamically enabled or disabled at runtime without modifying the code. This is especially useful when troubleshooting or deploying applications in different environments. On the other hand, removing `print()` statements requires modifying the code, which can be cumbersome and error-prone.
# 
# 4. **Integration with Libraries and Frameworks**: Many libraries and frameworks are built to work seamlessly with the logging module. They often provide hooks to capture and handle log messages generated by their internal components. By using logging, you can leverage these integrations and benefit from consistent and unified logging across different parts of your software.
# 
# 5. **Production Readiness**: Logging is designed to be production-ready, with features like log rotation, log levels, and easy integration with existing logging infrastructure. It provides a standardized and scalable approach to capturing and managing application logs in production environments. `print()`, on the other hand, is primarily intended for debugging purposes and lacks these production-ready features.
# 
# Overall, using logging messages instead of `print()` provides greater flexibility, configurability, and control over logging output, making it a more powerful and suitable choice for professional software development.

# # 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
# 
# The Step Over, Step In, and Step Out buttons are commonly found in debuggers and are used to control the execution flow during debugging. Here are the differences between these buttons:
# 
# 1. **Step Over**: When you click the Step Over button or use the corresponding keyboard shortcut (often F10), the debugger executes the current line of code and moves to the next line. If the line contains a function call, the debugger will not enter the function and will treat it as a single step, allowing you to skip over the function's internal details and proceed to the next line in the current scope.
# 
# 2. **Step In**: Clicking the Step In button or using the relevant keyboard shortcut (often F11) causes the debugger to execute the current line of code. If the line contains a function call, the debugger will enter the called function, allowing you to debug through its internal implementation. This enables you to analyze the behavior and variables within the called function.
# 
# 3. **Step Out**: The Step Out button or its corresponding keyboard shortcut (often Shift+F11) is used when you are already debugging inside a function and want to quickly execute the remaining lines of code in that function without stepping through each line. The debugger will continue execution until it exits the current function and returns to the caller, allowing you to skip the remaining lines of code within the function.
# 
# To summarize:
# - Step Over executes the current line and moves to the next line, skipping over function calls.
# - Step In executes the current line and enters any called functions for detailed debugging within the function.
# - Step Out executes the remaining lines in the current function and returns to the caller.
# 
# These debugging controls help you navigate through code during the debugging process, allowing you to trace the execution and identify issues in your program.

# # 10.After you click Continue, when will the debugger stop ?
# 
# After clicking the "Continue" button in a debugger, the debugger will continue running the program without interruption until one of the following conditions is met:
# 
# 1. **Breakpoint**: If there is a breakpoint set at a particular line in the code, the debugger will stop when it reaches that line. Breakpoints allow you to pause the program execution at specific points to inspect variables, step through the code, or analyze the program's state.
# 
# 2. **Exception**: If an exception occurs during the program's execution and it is not caught within the code, the debugger will pause and highlight the line where the exception was raised. This allows you to examine the state of the program at the point of the exception and identify the cause of the error.
# 
# 3. **Program Completion**: The debugger will stop when the program execution is complete, meaning it reaches the end of the main script or the designated exit point.
# 
# By clicking "Continue," you essentially instruct the debugger to resume normal execution and let the program run until it encounters one of the above conditions that trigger a pause or termination.

# # 11. What is the concept of a breakpoint?
# 
# The concept of a breakpoint is a feature provided by debuggers to pause the execution of a program at a specific line or condition during debugging. A breakpoint allows you to examine the program's state, inspect variables, and step through the code to understand its behavior.
# 
# When a breakpoint is set at a particular line in the code, the debugger monitors the program's execution and stops when it reaches that line. This allows you to analyze the program's state at that point, inspect variable values, and step through the code line by line to understand how the program is behaving.
# 
# Breakpoints are useful for various debugging scenarios, including:
# 
# 1. **Spotting Errors**: By setting breakpoints at critical points in the code, you can examine the state of variables and data structures to identify errors or unexpected behavior.
# 
# 2. **Analyzing Program Flow**: Breakpoints enable you to step through the code line by line, allowing you to understand the flow of execution, track variable changes, and verify if the program is following the expected logic.
# 
# 3. **Inspecting Variables**: When the program pauses at a breakpoint, you can inspect the values of variables, check if they match the expected values, and identify any anomalies.
# 
# 4. **Identifying Performance Issues**: Breakpoints can be used to measure the time taken by a specific section of code, helping to identify performance bottlenecks.
# 
# Breakpoints can typically be set using integrated development environments (IDEs) or command-line debuggers. Once set, they allow you to gain valuable insights into the program's execution and assist in troubleshooting and resolving issues.

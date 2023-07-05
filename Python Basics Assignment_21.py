#!/usr/bin/env python
# coding: utf-8

# ### 1. Add the current date to the text file today.txt as a string.
# 
# ```python
# from datetime import date
# 
# # Get the current date
# current_date = date.today()
# 
# # Open the file in append mode and write the current date
# with open('today.txt', 'a') as file:
#     file.write(str(current_date))
# ```
# 
# In this code, we first import the `date` class from the `datetime` module to get the current date.
# 
# Then, we use the `date.today()` method to obtain the current date.
# 
# Next, we open the file `today.txt` in append mode using the `open()` function with the mode parameter set to `'a'`. This ensures that any existing content in the file is preserved, and new content will be appended to the end of the file.
# 
# Finally, we write the string representation of the current date to the file using the `write()` method.
# 
# After running this code, the current date will be added as a string to the `today.txt` file.

# ### 2. Read the text file today.txt into the string today_string
# 
# ```python
# with open('today.txt', 'r') as file:
#     today_string = file.read()
# 
# print(today_string)
# ```
# 
# In this code, we open the file `today.txt` in read mode using the `open()` function with the mode parameter set to `'r'`. This allows us to read the contents of the file.
# 
# Then, we use the `read()` method to read the entire content of the file into the `today_string` variable.
# 
# Finally, we print the value of `today_string` to verify that the file content has been successfully read into the string.
# 
# After running this code, the contents of the `today.txt` file will be stored in the `today_string` variable, and it will be printed to the console.

# ### 3. Parse the date from today_string.
# 
# ```python
# from datetime import datetime
# 
# date_format = "%Y-%m-%d"
# 
# parsed_date = datetime.strptime(today_string.strip(), date_format).date()
# 
# print(parsed_date)
# ```
# 
# In this code, we import the `datetime` module to work with dates and times.
# 
# We define the expected date format as "%Y-%m-%d", where "%Y" represents the year, "%m" represents the month, and "%d" represents the day.
# 
# Then, we use the `strptime()` method of the `datetime` class to parse the date from the `today_string`. We strip any leading or trailing whitespace from the string using the `strip()` method.
# 
# Finally, we access the `date()` method of the parsed datetime object to extract the date part, and we print it.
# 
# After running this code, you will see the parsed date printed to the console.

# ### 4. List the files in your current directory
# 
# ```python
# import os
# 
# # Get the current directory
# current_directory = os.getcwd()
# 
# # List all files in the current directory
# files = os.listdir(current_directory)
# 
# # Print the file names
# for file in files:
#     print(file)
# ```
# 
# In this code, we first import the `os` module, which provides functions for interacting with the operating system.
# 
# Then, we use the `os.getcwd()` function to get the current directory. This function returns a string representing the current working directory.
# 
# Next, we use the `os.listdir()` function to obtain a list of all files and directories in the current directory.
# 
# Finally, we iterate over the files in the list and print their names using a `for` loop.
# 
# When you run this code, it will display the names of all the files in your current directory.

# ### 5. Create a list of all of the files in your parent directory (minimum five files should be available).
# 
# To create a list of all the files in your parent directory, you can use the `os` module along with the `os.listdir()` function. Here's an example code snippet:
# 
# ```python
# import os
# 
# # Get the parent directory
# parent_directory = os.path.dirname(os.getcwd())
# 
# # List all files in the parent directory
# files = os.listdir(parent_directory)
# 
# # Print the file names
# for file in files:
#     print(file)
# ```
# 
# In this code, we first import the `os` module.
# 
# Then, we use the `os.getcwd()` function to get the current directory and `os.path.dirname()` function to obtain its parent directory.
# 
# Next, we use the `os.listdir()` function to get a list of all files and directories in the parent directory.
# 
# Finally, we iterate over the files in the list and print their names using a `for` loop.
# 
# When you run this code, it will display the names of all the files in your parent directory.

# ### 6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.
# 
# Here's an example code snippet that uses the `multiprocessing` module to create three separate processes. Each process will wait for a random number of seconds between one and five, print the current time, and then exit:
# 
# ```python
# import multiprocessing
# import random
# import time
# from datetime import datetime
# 
# def process_function():
#     wait_time = random.randint(1, 5)
#     time.sleep(wait_time)
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"Process {multiprocessing.current_process().name}: Current time is {current_time}")
# 
# if __name__ == "__main__":
#     processes = []
# 
#     for i in range(3):
#         process = multiprocessing.Process(target=process_function)
#         process.start()
#         processes.append(process)
# 
#     for process in processes:
#         process.join()
# ```
# 
# In this code, we first import the necessary modules: `multiprocessing` for creating processes, `random` for generating random wait times, `time` for using the `sleep()` function, and `datetime` for getting the current time.
# 
# Then, we define a function `process_function()` that represents the task to be executed by each process. Inside this function, we generate a random wait time between one and five seconds using `random.randint()`, sleep for that duration using `time.sleep()`, and then get the current time using `datetime.now().strftime()`.
# 
# In the main block, we create three separate processes by iterating from 0 to 2. For each iteration, we create a process using `multiprocessing.Process()`, passing the `process_function` as the target. We start each process using `process.start()` and store them in the `processes` list.
# 
# Finally, we use a `for` loop to join (wait for) each process to complete using `process.join()`.
# 
# When you run this code, you will see the three processes executing concurrently. Each process will wait for a random number of seconds, print the current time, and then exit. The order of execution may vary for each run.

# ### 7. Create a date object of your day of birth.
# 
# To create a `date` object representing your day of birth, you can use the `datetime` module. Here's an example code snippet:
# 
# ```python
# from datetime import date
# 
# # Specify your day of birth
# birth_year = 2000
# birth_month = 6
# birth_day = 15
# 
# # Create a date object
# birth_date = date(birth_year, birth_month, birth_day)
# 
# print(birth_date)
# ```
# 
# In this code, we import the `date` class from the `datetime` module.
# 
# Then, we specify the year, month, and day of your birth as `birth_year`, `birth_month`, and `birth_day`, respectively.
# 
# Next, we create a `date` object named `birth_date` by calling the `date()` constructor and passing in the birth year, month, and day as arguments.
# 
# Finally, we print the `birth_date` object, which will display the date in the format `YYYY-MM-DD`.
# 
# You can modify the values of `birth_year`, `birth_month`, and `birth_day` to match your own day of birth.

# ### 8. What day of the week was your day of birth?
# 
# To determine the day of the week for your day of birth, you can use the `weekday()` method of the `date` object. The `weekday()` method returns an integer where Monday is 0 and Sunday is 6.
# 
# ```python
# from datetime import date
# 
# # Specify your day of birth
# birth_year = 2000
# birth_month = 6
# birth_day = 15
# 
# # Create a date object
# birth_date = date(birth_year, birth_month, birth_day)
# 
# # Get the day of the week
# day_of_week = birth_date.weekday()
# 
# # Define a list of weekdays
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# 
# # Print the day of the week
# print(weekdays[day_of_week])
# ```
# 
# In this code, we first create a `date` object representing your day of birth using the specified year, month, and day.
# 
# Then, we use the `weekday()` method on the `birth_date` object to obtain the day of the week as an integer.
# 
# Next, we define a list `weekdays` containing the names of the days of the week in the appropriate order.
# 
# Finally, we print the day of the week by indexing into the `weekdays` list using the `day_of_week` integer.
# 
# You can modify the values of `birth_year`, `birth_month`, and `birth_day` to match your own day of birth.

# ### 9. When will you be (or when were you) 10,000 days old?
# 
# To calculate the date when you will be or when you were 10,000 days old, you can use the `timedelta` class from the `datetime` module. 
# 
# ```python
# from datetime import date, timedelta
# 
# # Specify your day of birth
# birth_year = 2000
# birth_month = 6
# birth_day = 15
# 
# # Create a date object for your birthday
# birth_date = date(birth_year, birth_month, birth_day)
# 
# # Calculate the timedelta for 10,000 days
# ten_thousand_days = timedelta(days=10000)
# 
# # Calculate the date when you will be or were 10,000 days old
# result_date = birth_date + ten_thousand_days
# 
# # Print the result
# print(result_date)
# ```
# 
# In this code, we first create a `date` object representing your day of birth using the specified year, month, and day.
# 
# Then, we create a `timedelta` object named `ten_thousand_days` with a value of 10,000 days.
# 
# Next, we calculate the result date by adding the `ten_thousand_days` timedelta to your birth date using the `+` operator.
# 
# Finally, we print the result date, which will be the date when you will be or were 10,000 days old.
# 
# You can modify the values of `birth_year`, `birth_month`, and `birth_day` to match your own day of birth.

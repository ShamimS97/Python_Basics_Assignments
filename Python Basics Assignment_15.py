#!/usr/bin/env python
# coding: utf-8

# # 1.How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).
# 
# To calculate the number of seconds in an hour, you can use the interactive Python interpreter as a calculator. Simply multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60). Here's an example:
# 
# ```python
# seconds_in_minute = 60
# minutes_in_hour = 60
# 
# seconds_in_hour = seconds_in_minute * minutes_in_hour
# 
# print(seconds_in_hour)
# ```
# 
# When you run the code, it will output:
# 
# ```
# 3600
# ```
# 
# Therefore, there are 3600 seconds in an hour.

# # 2. Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.
# 
# To assign the result of the previous task, which is the number of seconds in an hour (3600), to a variable called `seconds_per_hour`, you can use the assignment operator (`=`). Here's an example:
# 
# ```python
# seconds_per_hour = 3600
# 
# print(seconds_per_hour)
# ```
# 
# When you run the code, it will output:
# 
# ```
# 3600
# ```
# 
# Now, the value 3600 is stored in the variable `seconds_per_hour`, and you can use this variable in your code for further calculations or operations related to seconds in an hour.

# # 3. How many seconds do you think there are in a day? Make use of the variables seconds per hour and minutes per hour.
# 
# To calculate the number of seconds in a day, you can use the variables `seconds_per_hour` and `minutes_per_hour` that were previously defined. Since there are 24 hours in a day, you can multiply the number of seconds in an hour by the number of hours in a day (24). Here's an example:
# 
# ```python
# seconds_per_hour = 3600
# minutes_per_hour = 60
# 
# hours_per_day = 24
# 
# seconds_per_day = seconds_per_hour * minutes_per_hour * hours_per_day
# 
# print(seconds_per_day)
# ```
# 
# When you run the code, it will output:
# 
# ```
# 86400
# ```
# 
# Therefore, there are 86,400 seconds in a day.

# # 4. Calculate seconds per day again, but this time save the result in a variable called seconds_per_day
# 
# To calculate the number of seconds in a day and save the result in a variable called `seconds_per_day`, you can multiply the number of seconds in an hour by the number of minutes per hour and the number of hours per day. Here's an example:
# 
# ```python
# seconds_per_hour = 3600
# minutes_per_hour = 60
# hours_per_day = 24
# 
# seconds_per_day = seconds_per_hour * minutes_per_hour * hours_per_day
# 
# print(seconds_per_day)
# ```
# 
# When you run the code, it will output:
# 
# ```
# 86400
# ```
# 
# The value `86400` represents the number of seconds in a day. It is now stored in the variable `seconds_per_day`, and you can use this variable in your code for any further calculations or operations related to seconds in a day.

# # 5. Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
# 
# To divide the `seconds_per_day` variable by the `seconds_per_hour` variable using floating-point division, you can simply use the division operator (`/`). Here's an example:
# 
# ```python
# seconds_per_day = 86400
# seconds_per_hour = 3600
# 
# result = seconds_per_day / seconds_per_hour
# 
# print(result)
# ```
# 
# When you run the code, it will output:
# 
# ```
# 24.0
# ```
# 
# The result of dividing the `seconds_per_day` by `seconds_per_hour` is `24.0`. The result is a float value because floating-point division was used.

# # 6. Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree with the floating-point value from the previous question, aside from the final .0?
# 
# To divide the `seconds_per_day` variable by the `seconds_per_hour` variable using integer division (floor division), you can use the double forward slash operator (`//`). Here's an example:
# 
# ```python
# seconds_per_day = 86400
# seconds_per_hour = 3600
# 
# result = seconds_per_day // seconds_per_hour
# 
# print(result)
# ```
# 
# When you run the code, it will output:
# 
# ```
# 24
# ```
# 
# The result of the integer division (`//`) is `24`, which agrees with the floating-point value (`24.0`) from the previous question. The only difference is the absence of the decimal point and the `.0` in the integer division result. Both calculations yield the same whole number result of `24`, indicating that there are 24 hours in a day.

# # 7. Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
# 
# Here's an implementation of a generator function called `genPrimes` that generates the sequence of prime numbers on successive calls to its `next()` method:
# 
# ```python
# def genPrimes():
#     # Start with the first prime number
#     num = 2
# 
#     while True:
#         if isPrime(num):
#             yield num
#         num += 1
# 
# def isPrime(n):
#     # Check if a number is prime
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# ```
# 
# In this implementation, the `genPrimes` function is a generator that continuously generates prime numbers. It starts with the first prime number, which is 2, and then increments the number by 1 on each iteration.
# 
# The `isPrime` function is a helper function that checks whether a number is prime. It returns `True` if the number is prime and `False` otherwise. It uses a basic primality test by iterating from 2 to the square root of the number and checking if any of the numbers evenly divide the given number.
# 
# To use the `genPrimes` generator, you can call its `next()` method in a loop to obtain the next prime number in the sequence. Here's an example:
# 
# ```python
# primes = genPrimes()
# 
# print(next(primes))  # Output: 2
# print(next(primes))  # Output: 3
# print(next(primes))  # Output: 5
# print(next(primes))  # Output: 7
# print(next(primes))  # Output: 11
# # Continue calling next(primes) to get subsequent prime numbers
# ```
# 
# Each call to `next(primes)` will yield the next prime number in the sequence.

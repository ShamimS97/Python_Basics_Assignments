#!/usr/bin/env python
# coding: utf-8

# # 1. What advantages do Excel spreadsheets have over CSV spreadsheets?
# 
# Excel spreadsheets offer several advantages over CSV (Comma-Separated Values) spreadsheets. Here are some key advantages:
# 
# 1. Data Formatting: Excel allows you to format and style data in various ways, including applying different fonts, colors, and cell borders. It supports formatting options such as conditional formatting, data validation, and number formatting, which CSV files lack.
# 
# 2. Formulas and Functions: Excel provides a wide range of built-in formulas and functions that can be used to perform complex calculations and data analysis. These formulas can reference cells, perform arithmetic operations, manipulate text, and more. CSV files, on the other hand, contain only raw data without the ability to perform calculations directly.
# 
# 3. Multiple Sheets: Excel allows you to create multiple sheets within a single workbook, enabling you to organize and manage related data in a structured manner. This feature is absent in CSV files, where each file represents a single sheet.
# 
# 4. Data Visualization: Excel offers various charting and graphing capabilities to visually represent data. You can create different types of charts, such as bar graphs, pie charts, line graphs, and scatter plots, directly within Excel. This feature is not available in CSV files, which contain only plain text data.
# 
# 5. Data Validation: Excel enables you to define data validation rules to ensure data integrity and consistency. You can restrict data entry based on predefined criteria, such as numeric ranges, date formats, or specific text values. CSV files do not have built-in data validation mechanisms.
# 
# 6. Filtering and Sorting: Excel provides filtering and sorting options that allow you to quickly analyze and manipulate data. You can filter data based on specific criteria and sort it in ascending or descending order. CSV files do not have these built-in features.
# 
# 7. Macros and Automation: Excel supports macros, which are scripts written in VBA (Visual Basic for Applications) that automate repetitive tasks or perform complex operations. Macros can be used to automate data processing, generate reports, and perform various other tasks. CSV files do not support macros.
# 
# 8. Collaboration and Sharing: Excel offers collaboration features that allow multiple users to work on the same spreadsheet simultaneously. It supports features like track changes, comments, and sharing options. While CSV files can be shared and edited by multiple users, they lack built-in collaboration features.
# 
# It's worth noting that CSV files have their own advantages, such as simplicity, ease of use, and compatibility with a wide range of software applications. However, Excel's extensive features make it a powerful tool for data analysis, visualization, and complex calculations.

# # 2.What do you pass to csv.reader() and csv.writer() to create reader and writer objects?
# 
# To create reader and writer objects using the `csv` module in Python, you need to pass file objects as arguments to the `csv.reader()` and `csv.writer()` functions, respectively. Here's how you can create reader and writer objects:
# 
# 1. Creating a Reader Object:
# To read data from a CSV file, you need to create a reader object. Here's an example:
# 
# ```python
# import csv
# 
# # Open the CSV file in read mode
# with open('data.csv', 'r') as file:
# 
#     # Create a reader object
#     reader = csv.reader(file)
#     
#     # Use the reader object to read data
#     for row in reader:
#         # Process each row
#         print(row)
# ```
# 
# In the above code, `csv.reader()` is used to create a reader object `reader` by passing the `file` object opened in read mode.
# 
# 2. Creating a Writer Object:
# To write data to a CSV file, you need to create a writer object. Here's an example:
# 
# ```python
# import csv
# 
# # Open the CSV file in write mode
# with open('output.csv', 'w', newline='') as file:
# 
#     # Create a writer object
#     writer = csv.writer(file)
#     
#     # Write data using the writer object
#     writer.writerow(['Name', 'Age', 'Country'])
#     writer.writerow(['John Doe', 30, 'USA'])
#     writer.writerow(['Jane Smith', 25, 'Canada'])
# ```
# 
# In the above code, `csv.writer()` is used to create a writer object `writer` by passing the `file` object opened in write mode. The optional `newline=''` argument is used to handle newline characters in CSV files correctly.
# 
# Once you have created the reader or writer object, you can use them to read or write data respectively, based on your requirements. Remember to open the file in the appropriate mode ('r' for reading and 'w' for writing) before creating the reader or writer object.

# # 3. What modes do File objects for reader and writer objects need to be opened in?
# 
# The file objects used for reader and writer objects in the `csv` module need to be opened in different modes depending on the operation you want to perform. Here are the recommended modes for opening file objects:
# 
# 1. Reader Object:
# To create a reader object for reading data from a CSV file, the file object needs to be opened in **read mode ('r')**. This is because the reader object only reads data from the file and does not modify it. Here's an example:
# 
# ```python
# import csv
# 
# # Open the CSV file in read mode
# with open('data.csv', 'r') as file:
# 
#     # Create a reader object
#     reader = csv.reader(file)
#     
#     # Use the reader object to read data
#     for row in reader:
#         # Process each row
#         print(row)
# ```
# 
# In the above code, the file object `file` is opened in read mode ('r') using the `open()` function. This allows the reader object `reader` to access the file and read the CSV data.
# 
# 2. Writer Object:
# To create a writer object for writing data to a CSV file, the file object needs to be opened in **write mode ('w')**. This mode allows the writer object to create a new file or overwrite an existing file with the newly written data. Here's an example:
# 
# ```python
# import csv
# 
# # Open the CSV file in write mode
# with open('output.csv', 'w', newline='') as file:
# 
#     # Create a writer object
#     writer = csv.writer(file)
#     
#     # Write data using the writer object
#     writer.writerow(['Name', 'Age', 'Country'])
#     writer.writerow(['John Doe', 30, 'USA'])
#     writer.writerow(['Jane Smith', 25, 'Canada'])
# ```
# 
# In the above code, the file object `file` is opened in write mode ('w') using the `open()` function. The optional `newline=''` argument is used to handle newline characters in CSV files correctly. The writer object `writer` can then write data to the file using methods like `writerow()`.
# 
# Remember to use the appropriate mode ('r' or 'w') when opening the file object based on whether you want to read from or write to the CSV file.

# # 4. What method takes a list argument and writes it to a CSV file?
# 
# The method that takes a list argument and writes it to a CSV file is the `writerow()` method of the writer object in the `csv` module. This method is used to write a single row of data to the CSV file. Each element in the list represents a value in the row, and the method automatically handles the formatting and delimiter placement. Here's an example:
# 
# ```python
# import csv
# 
# # Open the CSV file in write mode
# with open('output.csv', 'w', newline='') as file:
# 
#     # Create a writer object
#     writer = csv.writer(file)
#     
#     # Write data using the writer object
#     row1 = ['Name', 'Age', 'Country']
#     row2 = ['John Doe', 30, 'USA']
#     row3 = ['Jane Smith', 25, 'Canada']
#     
#     writer.writerow(row1)  # Writing the first row
#     writer.writerow(row2)  # Writing the second row
#     writer.writerow(row3)  # Writing the third row
# ```
# 
# In the above code, the `writerow()` method is called on the writer object `writer` for each row of data to be written. The `row1`, `row2`, and `row3` lists represent the data for each row. The method automatically writes the elements of the list as separate fields in the CSV file.
# 
# After executing the code, the CSV file named 'output.csv' will contain the following content:
# 
# ```
# Name,Age,Country
# John Doe,30,USA
# Jane Smith,25,Canada
# ```
# 
# Each row of the list is written as a separate row in the CSV file.

# # 5. What do the keyword arguments delimiter and line terminator do?
# 
# The keyword arguments `delimiter` and `line terminator` are used in the `csv.writer()` function of the `csv` module in Python. These arguments allow you to customize the delimiter character and line terminator used in the CSV file. Here's a brief explanation of each argument:
# 
# 1. `delimiter`:
# The `delimiter` argument specifies the character used to separate individual fields (values) within a CSV row. By default, the delimiter is a comma (`,`). However, you can specify a different delimiter character if needed. Here's an example:
# 
# ```python
# import csv
# 
# # Open the CSV file in write mode
# with open('output.csv', 'w', newline='') as file:
# 
#     # Create a writer object with a custom delimiter
#     writer = csv.writer(file, delimiter='|')
#     
#     # Write data using the writer object
#     row = ['John Doe', 30, 'USA']
#     writer.writerow(row)
# ```
# 
# In the above code, the `csv.writer()` function is called with the `delimiter='|'` argument to set the delimiter character as a pipe symbol (`|`) instead of the default comma (`,`). The `writerow()` method then writes the `row` list to the CSV file using the specified delimiter.
# 
# The resulting CSV file will have the following content:
# 
# ```
# John Doe|30|USA
# ```
# 
# 2. `line terminator`:
# The `line terminator` argument specifies the character(s) used to terminate each line in the CSV file. By default, it uses the system's default line terminator (e.g., `\r\n` on Windows, `\n` on Unix-like systems). However, you can specify a different line terminator if desired. Here's an example:
# 
# ```python
# import csv
# 
# # Open the CSV file in write mode
# with open('output.csv', 'w', newline='') as file:
# 
#     # Create a writer object with a custom line terminator
#     writer = csv.writer(file, lineterminator='\r\n')
#     
#     # Write data using the writer object
#     row = ['John Doe', 30, 'USA']
#     writer.writerow(row)
# ```
# 
# In the above code, the `csv.writer()` function is called with the `lineterminator='\r\n'` argument to set the line terminator as carriage return followed by a newline character (`\r\n`). This is different from the default line terminator, which might be different depending on the operating system.
# 
# The resulting CSV file will have the following content:
# 
# ```
# John Doe,30,USA\r\n
# ```
# 
# Note that in the above representation, `\r\n` is used to represent the line terminator, but it will be displayed as a new line when viewed in a text editor or when read by other programs.
# 
# By customizing the `delimiter` and `line terminator` arguments, you can adapt the CSV file format to match specific requirements or compatibility with other systems.

# # 6. What function takes a string of JSON data and returns a Python data structure?
# 
# The function that takes a string of JSON data and returns a Python data structure is `json.loads()`. This function is part of the built-in `json` module in Python and is used to parse (load) a JSON-formatted string into a corresponding Python data structure. Here's an example:
# 
# ```python
# import json
# 
# json_data = '{"name": "John", "age": 30, "country": "USA"}'
# 
# # Parse the JSON data
# python_data = json.loads(json_data)
# 
# # Access the Python data structure
# print(python_data["name"])     # Output: John
# print(python_data["age"])      # Output: 30
# print(python_data["country"])  # Output: USA
# ```
# 
# In the above code, the `json.loads()` function is used to parse the `json_data` string, which represents a JSON object. It converts the JSON string into a corresponding Python data structure, which in this case is a dictionary. The resulting Python data structure is stored in the variable `python_data`.
# 
# After parsing, you can access the elements of the Python data structure just like you would with any other Python dictionary or data structure. In the example, we access the values of the "name", "age", and "country" keys in the `python_data` dictionary.
# 
# The output of the above code will be:
# 
# ```
# John
# 30
# USA
# ```
# 
# By using `json.loads()`, you can convert JSON data into a format that can be easily manipulated and processed within your Python program.

# # 7. What function takes a Python data structure and returns a string of JSON data?
# 
# The function that takes a Python data structure and returns a string of JSON data is `json.dumps()`. This function is part of the built-in `json` module in Python and is used to serialize (dump) a Python object into a JSON-formatted string. Here's an example:
# 
# ```python
# import json
# 
# # Create a Python data structure
# python_data = {
#     "name": "John",
#     "age": 30,
#     "country": "USA"
# }
# 
# # Convert the Python data structure to JSON
# json_data = json.dumps(python_data)
# 
# # Print the JSON data
# print(json_data)
# ```
# 
# In the above code, the `json.dumps()` function is used to convert the `python_data` dictionary into a JSON-formatted string. The resulting JSON string is stored in the variable `json_data`.
# 
# After converting the Python data structure to JSON, you can perform various operations with the resulting JSON string. In the example, we simply print the JSON data to the console.
# 
# The output of the above code will be:
# 
# ```
# {"name": "John", "age": 30, "country": "USA"}
# ```
# 
# The `json.dumps()` function provides additional optional parameters to control the formatting of the resulting JSON string. For example, you can use the `indent` parameter to specify the indentation level for pretty-printing the JSON data:
# 
# ```python
# json_data = json.dumps(python_data, indent=4)
# ```
# 
# This will result in the JSON data being formatted with an indentation of 4 spaces for improved readability.
# 
# By using `json.dumps()`, you can convert Python data structures into JSON format, which is commonly used for data interchange between different systems and languages.

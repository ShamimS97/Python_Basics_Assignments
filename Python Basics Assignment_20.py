#!/usr/bin/env python
# coding: utf-8

# ### 1. Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.
# 
# ```python
# test1 = 'This is a test of the emergency text system'
# 
# with open('test.txt', 'w') as file:
#     file.write(test1)
# ```
# 
# In this code, the variable `test1` is assigned the string value `'This is a test of the emergency text system'`.
# 
# The `open()` function is used to open the file `test.txt` in write mode (`'w'`). This will create the file if it doesn't exist or overwrite it if it does.
# 
# The `write()` method is called on the file object to write the contents of `test1` to the file.
# 
# Make sure to run this code in the appropriate directory where you want the `test.txt` file to be created.

# ### 2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?
# 
# ```python
# with open('test.txt', 'r') as file:
#     test2 = file.read()
# 
# print(test1 == test2)
# ```
# 
# In this code, the `open()` function is used to open the file `test.txt` in read mode (`'r'`). The `read()` method is called on the file object to read its contents and assign it to the variable `test2`.
# 
# The `print()` statement compares `test1` and `test2` using the equality operator (`==`) and prints `True` if they are the same and `False` otherwise.
# 
# Running this code will output `True` if the contents of `test1` and `test2` are the same, and `False` if there is any difference between them.
# 
# Note: Ensure that the `test.txt` file exists in the current directory or provide the correct path to the file in the `open()` function if it's in a different directory.

# ### 3. Create a CSV file called books.csv by using these lines:
# 
# #### title,author,year
# #### The Weirdstone of Brisingamen,Alan Garner,1960
# #### Perdido Street Station,China Miéville,2000
# #### Thud!,Terry Pratchett,2005
# #### The Spellman Files,Lisa Lutz,2007
# #### Small Gods,Terry Pratchett,1992
# 
# ```python
# import csv
# 
# lines = [
#     ['title', 'author', 'year'],
#     ['The Weirdstone of Brisingamen', 'Alan Garner', '1960'],
#     ['Perdido Street Station', 'China Miéville', '2000'],
#     ['Thud!', 'Terry Pratchett', '2005'],
#     ['The Spellman Files', 'Lisa Lutz', '2007'],
#     ['Small Gods', 'Terry Pratchett', '1992']
# ]
# 
# with open('books.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(lines)
# ```
# 
# In this code, the `csv` module is imported to handle CSV operations.
# 
# The lines of data are defined as a list of lists, where each inner list represents a row of the CSV file.
# 
# The `open()` function is used to open the file `books.csv` in write mode (`'w'`). The `newline=''` parameter is passed to ensure correct line endings in the CSV file.
# 
# A `csv.writer` object is created using the file object, and the `writerows()` method is called to write all the lines of data to the CSV file.
# 
# After executing this code, you should find a `books.csv` file with the provided lines in the same directory where the script is executed.

# ### 4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).
# 
# ```python
# import sqlite3
# 
# # Create a connection to the database (will create a new file if it doesn't exist)
# conn = sqlite3.connect('books.db')
# 
# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()
# 
# # Execute SQL command to create the 'books' table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS books (
#         title TEXT,
#         author TEXT,
#         year INTEGER
#     )
# ''')
# 
# # Commit the changes and close the connection
# conn.commit()
# conn.close()
# ```
# 
# In this code, the `sqlite3` module is imported to work with SQLite databases.
# 
# The `connect()` function is used to establish a connection to the database file. If the file doesn't exist, it will be created.
# 
# A cursor object is created using the connection to execute SQL commands.
# 
# The `execute()` method is called on the cursor object to execute an SQL command. In this case, it creates the `books` table with the specified fields: `title` (text), `author` (text), and `year` (integer).
# 
# After executing this code, you should have a `books.db` file containing the SQLite database with the `books` table and its fields.

# ### 5. Read books.csv and insert its data into the book table.
# 
# ```python
# import csv
# import sqlite3
# 
# # Open the CSV file for reading
# with open('books.csv', 'r') as file:
#     # Create a CSV reader object
#     reader = csv.reader(file)
#     
#     # Create a connection to the database
#     conn = sqlite3.connect('books.db')
#     cursor = conn.cursor()
#     
#     # Iterate over each row in the CSV file
#     for row in reader:
#         # Extract the values from the row
#         title, author, year = row
#         
#         # Execute the SQL command to insert the values into the table
#         cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
#     
#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()
# ```
# 
# In this code, we first import the `csv` and `sqlite3` modules to handle reading the CSV file and interacting with the SQLite database, respectively.
# 
# The `open()` function is used to open the `books.csv` file in read mode (`'r'`), and a CSV reader object is created to read the file.
# 
# We then establish a connection to the `books.db` database using `sqlite3.connect()`, and create a cursor object to execute SQL commands.
# 
# Next, we iterate over each row in the CSV file using a `for` loop. For each row, we extract the values of `title`, `author`, and `year`.
# 
# We then use the `execute()` method on the cursor object to execute an SQL command to insert the values into the `books` table using parameterized queries.
# 
# Finally, we commit the changes using `conn.commit()` and close the connection with `conn.close()`.
# 
# After running this code, the data from the `books.csv` file should be inserted into the `books` table in the `books.db` SQLite database.

# ### 6. Select and print the title column from the book table in alphabetical order.
# 
# ```python
# import sqlite3
# 
# # Create a connection to the database
# conn = sqlite3.connect('books.db')
# cursor = conn.cursor()
# 
# # Execute the SQL command to select the title column from the books table
# cursor.execute("SELECT title FROM books ORDER BY title ASC")
# 
# # Fetch all the rows returned by the query
# rows = cursor.fetchall()
# 
# # Print the title column values
# for row in rows:
#     print(row[0])
# 
# # Close the connection
# conn.close()
# ```
# 
# In this code, we import the `sqlite3` module and establish a connection to the `books.db` SQLite database.
# 
# A cursor object is created to execute SQL commands.
# 
# The `execute()` method is used to execute an SQL command to select the `title` column from the `books` table, ordering the results in ascending order using `ORDER BY title ASC`.
# 
# The `fetchall()` method is then called to fetch all the rows returned by the query.
# 
# Finally, we iterate over the rows and print the value of the `title` column. The `row[0]` syntax is used to access the value of the first (and only) column in each row.
# 
# After running this code, the `title` column values from the `books` table will be printed in alphabetical order.

# ### 7. From the book table, select and print all columns in the order of publication.
# 
# ```python
# import sqlite3
# 
# # Create a connection to the database
# conn = sqlite3.connect('books.db')
# cursor = conn.cursor()
# 
# # Execute the SQL command to select all columns from the books table, ordering by year
# cursor.execute("SELECT * FROM books ORDER BY year")
# 
# # Fetch all the rows returned by the query
# rows = cursor.fetchall()
# 
# # Print the column values
# for row in rows:
#     print(row)
# 
# # Close the connection
# conn.close()
# ```
# 
# In this code, we import the `sqlite3` module and establish a connection to the `books.db` SQLite database.
# 
# A cursor object is created to execute SQL commands.
# 
# The `execute()` method is used to execute an SQL command to select all columns (`*`) from the `books` table, ordering the results by the `year` column.
# 
# The `fetchall()` method is then called to fetch all the rows returned by the query.
# 
# Finally, we iterate over the rows and print each row, which represents all the column values for that row.
# 
# After running this code, all the columns from the `books` table will be printed in the order of publication.

# ### 8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.
# 
# ```python
# from sqlalchemy import create_engine
# 
# # Create the engine to connect to the SQLite database
# engine = create_engine('sqlite:///books.db')
# 
# # Connect to the database
# conn = engine.connect()
# 
# # Perform database operations...
# 
# # Close the connection
# conn.close()
# ```
# 
# In this code, we import the `create_engine` function from `sqlalchemy`.
# 
# The `create_engine` function is used to create an engine object that represents the connection to the SQLite database. The `sqlite:///books.db` string specifies the connection URL, where `books.db` is the name of the SQLite database file.
# 
# We then use the `connect` method of the engine object to establish a connection to the database. The `connect` method returns a connection object, which we can use to perform various database operations.
# 
# You can place your desired database operations between the `conn = engine.connect()` and `conn.close()` statements.
# 
# Remember to replace the `# Perform database operations...` comment with your actual database operations, such as executing queries or performing other database actions.
# 
# After running this code, you will have established a connection to the `books.db` database using SQLAlchemy.

# ### 9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.
# 
# ```python
# import redis
# 
# # Connect to the Redis server
# r = redis.Redis()
# 
# # Create a Redis hash called 'test' with the fields 'count' and 'name'
# r.hset('test', 'count', 1)
# r.hset('test', 'name', 'Fester Bestertester')
# 
# # Print all the fields for 'test'
# fields = r.hgetall('test')
# for field, value in fields.items():
#     print(field.decode(), value.decode())
# ```
# 
# Before running this code, make sure you have Redis server installed and running on your computer. Additionally, ensure that you have installed the `redis` library by running `pip install redis`.
# 
# Once you have Redis and the `redis` library set up, you can execute the above code to create a Redis hash called 'test' with the fields 'count' and 'name', and then print all the fields for 'test'.
# 
# Please note that if you have a Redis server running on a different host or port, you may need to modify the connection parameters when creating the Redis client using `redis.Redis(host='your_host', port=your_port)`.

# ### 10. Increment the count field of test and print it.
# 
# ```python
# import redis
# 
# # Connect to the Redis server
# r = redis.Redis()
# 
# # Increment the count field of 'test'
# r.hincrby('test', 'count', 1)
# 
# # Print the updated count field value
# count = r.hget('test', 'count')
# print(count.decode())
# ```
# 
# In this code, we use the `hincrby` method of the Redis client to increment the value of the count field in the 'test' hash by 1.
# 
# Then, we retrieve the updated value of the count field using the `hget` method, and decode it using the `decode()` method to convert it from bytes to a string.
# 
# Finally, we print the updated count field value.
# 
# After running this code, you will see the incremented value of the count field printed to the console.

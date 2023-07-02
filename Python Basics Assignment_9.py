#!/usr/bin/env python
# coding: utf-8

# # 1. To what does a relative path refer?
# 
# A relative path refers to the location of a file or directory relative to the current working directory or another reference point. It specifies the path starting from the current location rather than from the root of the file system.
# 
# In other words, a relative path describes the location of a file or directory relative to the current directory or another specified directory. It does not provide the full path from the root of the file system but instead indicates the necessary steps to navigate from the current directory to the target file or directory.
# 
# For example, consider the following directory structure:
# 
# ```
# - project
#   - src
#     - main.py
#   - data
#     - file.txt
# ```
# 
# If the current working directory is the `project` directory, a relative path to `file.txt` from `main.py` would be `'../data/file.txt'`. The `..` signifies going up one level in the directory hierarchy to reach the `project` directory, and then moving into the `data` directory to access `file.txt`.
# 
# Relative paths are useful for referencing files and directories within the same project or directory structure without relying on the absolute path, which may vary across different systems or environments.

# # 2. What does an absolute path start with your operating system?
# 
# The exact format of an absolute path depends on the operating system you are using. However, in most operating systems, an absolute path starts with the root directory.
# 
# Here are some common conventions for absolute paths in different operating systems:
# 
# - Windows: An absolute path in Windows typically starts with the drive letter followed by a colon (`C:`) and then the backslash (`\`). For example: `C:\path\to\file.txt`.
# - Unix-like systems (Linux, macOS, Unix): An absolute path in Unix-like systems starts with a forward slash (`/`). For example: `/path/to/file.txt`.
# 
# In both cases, the absolute path provides the full and specific location of a file or directory starting from the root of the file system. It includes all necessary directory names and separators to navigate directly to the target file or directory, regardless of the current working directory.
# 
# It's worth noting that the exact conventions and syntax for absolute paths may have some variations depending on the operating system and file system being used.

# # 3. What do the functions os.getcwd() and os.chdir() do?
# 
# The functions `os.getcwd()` and `os.chdir()` are part of the `os` module in Python and are used to interact with the file system.
# 
# 1. `os.getcwd()`:
#    - The `os.getcwd()` function returns the current working directory (CWD) as a string.
#    - The current working directory refers to the directory from which the Python script is being executed.
#    - It returns the absolute path of the current working directory.
# 
# 2. `os.chdir(path)`:
#    - The `os.chdir()` function is used to change the current working directory to the specified `path`.
#    - `path` can be either an absolute path or a relative path.
#    - When `os.chdir()` is called with a valid `path`, the current working directory is updated to the specified location.
#    - If the specified `path` does not exist or is invalid, it raises an exception (typically `FileNotFoundError` or `OSError`).
# 
# Here's an example that demonstrates the use of these functions:
# 
# ```python
# import os
# 
# # Get the current working directory
# current_dir = os.getcwd()
# print("Current directory:", current_dir)
# 
# # Change the current working directory
# new_dir = "/path/to/new/directory"
# os.chdir(new_dir)
# print("Changed to:", os.getcwd())
# ```
# 
# In the example above, `os.getcwd()` is used to obtain the current working directory, and `os.chdir()` is used to change the current working directory to the specified `new_dir`. The updated current working directory is then printed.
# 
# These functions are helpful when you need to work with files and directories in different locations on the file system within your Python scripts.

# # 4. What are the . and .. folders?
# 
# In the context of file systems, the `.` (dot) and `..` (dot-dot) folders have special meanings:
# 
# 1. `.` (dot) folder:
#    - The `.` folder represents the current directory.
#    - It is a reference to the directory where the command or script is currently executing.
#    - It is often used to indicate the current working directory when specifying file paths.
# 
# 2. `..` (dot-dot) folder:
#    - The `..` folder represents the parent directory.
#    - It is a reference to the directory that contains the current directory.
#    - It is used to navigate up one level in the directory hierarchy.
# 
# For example, consider the following directory structure:
# 
# ```
# - project
#   - src
#     - main.py
#   - data
#     - file.txt
# ```
# 
# If the current working directory is `src`, the `.` folder refers to the `src` directory itself, and `..` refers to the `project` directory (the parent directory).
# 
# Here are some examples of how the `.` and `..` folders are used:
# 
# - To reference a file in the current directory: `./file.txt` (equivalent to `file.txt`).
# - To reference a file in the parent directory: `../otherdir/file.txt`.
# - To reference the current directory explicitly: `./` or `.`.
# - To reference the parent directory explicitly: `../` or `..`.
# 
# These special folders are used to navigate and reference files and directories within a file system, making it easier to specify relative paths in different locations.

# # 5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
# 
# In the file path `C:\bacon\eggs\spam.txt`, the directory name and base name can be identified as follows:
# 
# - Directory Name: `C:\bacon\eggs`
#   - The directory name refers to the path of the folder or directory containing the file.
#   - In this case, `C:\bacon\eggs` is the directory name as it represents the path to the folder where `spam.txt` is located.
#   - It includes all the directories leading up to the file.
# 
# - Base Name: `spam.txt`
#   - The base name refers to the actual file name itself, excluding the directory path.
#   - In this case, `spam.txt` is the base name.
#   - It represents the name of the file without any directory information.
# 
# To summarize, in the file path `C:\bacon\eggs\spam.txt`, the directory name is `C:\bacon\eggs`, and the base name is `spam.txt`.

# # 6. What are the three “mode” arguments that can be passed to the open() function?
# 
# The `open()` function in Python allows you to work with files and requires a "mode" argument to specify the intended file access mode. The three main mode arguments that can be passed to the `open()` function are:
# 
# 1. "r" (Read Mode):
#    - The "r" mode is used for reading files.
#    - It is the default mode if no mode argument is specified.
#    - The file must exist, or else an error will occur.
#    - Example: `open("file.txt", "r")`
# 
# 2. "w" (Write Mode):
#    - The "w" mode is used for writing files.
#    - If the file already exists, it will be truncated (emptied).
#    - If the file does not exist, a new file will be created.
#    - Example: `open("file.txt", "w")`
# 
# 3. "a" (Append Mode):
#    - The "a" mode is used for appending data to an existing file.
#    - If the file does not exist, a new file will be created.
#    - The data is added to the end of the file, without overwriting existing content.
#    - Example: `open("file.txt", "a")`
# 
# These mode arguments can be combined with other characters to indicate additional options. For example:
# 
# - "rb": Read mode in binary format.
# - "wb": Write mode in binary format.
# - "ab": Append mode in binary format.
# 
# It's important to note that the `open()` function returns a file object that should be used with the `with` statement or closed explicitly using the `close()` method to ensure proper file handling and resource management.

# # 7. What happens if an existing file is opened in write mode?
# 
# If an existing file is opened in write mode (`"w"`), the file will be truncated, which means that its content will be completely overwritten. The file will be emptied, and any existing data in the file will be lost.
# 
# Here's what happens when an existing file is opened in write mode:
# 
# 1. If the file exists: 
#    - The existing file will be opened in write mode.
#    - All the data in the file will be removed (truncated).
#    - The file pointer will be positioned at the beginning of the file.
#    - Any subsequent write operations to the file will overwrite its content.
#    - If you write new data to the file, it will replace the previous content entirely.
#    - The file size may remain the same if the new content is the same length as the original content, but the file's contents will be different.
# 
# 2. If the file does not exist:
#    - A new file with the specified name will be created.
#    - The file will be opened in write mode.
#    - Any subsequent write operations to the file will add new content.
#    - The file pointer will be positioned at the beginning of the file.
# 
# It's essential to exercise caution when opening files in write mode, as it can result in the loss of existing data. Make sure to have a backup of any important files before opening them in write mode to avoid accidental data loss.

# # 8. How do you tell the difference between read() and readlines()?
# 
# In Python, `read()` and `readlines()` are two methods used to read data from a file, but they differ in how they retrieve and return the data.
# 
# Here's the distinction between `read()` and `readlines()`:
# 
# 1. `read()`:
#    - The `read()` method reads the entire contents of a file and returns them as a single string.
#    - It reads all the characters in the file, including newlines and other special characters.
#    - If no size argument is specified, `read()` reads the entire file.
#    - Example: `file.read()`
# 
# 2. `readlines()`:
#    - The `readlines()` method reads all the lines of a file and returns them as a list of strings.
#    - Each line in the file becomes a separate string element in the list.
#    - It retains the newline characters at the end of each line.
#    - Example: `file.readlines()`
# 
# To summarize:
# 
# - Use `read()` if you want to read the entire file as a single string, without separating it into individual lines.
# - Use `readlines()` if you want to read the file and retrieve the lines as a list of strings, where each element represents a line from the file.
# 
# Here's an example that demonstrates the difference:
# 
# ```python
# # Example file content:
# # Line 1
# # Line 2
# # Line 3
# 
# # Using read()
# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)
# 
# # Output:
# # Line 1
# # Line 2
# # Line 3
# 
# # Using readlines()
# with open("file.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)
# 
# # Output:
# # ['Line 1\n', 'Line 2\n', 'Line 3']
# ```
# 
# In the example, `read()` reads the entire file content as a single string, while `readlines()` reads the lines of the file and returns them as a list of strings, with each line being a separate element in the list.

# # 9. What data structure does a shelf value resemble?
# 
# In Python, the `shelf` module provides a way to store and retrieve Python objects in a persistent dictionary-like data structure. The `shelf` value resembles a dictionary because it allows you to store and retrieve data using key-value pairs. It provides a convenient way to persistently store and retrieve data between program runs.
# 
# Internally, the `shelf` module uses a database implementation called "dbm" (database manager) to store the data. The specific database module used depends on the Python implementation and platform. Common database modules used by `shelf` include `dbm.ndbm` (native database), `dbm.gnu` (GNU dbm), `dbm.dumb` (portable fallback implementation), etc.
# 
# The `shelf` value can be accessed and manipulated like a dictionary. You can use dictionary-like operations such as indexing, assignment, deletion, and iteration to work with the data stored in the `shelf`. However, the values stored in the `shelf` must be picklable, meaning they need to be serializable using Python's `pickle` module.
# 
# Here's a simple example that demonstrates the usage of `shelf`:
# 
# ```python
# import shelve
# 
# # Open a shelf file for read and write access
# with shelve.open("mydata") as myshelf:
#     # Store data in the shelf
#     myshelf["key1"] = "value1"
#     myshelf["key2"] = [1, 2, 3]
#     myshelf["key3"] = {"name": "John", "age": 30}
# 
#     # Retrieve data from the shelf
#     print(myshelf["key1"])
#     print(myshelf.get("key2"))
# 
#     # Iterate over the shelf keys and values
#     for key, value in myshelf.items():
#         print(key, value)
# ```
# 
# In this example, the `shelve.open()` function is used to create or open a shelf file called "mydata". The shelf behaves like a dictionary, allowing data to be stored and retrieved using keys. The values stored in the shelf can be of various types, including strings, lists, dictionaries, etc.

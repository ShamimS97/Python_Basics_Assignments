#!/usr/bin/env python
# coding: utf-8

# # 1. How do you distinguish between shutil.copy() and shutil.copytree()?
# 
# The `shutil.copy()` and `shutil.copytree()` functions in Python's `shutil` module are used for copying files and directories, respectively. Here's how you can distinguish between them:
# 
# 1. `shutil.copy(src, dst)`:
#    - The `shutil.copy()` function is used to copy a single file from the source (`src`) to the destination (`dst`).
#    - It takes two arguments: `src` represents the path of the source file to be copied, and `dst` represents the destination path where the file will be copied.
#    - If the `dst` path is a directory, the copied file will have the same filename as the source file and will be placed in the specified directory.
#    - If the `dst` path specifies a file name, the source file will be copied to that specific file location.
#    - Example: `shutil.copy("source_file.txt", "destination_directory/")`
# 
# 2. `shutil.copytree(src, dst)`:
#    - The `shutil.copytree()` function is used to recursively copy an entire directory tree from the source (`src`) to the destination (`dst`).
#    - It takes two arguments: `src` represents the path of the source directory to be copied, and `dst` represents the destination path where the directory tree will be copied.
#    - The entire directory tree, including all files and subdirectories, will be copied to the destination directory.
#    - If the `dst` directory already exists, an error will occur unless the `dirs_exist_ok` parameter is set to `True`.
#    - Example: `shutil.copytree("source_directory/", "destination_directory/")`
# 
# To summarize:
# 
# - Use `shutil.copy()` when you want to copy a single file from the source to the destination.
# - Use `shutil.copytree()` when you want to copy an entire directory tree, including all files and subdirectories, from the source to the destination.
# 
# Both functions provide options for preserving file metadata (such as timestamps and permissions) and handling errors during the copying process. Make sure to refer to the official Python documentation for additional details and optional parameters for these functions.

# # 2. What function is used to rename files??
# 
# The `shutil.move()` function in Python's `shutil` module is used to rename files and directories. It can also be used to move files from one directory to another.
# 
# Here's how you can use `shutil.move()` to rename a file:
# 
# ```python
# import shutil
# 
# # Rename a file
# shutil.move("old_name.txt", "new_name.txt")
# ```
# 
# In the example above, the file named "old_name.txt" is renamed to "new_name.txt" using the `shutil.move()` function. The function takes two arguments: the source file path (the file to be renamed) and the destination file path (the new name for the file).
# 
# It's important to note that if the destination file already exists, it will be overwritten by the source file. If the source and destination paths are in different directories, the `shutil.move()` function will move the file to the new directory while renaming it.
# 
# In addition to renaming files, the `shutil.move()` function can also be used to move files or directories to different locations on the file system.
# 
# Remember to exercise caution when using `shutil.move()` to rename or move files, as it can modify or overwrite existing files. Make sure to double-check your source and destination paths before executing the function to avoid unintended consequences.

# # 3. What is the difference between the delete functions in the send2trash and shutil modules?
# 
# The `send2trash` and `shutil` modules in Python provide functions for deleting files and directories, but they have some differences in terms of behavior and functionality.
# 
# 1. `send2trash` module:
#    - The `send2trash` module provides a cross-platform method for sending files and directories to the operating system's trash or recycle bin instead of permanently deleting them.
#    - The `send2trash.send2trash()` function is used to delete a file or directory by moving it to the trash or recycle bin, depending on the operating system.
#    - This function does not permanently delete the file but provides a way to recover it from the trash or recycle bin if needed.
#    - Example: `send2trash.send2trash("file.txt")`
# 
# 2. `shutil` module:
#    - The `shutil` module provides more direct methods for deleting files and directories, but they result in permanent deletion without the ability to recover them from the trash or recycle bin.
#    - The `shutil.rmtree()` function is used to remove a directory and its contents recursively, permanently deleting all files and subdirectories within it.
#    - The `os.remove()` function can be used to delete a single file permanently.
#    - Example: 
#      - `shutil.rmtree("directory")`
#      - `os.remove("file.txt")`
# 
# To summarize:
# 
# - Use the `send2trash` module when you want to delete files or directories and have the ability to recover them from the trash or recycle bin if needed.
# - Use the `shutil` module when you want to permanently delete files or directories without the option for recovery.
# 
# The choice between these modules depends on your specific requirements and whether you need the ability to recover deleted files or prefer permanent deletion.

# # 4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
# 
# The equivalent method in `ZipFile` objects to the `open()` method in `File` objects is the `ZipFile.open()` method.
# 
# The `ZipFile.open()` method is used to open a file inside a ZIP archive, similar to how the `open()` method is used to open a file in the file system.
# 
# Here's an example of using `ZipFile.open()` to read the contents of a file within a ZIP archive:
# 
# ```python
# import zipfile
# 
# # Open a ZIP archive
# with zipfile.ZipFile("archive.zip", "r") as myzip:
#     # Open a file within the ZIP archive
#     with myzip.open("file.txt") as myfile:
#         # Read and print the contents of the file
#         contents = myfile.read()
#         print(contents)
# ```
# 
# In the example above, `ZipFile("archive.zip", "r")` opens the ZIP archive in read mode, and `myzip.open("file.txt")` opens the file named "file.txt" within the archive. The `with` statement ensures that the file is closed automatically after reading its contents.
# 
# The `ZipFile.open()` method returns a file-like object that can be used to read the contents of the file within the ZIP archive. You can then read the contents using methods like `read()`, `readline()`, or iterate over the lines.
# 
# Note that the `ZipFile` module is part of the Python standard library and provides functionality for working with ZIP archives.

# # 5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
# 
# Here's an example program that searches a folder tree for files with a specific file extension and copies them to a new folder:
# 
# ```python
# import os
# import shutil
# 
# def search_and_copy_files(source_folder, destination_folder, file_extension):
#     for foldername, subfolders, filenames in os.walk(source_folder):
#         for filename in filenames:
#             if filename.endswith(file_extension):
#                 source_path = os.path.join(foldername, filename)
#                 destination_path = os.path.join(destination_folder, filename)
#                 shutil.copy2(source_path, destination_path)
#                 print(f"Copied {filename} to {destination_folder}")
# 
# # Example usage
# source_folder = "path/to/source/folder"
# destination_folder = "path/to/destination/folder"
# file_extension = ".pdf"
# 
# search_and_copy_files(source_folder, destination_folder, file_extension)
# ```
# 
# In this program:
# 
# 1. The `search_and_copy_files()` function takes three parameters: `source_folder` (the root folder to search from), `destination_folder` (the folder where the matching files will be copied to), and `file_extension` (the file extension to search for).
# 
# 2. The `os.walk()` function is used to traverse the folder tree, starting from the `source_folder`. It iterates over all the subfolders and filenames in the tree.
# 
# 3. For each file, the program checks if it ends with the specified `file_extension`. If it does, the source and destination paths are constructed using `os.path.join()`.
# 
# 4. The `shutil.copy2()` function is used to copy the file from the source path to the destination path. This function preserves the original file's metadata such as timestamps.
# 
# 5. After copying a file, a message is printed indicating the file name and the destination folder where it was copied.
# 
# You can modify the `source_folder`, `destination_folder`, and `file_extension` variables in the example code to fit your specific requirements. Make sure to provide the correct paths to the source and destination folders, and specify the desired file extension you want to search for and copy.
# 
# Note: The program uses `shutil.copy2()` to preserve metadata during the copying process. If you don't require metadata preservation, you can use `shutil.copy()` instead.

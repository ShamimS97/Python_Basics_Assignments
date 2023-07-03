#!/usr/bin/env python
# coding: utf-8

# # 1. In what modes should the PdfFileReader() and PdfFileWriter() File objects will be opened?
# 
# In the PyPDF2 library, which is commonly used for working with PDF files in Python, the `PdfFileReader()` and `PdfFileWriter()` functions are used to read and write PDF files, respectively. When using these functions, the file objects should be opened in specific modes. 
# 
# For `PdfFileReader()`, the file object should be opened in binary mode with the "rb" (read binary) mode. This is because PDF files are binary files, and reading them requires binary mode to ensure proper handling of the file's content. Here's an example of how to open a PDF file for reading:
# 
# ```python
# from PyPDF2 import PdfFileReader
# 
# file_path = "path/to/your/file.pdf"
# 
# with open(file_path, "rb") as file:
#     pdf_reader = PdfFileReader(file)
#     # Perform operations with the PdfFileReader object
# ```
# 
# On the other hand, `PdfFileWriter()` is used to create or modify PDF files. When using this function, the file object should be opened in binary mode with the "wb" (write binary) mode. Here's an example of how to open a PDF file for writing:
# 
# ```python
# from PyPDF2 import PdfFileWriter
# 
# file_path = "path/to/your/file.pdf"
# 
# with open(file_path, "wb") as file:
#     pdf_writer = PdfFileWriter()
#     # Perform operations with the PdfFileWriter object
# ```
# 
# By opening the file objects in the appropriate modes, you ensure that the PyPDF2 library can read or write the PDF file correctly.

# # 2. From a PdfFileReader object, how do you get a Page object for page 5?
# 
# To obtain a Page object for a specific page in a PDF file using the PyPDF2 library's PdfFileReader object, you can use the `getPage()` method. To get the Page object for page 5, you would use the index 4, as the index starts from 0.
# 
# Here's an example:
# 
# ```python
# from PyPDF2 import PdfFileReader
# 
# file_path = "path/to/your/file.pdf"
# 
# with open(file_path, "rb") as file:
#     pdf_reader = PdfFileReader(file)
#     page_number = 5  # Page number you want (starting from 1)
#     
#     if page_number >= 1 and page_number <= pdf_reader.getNumPages():
#         page_object = pdf_reader.getPage(page_number - 1)
#         # Perform operations with the Page object
#     else:
#         print("Invalid page number.")
# ```
# 
# In this example, `pdf_reader.getNumPages()` returns the total number of pages in the PDF file. We subtract 1 from the page_number variable because the index starts from 0, while page numbers typically start from 1.
# 
# After obtaining the Page object, you can perform various operations on it, such as extracting text, modifying the page content, or extracting images.

# # 3. What PdfFileReader variable stores the number of pages in the PDF document?
# 
# The `PdfFileReader` variable that stores the number of pages in the PDF document is `numPages`. It is a property of the `PdfFileReader` object in the PyPDF2 library.
# 
# Here's an example of how to access the `numPages` variable:
# 
# ```python
# from PyPDF2 import PdfFileReader
# 
# file_path = "path/to/your/file.pdf"
# 
# with open(file_path, "rb") as file:
#     pdf_reader = PdfFileReader(file)
#     total_pages = pdf_reader.numPages
#     print("Total number of pages:", total_pages)
# ```
# 
# In this example, `pdf_reader.numPages` returns the total number of pages in the PDF document. You can assign it to a variable, such as `total_pages`, and use it for further processing or display purposes.
# 
# Note that the `numPages` variable represents the total count of pages in the PDF document, starting from 1.

# # 4. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?
# 
# If a `PdfFileReader` object's PDF is encrypted with the password "swordfish," you need to provide the password before you can obtain Page objects from it. This is necessary to decrypt the PDF file and gain access to its contents.
# 
# To decrypt the encrypted PDF, you can use the `decrypt()` method of the `PdfFileReader` object and pass the password as a string parameter.
# 
# Here's an example:
# 
# ```python
# from PyPDF2 import PdfFileReader
# 
# file_path = "path/to/your/file.pdf"
# password = "swordfish"
# 
# with open(file_path, "rb") as file:
#     pdf_reader = PdfFileReader(file)
#     
#     if pdf_reader.isEncrypted:
#         pdf_reader.decrypt(password)
#     
#     # Now you can obtain Page objects and perform operations
#     # on the decrypted PDF file
#     page_object = pdf_reader.getPage(0)  # Example: Get the first page
#     # Perform operations with the Page object
# ```
# 
# In this example, `pdf_reader.isEncrypted` checks if the PDF is encrypted. If it is, the `pdf_reader.decrypt(password)` method is called to decrypt the PDF using the provided password. After decrypting the PDF, you can proceed to obtain Page objects or perform any other operations on the decrypted document.
# 
# It's important to note that you should only attempt to decrypt the PDF if you have the correct password. Otherwise, you won't be able to access the encrypted PDF's content.

# # 5. What methods do you use to rotate a page?
# 
# To rotate a page in a PDF using the PyPDF2 library, you can use the `rotateClockwise()` and `rotateCounterClockwise()` methods available for the `PageObject` class.
# 
# Here's how you can use these methods to rotate a page:
# 
# ```python
# from PyPDF2 import PdfFileReader, PdfFileWriter
# 
# file_path = "path/to/your/file.pdf"
# 
# with open(file_path, "rb") as file:
#     pdf_reader = PdfFileReader(file)
#     
#     page_number = 1  # Example: Rotate the first page
#     page = pdf_reader.getPage(page_number - 1)
#     
#     # Rotate the page clockwise by 90 degrees
#     page.rotateClockwise(90)
#     
#     # Rotate the page counter-clockwise by 180 degrees
#     # page.rotateCounterClockwise(180)
#     
#     # Create a new PDF writer object
#     pdf_writer = PdfFileWriter()
#     pdf_writer.addPage(page)
#     
#     # Save the rotated page to a new PDF file
#     output_file_path = "path/to/save/rotated_file.pdf"
#     with open(output_file_path, "wb") as output_file:
#         pdf_writer.write(output_file)
# ```
# 
# In this example, we first open the PDF file and create a `PdfFileReader` object. We specify the page number (starting from 1) that we want to rotate, and we retrieve the corresponding `PageObject` using `pdf_reader.getPage()`. 
# 
# Next, we use the `rotateClockwise()` or `rotateCounterClockwise()` method on the `PageObject` to rotate the page as desired. You can choose to rotate the page clockwise or counter-clockwise by specifying the rotation angle in degrees.
# 
# After rotating the page, we create a new `PdfFileWriter` object, add the rotated page to it using `pdf_writer.addPage()`, and then save the modified page to a new PDF file using `pdf_writer.write()`.
# 
# You can uncomment the `rotateCounterClockwise()` line and comment out the `rotateClockwise()` line if you want to rotate the page in the opposite direction.

# # 6. What is the difference between a Run object and a Paragraph object?
# 
# In the context of document processing and text formatting, a Run object and a Paragraph object represent different elements and have distinct purposes.
# 
# 1. Run object: 
#    - A Run object represents a contiguous run of text within a paragraph that shares the same formatting properties.
#    - It is a subset of text within a paragraph that has consistent formatting, such as font style, size, color, or other character-level attributes.
#    - Runs allow you to apply different formatting to different parts of a paragraph without splitting it into separate paragraphs.
#    - For example, within a single paragraph, you may have different words or phrases in bold, italic, or with different font sizes. Each of these variations would be represented as a separate Run object.
# 
# 2. Paragraph object:
#    - A Paragraph object represents a distinct block of text or content with its own formatting properties.
#    - It typically consists of one or more sentences or lines of text that are logically grouped together.
#    - Paragraphs are used to organize and structure the content within a document.
#    - They have formatting properties such as alignment, indentation, line spacing, or other paragraph-level attributes.
#    - You can apply formatting to the entire paragraph as a whole, affecting all the text within it.
# 
# In summary, a Run object represents a portion of text within a paragraph with consistent formatting, while a Paragraph object represents a block of text with its own formatting properties. Runs allow for more granular control over formatting within a paragraph, while paragraphs provide a higher-level structure for organizing content in a document.

# # 7. How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?
# 
# To obtain a list of Paragraph objects for a Document object stored in a variable named `doc`, it depends on the specific library or tool you are using for document processing. However, assuming you are referring to the `python-docx` library, which is commonly used for working with Microsoft Word documents in Python, you can iterate over the `doc.paragraphs` property to access each Paragraph object.
# 
# Here's an example:
# 
# ```python
# from docx import Document
# 
# # Assuming `doc` is a Document object
# 
# paragraphs = doc.paragraphs
# 
# for paragraph in paragraphs:
#     # Perform operations with each Paragraph object
#     print(paragraph.text)  # Example: Print the text content of each paragraph
# ```
# 
# In this example, `doc.paragraphs` returns a list of Paragraph objects contained within the Document object `doc`. You can iterate over this list using a `for` loop to access each Paragraph object individually. Within the loop, you can perform operations on each Paragraph object, such as retrieving its text content, applying formatting, or modifying the paragraph structure.
# 
# The `paragraph.text` property gives you access to the plain text content of each paragraph. You can replace `print(paragraph.text)` with the desired operations or manipulations you want to perform with each Paragraph object.
# 
# Note that this example assumes you have already loaded a Word document into the `doc` variable using the `Document` class from the `python-docx` library.

# # 8. What type of object has bold, underline, italic, strike, and outline variables?
# 
# The `Font` object in various document processing libraries or tools typically has variables or properties such as `bold`, `underline`, `italic`, `strike`, and `outline`. The `Font` object represents the formatting properties of a specific text range, such as a Run object within a document.
# 
# The specific implementation and availability of these variables may vary depending on the library or tool being used. However, in general, the `Font` object allows you to control the font-related formatting attributes of a text range, including boldness, underline style, italicization, strikethrough, and outline formatting.
# 
# Here's a general example demonstrating how these variables might be used in the context of the `Font` object:
# 
# ```python
# from docx import Document
# 
# # Assuming you have a Run object stored in the variable `run`
# 
# font = run.font
# 
# # Access and modify the font formatting attributes
# font.bold = True
# font.underline = True
# font.italic = True
# font.strike = True
# font.outline = True
# ```
# 
# In this example, the `run` object represents a specific text range, such as a word or phrase within a paragraph. By accessing its `font` property, you can retrieve the associated `Font` object and modify its formatting attributes. Setting the respective attributes to `True` enables the formatting, such as making the text bold, underlined, italicized, struck through, or outlined.
# 
# It's important to note that the specific syntax and usage may differ depending on the document processing library or tool you are using. The example above assumes the usage of the `python-docx` library for working with Microsoft Word documents in Python.

# # 9. What is the difference between False, True, and None for the bold variable?
# 
# In the context of the `bold` variable, which typically belongs to the `Font` object in document processing libraries, `False`, `True`, and `None` have different meanings:
# 
# 1. `False`: Setting the `bold` variable to `False` means that the text is not formatted as bold. It indicates that the text should have regular or normal weight without any bold emphasis.
# 
# 2. `True`: Setting the `bold` variable to `True` means that the text is formatted as bold. It indicates that the text should appear with a bold weight, providing emphasis or stronger visual weight compared to regular text.
# 
# 3. `None`: In some document processing libraries, setting the `bold` variable to `None` may have different implications. It could mean that the font's bold attribute is not explicitly set, allowing it to inherit the formatting from a higher-level style or the default document settings. The behavior can vary depending on the library or tool being used.
# 
# It's important to consult the documentation of the specific library or tool you are working with to understand how these values are interpreted and the default behavior when `None` is used. The behavior may differ based on the implementation choices of the library or tool.

# # 10. How do you create a Document object for a new Word document?
# 
# To create a `Document` object for a new Word document using the `python-docx` library, you can simply call the `Document()` constructor without any parameters. This will create a new, empty Word document.
# 
# Here's an example:
# 
# ```python
# from docx import Document
# 
# # Create a new Word document
# doc = Document()
# 
# # Perform operations with the Document object
# doc.add_paragraph("Hello, World!")  # Example: Add a paragraph with text
# 
# # Save the document to a file
# doc.save("path/to/save/document.docx")
# ```
# 
# In this example, the `Document()` constructor creates a new `Document` object, representing an empty Word document. You can then perform various operations with the `doc` object, such as adding paragraphs, applying formatting, inserting tables or images, and so on.
# 
# After manipulating the document as desired, you can save it to a file using the `save()` method of the `Document` object. Specify the desired file path and name with the `.docx` extension to save the document in the Microsoft Word file format.
# 
# Note that you will need the `python-docx` library installed to create and manipulate Word documents in this manner. You can install it using `pip install python-docx` if you haven't already.

# # 11. How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc?
# 
# To add a paragraph with the text 'Hello, there!' to a `Document` object stored in a variable named `doc` using the `python-docx` library, you can use the `add_paragraph()` method of the `Document` object.
# 
# Here's an example:
# 
# ```python
# from docx import Document
# 
# # Assuming `doc` is a Document object
# 
# # Add a paragraph with the text 'Hello, there!'
# doc.add_paragraph('Hello, there!')
# 
# # Save the document to a file
# doc.save('path/to/save/document.docx')
# ```
# 
# In this example, the `add_paragraph()` method is used to add a new paragraph with the specified text, 'Hello, there!', to the `Document` object `doc`. This method automatically creates a new paragraph and appends it to the document.
# 
# After adding the paragraph, you can continue to perform further operations on the `Document` object, such as adding more paragraphs, applying formatting, inserting tables or images, and so on.
# 
# Finally, you can save the modified `Document` object to a file using the `save()` method, specifying the desired file path and name with the `.docx` extension.
# 
# Make sure you have the `python-docx` library installed to work with Word documents using the provided code. If you haven't installed it yet, you can use `pip install python-docx` to install it.
# 
# 

# # 12. What integers represent the levels of headings available in Word documents?
# 
# In Word documents, the levels of headings are typically represented using integers. The specific numbering convention for heading levels can vary depending on the style guide or document template being used. However, there are some common conventions:
# 
# 1. Heading 1: Level 1 headings are typically represented by the integer 1.
# 2. Heading 2: Level 2 headings are typically represented by the integer 2.
# 3. Heading 3: Level 3 headings are typically represented by the integer 3.
# 4. Heading 4: Level 4 headings are typically represented by the integer 4.
# 5. Heading 5: Level 5 headings are typically represented by the integer 5.
# 6. Heading 6: Level 6 headings are typically represented by the integer 6.
# 
# These numbering conventions follow a hierarchical structure, where higher-level headings have lower numbers, and lower-level headings have higher numbers.
# 
# It's important to note that the specific numbering conventions may differ based on the document template, style guide, or document processing tool being used. Some templates or tools may allow customization of the numbering scheme for headings.
# 
# When working with the `python-docx` library, for example, you can set the heading level using the `heading_level` attribute of the `Paragraph` object. The numbering starts from 1, where 1 represents Heading 1, 2 represents Heading 2, and so on.

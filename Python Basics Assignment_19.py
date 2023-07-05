#!/usr/bin/env python
# coding: utf-8

# ### 1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?
# 
# ```python
# class Thing:
#     pass
# 
# print(Thing)
# example = Thing()
# print(example)
# ```

# ### 2. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.
# 
# ```python
# class Thing2:
#     letters = 'abc'
# 
# print(Thing2.letters)
# ```
# 
# Output:
# ```
# abc
# ```
# 
# In this example, the `Thing2` class is defined with a class attribute `letters` set to the string 'abc'. When you access the `letters` attribute using `Thing2.letters` and print it, the output will be 'abc'.

# ### 3. Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?
# 
# ```python
# class Thing3:
#     def __init__(self):
#         self.letters = 'xyz'
# 
# # Create an object (instance) of Thing3
# example = Thing3()
# 
# # Print the value of the letters instance attribute
# print(example.letters)
# ```
# 
# Output:
# ```
# xyz
# ```
# 
# In this example, the `Thing3` class is defined with an instance attribute `letters` set to the string 'xyz'. The `__init__` method is used to initialize the instance attribute when an object is created. When you access `example.letters` and print it, the output will be 'xyz'.
# 
# So, yes, you need to create an object of the `Thing3` class to access and print the value of the `letters` instance attribute.

# ### 4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen' ,'H' and 1.
# 
# ```python
# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
# 
# # Create an object of the Element class with the specified values
# hydrogen = Element('Hydrogen', 'H', 1)
# ```
# 
# In this example, the `Element` class is defined with the `__init__` method, which is a special method called when an object is created from the class. The `__init__` method initializes the instance attributes `name`, `symbol`, and `number` with the values passed as arguments.
# 
# To create an object of the `Element` class with the values 'Hydrogen', 'H', and 1, the `hydrogen` object is created by calling `Element('Hydrogen', 'H', 1)`. The values 'Hydrogen', 'H', and 1 are passed as arguments, which will be assigned to the respective instance attributes of the `hydrogen` object.
# 
# Now, the `hydrogen` object represents an element with the attributes `name` as 'Hydrogen', `symbol` as 'H', and `number` as 1.

# ### 5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.
# 
# ```python
# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
# 
# # Dictionary with the keys and values
# element_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
# 
# # Create an object of the Element class using the dictionary
# hydrogen = Element(**element_dict)
# ```
# 
# In this example, the `Element` class is defined with the `__init__` method that initializes the instance attributes `name`, `symbol`, and `number`. 
# 
# The `element_dict` dictionary contains the keys and values representing the attributes of the `Element` class. By using `**element_dict`, the dictionary is unpacked and the values are passed as arguments to the `__init__` method of the `Element` class.
# 
# The `hydrogen` object is created using `Element(**element_dict)`, where the `element_dict` dictionary is unpacked and used to initialize the instance attributes of the `hydrogen` object.
# 
# Now, the `hydrogen` object represents an element with the attributes `name` as 'Hydrogen', `symbol` as 'H', and `number` as 1.

# ### 6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
# 
# ```python
# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#     
#     def dump(self):
#         print(f"Name: {self.name}, Symbol: {self.symbol}, Number: {self.number}")
# 
# # Create an object of the Element class
# hydrogen = Element('Hydrogen', 'H', 1)
# 
# # Use the dump() method to print the attributes
# hydrogen.dump()
# ```
# 
# In this updated example, the `dump()` method is defined within the `Element` class. It takes `self` as a parameter, which refers to the instance of the class. Inside the `dump()` method, the values of the attributes `name`, `symbol`, and `number` are printed using f-string formatting.
# 
# After creating the `hydrogen` object using `Element('Hydrogen', 'H', 1)`, you can call the `dump()` method on the `hydrogen` object to print its attributes. The output will be:
# 
# ```
# Name: Hydrogen, Symbol: H, Number: 1
# ```
# 
# The `dump()` method provides a convenient way to print the attribute values of an `Element` object.

# ### 7. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__,create a new hydrogen object, and call print(hydrogen) again.
# 
# When you call `print(hydrogen)`, it implicitly calls the `__str__()` method of the `hydrogen` object. To change the name of the `dump()` method to `__str__()` and modify its implementation to return a string representation of the object, you can update the `Element` class as follows:
# 
# ```python
# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#     
#     def __str__(self):
#         return f"Name: {self.name}, Symbol: {self.symbol}, Number: {self.number}"
# 
# # Create a new hydrogen object
# hydrogen = Element('Hydrogen', 'H', 1)
# 
# # Call print(hydrogen) to implicitly invoke __str__() method
# print(hydrogen)
# ```
# 
# In this updated example, the `dump()` method is renamed to `__str__()` (double underscores before and after `str`). Inside the `__str__()` method, instead of printing the attributes directly, it returns a string representation of the object using f-string formatting.
# 
# When you call `print(hydrogen)`, it will invoke the `__str__()` method of the `hydrogen` object. The returned string representation will be printed. The output will be:
# 
# ```
# Name: Hydrogen, Symbol: H, Number: 1
# ```
# 
# By implementing the `__str__()` method, you can control how your object is represented as a string when it is printed.

# ### 8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.
# 
# To modify the `Element` class to make the attributes `name`, `symbol`, and `number` private and define getter properties to access their values, you can use Python's property decorator. Here's an example:
# 
# ```python
# class Element:
#     def __init__(self, name, symbol, number):
#         self._name = name
#         self._symbol = symbol
#         self._number = number
#     
#     @property
#     def name(self):
#         return self._name
#     
#     @property
#     def symbol(self):
#         return self._symbol
#     
#     @property
#     def number(self):
#         return self._number
# ```
# 
# In this updated example, the attributes `name`, `symbol`, and `number` are prefixed with an underscore (`_`), indicating that they are intended to be private. Inside the `__init__()` method, these private attributes are assigned the values passed as arguments.
# 
# The `@property` decorator is used above the getter methods (`name()`, `symbol()`, and `number()`) to define them as properties. These getter methods simply return the values of the respective private attributes.
# 
# With this modification, you can access the attributes using the getter properties. For example:
# 
# ```python
# # Create an object of the Element class
# hydrogen = Element('Hydrogen', 'H', 1)
# 
# # Access the attributes using the getter properties
# print(hydrogen.name)
# print(hydrogen.symbol)
# print(hydrogen.number)
# ```
# 
# Output:
# ```
# Hydrogen
# H
# 1
# ```
# 
# By using the getter properties (`name`, `symbol`, and `number`), you can access the private attributes of the `Element` object. This provides a controlled way of accessing the attribute values while keeping them private within the class.

# ### 9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.
# 
# Here's an example of defining the three classes (`Bear`, `Rabbit`, and `Octothorpe`) with the `eats()` method in each class:
# 
# ```python
# class Bear:
#     def eats(self):
#         return 'berries'
# 
# class Rabbit:
#     def eats(self):
#         return 'clover'
# 
# class Octothorpe:
#     def eats(self):
#         return 'campers'
# ```
# 
# In this example, each class (`Bear`, `Rabbit`, and `Octothorpe`) has a single method called `eats()`. When called on an object of the respective class, it returns the specific food that the animal or object eats.
# 
# To create an object from each class and print what they eat, you can use the following code:
# 
# ```python
# bear = Bear()
# rabbit = Rabbit()
# octothorpe = Octothorpe()
# 
# print(bear.eats())         # Output: berries
# print(rabbit.eats())       # Output: clover
# print(octothorpe.eats())   # Output: campers
# ```
# 
# In this code, objects (`bear`, `rabbit`, and `octothorpe`) are created from each class, and the `eats()` method is called on each object to print what they eat.
# 
# Output:
# ```
# berries
# clover
# campers
# ```
# 
# Each object returns the specific food it eats based on the `eats()` method defined in its respective class.

# ### 10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.
# 
# ```python
# class Laser:
#     def does(self):
#         return 'disintegrate'
# 
# class Claw:
#     def does(self):
#         return 'crush'
# 
# class SmartPhone:
#     def does(self):
#         return 'ring'
# 
# class Robot:
#     def __init__(self):
#         self.laser = Laser()
#         self.claw = Claw()
#         self.smartphone = SmartPhone()
#     
#     def does(self):
#         print(f"Laser: {self.laser.does()}")
#         print(f"Claw: {self.claw.does()}")
#         print(f"SmartPhone: {self.smartphone.does()}")
# ```
# 
# In this example, the classes `Laser`, `Claw`, and `SmartPhone` each have a single method called `does()`, which returns the specific action performed by that component.
# 
# The `Robot` class has an `__init__()` method that creates instances of `Laser`, `Claw`, and `SmartPhone` as its attributes. The `does()` method of the `Robot` class then prints the actions performed by each component.
# 
# To create an object of the `Robot` class and call its `does()` method to print what each component does, you can use the following code:
# 
# ```python
# robot = Robot()
# robot.does()
# ```
# 
# Output:
# ```
# Laser: disintegrate
# Claw: crush
# SmartPhone: ring
# ```
# 
# In this code, an object (`robot`) of the `Robot` class is created. Calling `robot.does()` invokes the `does()` method of the `Robot` object, which in turn calls the `does()` methods of its component objects (`Laser`, `Claw`, and `SmartPhone`), printing the specific actions performed by each component.
# 
# Each component object returns the specific action it performs based on the `does()` method defined in its respective class, and the `Robot` object prints these actions for each component.

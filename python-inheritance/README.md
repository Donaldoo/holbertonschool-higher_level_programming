# Python Inheritance

* **Inheritance allows us to define a class that inherits all the methods and properties from another class.**

* **Parent class** is the class being inherited from, also called base class.

* **Child class** is the class that inherits from another class, also called derived class.


#### Creating a Parent Class:
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```

#### Create a Child Class:

To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

##### Example
Create a class named Student, which will inherit the properties and methods from the Person class:

```
class Student(Person):
  pass
```

Files | Content
-------- | -----------
`0-lookup.py` | Python function that returns a list of available attributes and methods of an objects.
`1-my_list.py` | Python class MyList that inherits from list
`2-is_same_class.py` | Python function that returns True if an object is exactly an instance of a specified class; otherwise False
`3-is_kind_of_class.py` | Python function that returns True if an object is an instance or inherited instance of a specified class; otherwise False
`4-inherits_from.py` | Python function that returns True if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise False
`5-base_geometry.py` | An empty Python class BaseGeometry
`6-base_geometry.py` | Public instance method def area(self): that raises an Exception with the message area() is not implemented
`7-base_geometry.py` | Public instance method def integer_validator(self, name, value): that validates the parameter value
`8-rectangle.py` | Python class Rectangle that inherits from BaseGeometry 
`9-rectangle.py` |Python class Rectangle that inherits from BaseGeometry (7-base_geometry.py). Builds on 8-rectangle.py
`10-square.py` | Python class Square that inherits from Rectangle (9-rectangle.py).
`11-square.py` | Python class Square that inherits from Rectangle (9-rectangle.py). Builds on 10-square.py

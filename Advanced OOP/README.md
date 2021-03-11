# Advanced OOP(Object Oriented Programming)


Python is a multi-paradigm programming language. It supports different programming approaches.

One of the popular approaches to solve a programming problem is by creating objects. This is known as **Object-Oriented Programming (OOP)**.

An object has two characteristics:

- attributes
- behavior

_**Let's take an example:**_

A parrot is can be an object, as it has the following properties:

- name, age, color as attributes
- singing, dancing as behavior

The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).


## Multiple inheritance

A class can be derived from more than one base class in Python, similar to C++. This is called multiple inheritance.

In multiple inheritance, the features of all the base classes are inherited into the derived class. The syntax for multiple inheritance is similar to single inheritance.

##### **EXAMPLE**

```python
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
```
Here, the `MultiDerived` class is derived from `Base1` and `Base2` classes. 
The `MultiDerived` class inherits from both `Base1` and `Base2` classes.

### Multilevel inheritance

We can also inherit from a derived class. This is called multilevel inheritance. It can be of any depth in Python.

In multilevel inheritance, features of the base class and the derived class are inherited into the new derived class.

An example with corresponding visualization is given below.

```python
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
```

Here, the `Derived1` class is derived from the `Base` class, and the `Derived2` class is derived from the `Derived1` class.


## ABC

The main goal of the abstract base class is to provide a standardized way to test whether an object adheres to a given specification. It can also prevent any attempt to instantiate a subclass that doesn’t override a particular method in the superclass. And finally, using an abstract class, a class can derive identity from another class without any object inheritance.

### Declaring Abstract Base Class

Python has a module called abc (abstract base class) that offers the necessary tools for crafting an abstract base class. First and foremost, you should understand the `ABCMeta` metaclass provided by the abstract base class. The rule is every abstract class must use `ABCMeta` metaclass.

`ABCMeta` metaclass provides a method called register method that can be invoked by its instance. By using this register method, any abstract base class can become an ancestor of any arbitrary concrete class. Let’s understand this process by considering an example of an abstract base class that registers itself as an ancestor of dict.

```python
import abc 


class AbstractClass(metaclass=abc.ABCMeta): 
	def abstractfunc(self): 
		return None


print(AbstractClass.register(dict)) 
```

**Output:**
``` 
<class 'dict'>
```
Here, dict identifies itself as a subclass of AbstractClass. Let’s do a check.

## Property setter

A setter is a method that sets the value of a property. In OOPs this helps to set the value to private attributes in a class.
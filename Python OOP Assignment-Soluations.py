                                                                   Python OOP Assignment


Q1. What is the purpose of Python's OOP?

Ans:
Python's Object-Oriented Programming (OOP) provides a way to organise code into reusable objects, promoting modularity and code reusability. It simplifies code organisation and enables abstraction, encapsulation, inheritance, and polymorphism.


Q2. Where does an inheritance search look for an attribute?
Ans:
In Python, the inheritance search for an attribute looks first in the instance itself and then in the class and its superclasses.


Q3. How do you distinguish between a class object and an instance object?
Ans:
a class object defines the structure and behaviour of the class, while an instance object is a concrete representation of that class with its own unique data and state. Class objects are used to define the blueprint, and instance objects are created from that blueprint with specific attributes and behaviour.

Q4. What makes the first argument in a class’s method function special?
Ans:
The first argument in a class's method function (conventionally named self) is special because it automatically refers to the instance object on which the method is being called. It allows the method to access and manipulate the instance's attributes and behaviour.

Q5. What is the purpose of the init method?
Ans:
The __init__ method in Python is used to initialise the attributes of an instance when it is created. It allows you to set the initial state of the object and perform any necessary setup or initialization tasks.


Q6. What is the process for creating a class instance?
Ans:
The process for creating a class instance involves defining the class, implementing the __init__ method for initialization, creating an instance of the class using the class name, and then accessing the instance's attributes and methods as needed.



Q7. What is the process for creating a class?
Ans:
The process for creating a class in Python involves defining the class using the 'class' keyword, specifying attributes and methods within the class, and creating instances of the class by calling the class name followed by parentheses.
	

Q8. How would you define the superclasses of a class?
Ans:
To define the superclasses of a class in Python:
Include the superclass names inside parentheses after the class name during class definition.
Separate multiple superclasses with commas if there are multiple inheritance.
The class will inherit attributes and methods from the specified superclasses, allowing for code reuse and sharing of functionality.



Q9. What is the relationship between classes and modules?
Ans:
The relationship between classes and modules in Python is that a module can contain one or more classes, along with other definitions, such as functions or variables. Classes provide a way to organise and encapsulate related data and behaviour within a module.

Q10. How do you make instances and classes?
Ans:
Instances of a class are created by calling the class name followed by parentheses, similar to invoking a function. This creates a new object of the class, which can then access the attributes and methods defined in the class. Classes are created by defining them using the class keyword, specifying attributes and methods within the class block.


Q11. Where and how should class attributes be created?
Ans:
Class attributes should be created inside the class block, but outside any method definitions. They are usually defined directly under the class declaration. Class attributes are shared among all instances of the class and can be accessed using the class name or instances of the class.

Q12. Where and how are instance attributes created?
Ans:
Instance attributes are created within the class's __init__ method by assigning values to the self parameter, which represents the instance being created. Instance attributes are specific to each instance and can hold different values for each object of the class.


Q13. What does the term "self" in a Python class mean?
Ans:
In a Python class, the term "self" is a conventionally used parameter name that represents the instance object on which a method is called. It refers to the specific instance itself and allows accessing its attributes and methods within the class. It acts as a reference to the current object and is used as the first parameter in most method definitions.


Q14. How does a Python class handle operator overloading?
Ans:
Python handles operator overloading in classes by implementing special methods that define the behaviour of operators when applied to instances of the class. These methods have specific names, such as __add__ for the addition operator (+), and they allow customising how operators work with objects of the class.


Q15. When do you consider allowing operator overloading of your classes?
Ans:
Operator overloading is considered when you want to define custom behaviour for operators on your class instances. It is useful when you want to make objects of your class work with operators in a way that makes sense based on the object's semantics. For example, overloading the addition operator (+) for a custom class can enable concatenation or merging of instances in a meaningful way.


Q16. What is the most popular form of operator overloading?
Ans:
The most popular form of operator overloading in Python is method-based operator overloading. It involves defining special methods with specific names, such as __add__, __sub__, __mul__, etc., to handle the corresponding operators (+, -, *, etc.) on instances of the class. These methods allow customising how operators behave when applied to objects of the class.

Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?

Ans:
The two most important concepts to grasp in order to comprehend Python OOP code are class and object. Understanding how classes define the structure and behavior of objects, and how objects interact with each other through methods and attributes, is crucial in understanding and working with OOP code.




Q18. Describe three applications for exception processing.
Ans:
Three applications for exception processing in Python are error handling, graceful program termination, and error reporting. Exceptions allow you to handle unexpected situations, such as file I/O errors, network errors, or invalid input, by catching and handling the exceptions appropriately, providing a more robust and reliable execution of your code.

Q19. What happens if you don't do something extra to treat an exception?
Ans:
If we don't handle or treat an exception in our code, it will propagate up the call stack, potentially causing program termination and displaying an error message. Unhandled exceptions can lead to crashes or unexpected behaviour in our script, making it harder to diagnose and fix issues.

Q20. What are your options for recovering from an exception in your script?
Ans:
Options for recovering from an exception in your script include catching the exception using try and except blocks, where you can handle the exception gracefully, log the error, or provide alternative behaviour. You can also raise a new exception to indicate a different error condition or use finally blocks to ensure certain code is executed regardless of whether an exception occurred or not.

Q21. Describe two methods for triggering exceptions in your script.
Ans:
Two methods for triggering exceptions in your script are using the raise statement to explicitly raise a specific exception at a certain point in the code and using built-in functions or methods that can raise exceptions based on certain conditions. For example, calling open() function on a non-existent file can raise a FileNotFoundError exception.

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of  
whether or not an exception exists.

Ans:
Two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists, are using the finally block, which is executed regardless of whether an exception occurs or not, and using the atexit module to register functions to be called when the program is about to exit.

Q23. What is the purpose of the try statement?
Ans:
The purpose of the try statement in Python is to define a block of code where exceptions can potentially occur. It allows you to handle exceptions and perform appropriate actions based on whether an exception is raised or not.


Q24. What are the two most popular try statement variations?
Ans:
The two most popular variations of the try statement are try-except and try-finally. The try-except variation is used to catch and handle specific exceptions, while the try-finally variation ensures that a specific block of code is executed regardless of whether an exception occurs or not.

Q25. What is the purpose of the raise statement?
Ans:
The purpose of the raise statement in Python is to explicitly raise an exception at a particular point in the code. It allows you to create and trigger your own exceptions, providing a way to signal and handle specific error conditions in your program

Q26. What does the assert statement do, and what other statement is it like?
Ans:
The assert statement in Python is used to test if a given condition is true. It raises an AssertionError exception if the condition evaluates to false, indicating that the program is in an unexpected state. It is similar to the if statement but is used specifically for testing and debugging purposes.

Q27. What is the purpose of the with/as argument, and what other statement is it like?
Ans:
The purpose of the with/as argument in Python is to define a context in which resources are managed automatically. It ensures that certain operations are performed both before and after a block of code is executed. The with/as statement is used for resource management, similar to the try-finally statement, but with a more concise syntax.

Q28. What are *args, **kwargs?
Ans:
'*args' and '**kwargs' are used in Python to accept a variable number of arguments in function definitions. *args allows passing a variable number of positional arguments to a function, while '**kwargs' allows passing a variable number of keyword arguments. These allow for greater flexibility in function parameterization

Q29. How can I pass optional or keyword parameters from one function to another?
Ans:
To pass optional or keyword parameters from one function to another, you can use the *args and '**kwargs'  syntax when calling the function and unpack them when passing them to the other function. This allows you to pass a variable number of arguments or keyword arguments from one function to another, without explicitly specifying each argument.






Q30. What are Lambda Functions?
Ans:
Lambda functions, also known as anonymous functions, are small, inline functions in Python that are defined without a name. They are created using the lambda keyword and are typically used for simple, one-line expressions or small utility functions. Lambda functions are often used in functional programming paradigms or situations where a function is needed as an argument to another function.


"""
Q31. Explain Inheritance in Python with an example?
Ans:
Inheritance in Python allows a class to inherit attributes and methods from another class. It enables code reuse and allows the child class to extend or override the functionality of the parent class.
For example,
a ‘Dog’ class can inherit attributes and methods from an ‘Animal’ class, such as ‘name’ and ‘sound’, while also adding its own specific attributes or methods.

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Bark!")

# Creating instances
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Labrador")

# Accessing attributes and methods
print(animal.name)  # Output: Generic Animal
animal.sound()  # Output: Animal sound

print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Labrador
dog.sound()  # Output: Bark!
"""


Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of 
class C, which version gets invoked?

Ans:
If class C inherits from classes A and B as 'class C(A, B)', and both classes A and B have their own versions of the method 'func()', the version of 'func()' that gets invoked depends on the method resolution order (MRO) of the classes.

In Python, the MRO is determined using the C3 linearization algorithm, which defines the order in which the base classes are searched for a method. The MRO is based on the inheritance hierarchy and ensures that each method is invoked only once.

When calling 'func()' from an object of class C, Python will search for the method in the following order:
1. The class C itself
2. Class A (the first parent class specified in the inheritance declaration)
3. Class B (the second parent class specified in the inheritance declaration)

If both class A and class B have their own versions of 'func()', the version from class A will be invoked first because it appears before class B in the inheritance declaration. If class A does not define 'func()', then the version from class B will be invoked.

It's important to note that if class A and class B have a common ancestor with their own version of 'func()', the MRO ensures that the method from the most specific ancestor is invoked first.


Q33. Which methods/functions do we use to determine the type of instance and inheritance?
Ans:
In Python, we can use the following methods/functions to determine the type of an instance and its inheritance:

type(): The type() function returns the type of an object. It can be used to determine the type of an instance. For example, type(obj) will return the class of obj.

isinstance(): The isinstance() function checks if an object is an instance of a particular class or a subclass thereof. It can be used to determine if an instance inherits from a specific class. For example, isinstance(obj, MyClass) will return True if obj is an instance of MyClass or any of its subclasses.

issubclass(): The issubclass() function checks if a class is a subclass of another class. It can be used to determine the inheritance relationship between classes. For example, issubclass(SubClass, BaseClass) will return True if SubClass is a subclass of BaseClass.

These methods/functions provide useful tools for type checking and determining the inheritance relationships in Python.
"""

Q34.Explain the use of the 'nonlocal' keyword in Python.
Ans:
The 'nonlocal' keyword in Python is used to indicate that a variable in a nested function should refer to the variable in the nearest enclosing scope, excluding the global scope. It allows modifying variables from the outer scope within the nested function, ensuring they are not treated as new local variables.

For example,

def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x += 5
        print("Inner function: x =", x)

    inner_function()
    print("Outer function: x =", x)

outer_function()


“””
In this example, the 'nonlocal' keyword is used in the inner_function to indicate that the variable 'x' being modified is the one from the outer_function's scope. Without 'nonlocal', modifying 'x' within the inner_function would create a new local variable, and the value of 'x' in the outer_function would remain unchanged.

By using 'nonlocal', the inner_function can access and modify the variable 'x' in the outer scope. The output of the example will be:
“”””
##########################OutPut##################################
Inner function: x = 15
Outer function: x = 15

"""

Q35. What is the global keyword?
Ans:

The 'global' keyword in Python is used to indicate that a variable defined within a function should be treated as a global variable, accessible throughout the entire program. It allows modifying global variables from within a function's local scope. The 'global' keyword is used to explicitly specify the scope of a variable to be global, avoiding the creation of a new local variable with the same name.



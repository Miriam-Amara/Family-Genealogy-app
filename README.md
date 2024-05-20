The family genealogy app is an app that allows users to register, create and view their family tree.
Currently, building the prototype with python OOP. It has four parts:
1. The registration part - completed
2. Login part - In progress
3. User profile
4. Admin part


Registration part:

This part has two modules Registration and init_reg
Registration.py contains 
one base class - Registration class and
Three subclasses - ChildRegistration class, MotherRegistration class and FatherRegistration class

The base class contains attributes common to the three subclasses. It initializes the instance attributes and sets their values to user input. It ensures that the input from user meets the requirement.

ChildRegistration class contains attributes specific to children registration. It sets the attributes to the input from user using the setter method. Then writes the information collected from the user to a file. 

MotherRegistration class contains attributes specific to registration of wives/mothers in a family. It sets attributes to the input from user using the setter method. Then writes the information to a file.

FatherRegistration class contains attributes specific to registration of fathers in a family. It sets the instance attributes to the input from the user. Then collects and writes the information to a file.


init_reg module imports Registration module. It has functions that initializes registration for children, mothers and fathers. When each function is called it prompts the user for input. The functions make sure the user inputs the correct value needed. If a user inputs a wrong value it displays a customized error and continues to prompt the user for the correct value.
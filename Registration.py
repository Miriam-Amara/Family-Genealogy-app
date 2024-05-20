import datetime
import os
import csv
import uuid

class Registration:
    """
    A base class for registering of users of family genealogy app.
    
    The Registration class serves as base class for the child, mother and father registration classes.
    It allows setting of the instance attributes to the values from users.
    It validates inputs from users and raises error if user input did not meet the requirements.
    
    Attributes:
        _firstname: The firstname of the user
        _middlename: The middlename of the user
        _lastname: The lastname of the user
        _gender: User's gender
        _birthdate: Date of birth of the user
    """
    
    def __init__(self):
        """
        Initializes the given instance attributes
        """
        self._firstname = None
        self._middlename = None
        self._lastname = None
        self._gender = None
        self._birthdate = None
    
    
    firstname = property()
    @firstname.setter
    def firstname(self, value):
        """
        Sets _firstname to the input from the user
        
        Args: 
            value: The input from the user
        """
        if not value or len(value) > 50:
            raise ValueError("invalid input")
        self._firstname = value
    
    
    middlename = property()
    @middlename.setter
    def middlename(self, value):
        """
        Sets _middlename to the input from the user
        
        Args: 
            value: The input from the user
        """
        if not value or len(value) > 50:
            raise ValueError("invalid input")
        self._middlename = value
    
    
    lastname = property()
    @lastname.setter
    def lastname(self, value):
        """
        Sets _lastname to the input from the user
        
        Args: 
            value: The input from the user
        """       
        if not value or len(value) > 50:
            raise ValueError("invalid input")
        self._lastname = value
    
    
    gender = property()
    @gender.setter
    def gender(self, value):
        """
        Sets _gender to the input from the user
        
        Args: 
            value: The input from the user
        """       
        if not value or value not in ['male', 'female']:
            raise ValueError("invalid input")
        self._gender = value
    
    
    birthdate = property()
    @birthdate.setter
    def birthdate(self, value):
        """
        Sets _birthdate to the input from the user
        
        Args: 
            value: The input from the user
        """       
        pass
        
        

        
        
        
class ChildRegistration(Registration):
    """
    A class to represent registration of children in the family genealogy app.
    
    Inherits from the Registration class, validates and set attributes specific to children registration.
    It also provides method to write information from users to the children_register.csv file
    
    Attributes:
        _fathername: The name of the child's father
        _mothername: The name of the child's mother
        _birthorder: The child's birth order in his family e.g first child, second child, ...
        _uid: The child's unique id
    """
    
    def __init__(self):
        """
        Initializes the base class attributes and the attributes of the ChildRegistration class
        """        
        super().__init__()
        self._fathername = None
        self._mothername = None
        self._birthorder = None
        self._uid = str(uuid.uuid4().fields[-1])[:6]
     
    
    fathername = property()
    @fathername.setter
    def fathername(self, value):
        """
        Sets _fathername to the input from the user
        
        Args: 
            value: The input from the user
        """        
        if not value or len(value) > 50:
            raise ValueError("invalid input")
        self._fathername = value
      
    
    mothername = property()
    @mothername.setter
    def mothername(self, value):
        """
        Sets _mothername to the input from the user
        
        Args: 
            value: The input from the user
        """        
        if not value or len(value) > 50:
            raise ValueError("invalid input")
        self._mothername = value
      
    
    birthorder = property()
    @birthorder.setter
    def birthorder(self, value):
        """
        Sets _birthorder to the input from the user
        
        Args: 
            value: The input from the user
        """       
        if not value or len(value) > 20:
            raise ValueError("invalid input")
        self._birthorder = value
        
    
    
    def write_data(self):
        """
        Writes the user's inputs to the children_register.csv file
        """       
        fieldnames = ("ID", "Firstname", "Middlename", "Lastname", "Gender", "Birthdate", "Father_name", "Mother_name", "Birth_order")
        data = {"ID": self._uid,
                "Firstname": self._firstname,
                "Middlename": self._middlename,
                "Lastname": self._lastname,
                "Gender": self._gender,
                "Birthdate": self._birthdate,
                "Father_name": self._fathername,
                "Mother_name": self._mothername,
                "Birth_order": self._birthorder}
        try:
            with open("children_register.csv", "a", newline = '') as cregister:
                writer = csv.DictWriter(cregister, fieldnames = fieldnames)
                if os.stat("children_register.csv").st_size > 0:
                    writer.writerow(data)
                else:
                    writer.writeheader()
                    writer.writerow(data)
        except Exception:
            Print("Registration not successful. Contact admin for support")
        else:
            print("Registration Successful!")






        
class MotherRegistration(Registration):
    """
    A class to represent registration of mothers/wives in the family genealogy app.
    
    Inherits from the Registration class, validates and set attributes specific to mothers registration.
    It also provides method to write information from users to the mothers_register.csv file
    
    Attributes:
        _husbandname: The name of the woman's husband
        _no_children: The number of children born by the woman
        _child_name: The name of each of her children
        _child_gender: The gender of each of her children
        _child_birthorder: The birth order of each of her children
        _child_status: The living status of each of her children e.g alive, dead, unknown
        _child_birthdate: Date of birth of each of her children
        _uid (str): The mother's unique id
    """
    
    def __init__(self):
        """
        Initializes the attributes of the base class and the attributes of MotherRegistration class
        """        
        super().__init__()
        self._husbandname = None
        self._no_children = None
        self._child_name = None
        self._child_gender = None
        self._child_birthorder = None
        self._child_status = None
        self._child_birthdate = None
        self._uid = str(uuid.uuid4().fields[-1])[:6]
    
    
    husbandname = property()
    @husbandname.setter
    def husbandname(self, value):
        """
        Sets husband name to the input from the user
        
        Args: 
            value: The input from the user
        """        
        if not value or len(value) > 50:
            raise ValueError("invalid input")
        self._husbandname = value
   

    @property
    def no_children(self):
        """
        Gets the no of children
        
        Returns:
            the no of children
        """        
        return self._no_children
    
    
    @no_children.setter
    def no_children(self, value):
        """
        Sets the number of children to the input from the user
        
        Args: 
            value (str): The input from the user
        """       
        if not value:
            raise ValueError("field cannot be empty")
        if value.isdigit() == False:
            raise ValueError("Invalid input. Only positive numbers are allowed")
        self._no_children = int(value)
   

    @property
    def child_name(self):
        """
        Gets the name of child
        
        Returns:
            The name of child
        """        
        return self._child_name
    
    
    @child_name.setter
    def child_name(self, value):
        """
        Sets child name to the input from the user
        
        Args: 
            value: The input from the user
        """        
        if not value or len(value) > 50:
            raise ValueError("invalid input")
        self._child_name = value
    
    
    child_gender = property()
    @child_gender.setter
    def child_gender(self, value):
        """
        Sets child's gender to the input from the user
        
        Args: 
            value: The input from the user
        """        
        if not value or value not in ['male', 'female']:
            raise ValueError("invalid input")
        self._child_gender = value
    
    
    
    child_birthorder = property()
    @child_birthorder.setter
    def child_birthorder(self, value):
        """
        Sets child birth order to the input from the user
        
        Args: 
            value: The input from the user
        """       
        if not value or len(value) > 20:
            raise ValueError("invalid input")
        self._child_birthorder = value
        
        
    child_status = property()
    @child_status.setter
    def child_status(self, value):
        """
        Sets child's status to the input from the user
        
        Args: 
            value: The input from the user
        """        
        if not value or value not in ['alive', 'deceased', 'unknown']:
            raise ValueError("invalid input")
        self._child_status = value
     
    
    child_birthdate = property()
    @child_birthdate.setter
    def child_birthdate(self, value):
        """
        Sets child date of birth to the input from the user
        
        Args: 
            value: The input from the user
        """        
        if not value:
            raise ValueError("invalid input")
        self._child_birthdate = value
        
        
    
    def write_data(self):
        """
        Writes the user's inputs to the mothers_register.csv file
        
        It opens the mothers_register.csv file and checks if the mother's unique id exists.
        If the unique id exists it appends only each child information to the next line.
        """       
        status = False
        file_path = "mothers_register.csv"
        fieldnames = ("ID", "Firstname", "Middlename", "Lastname", "Gender", "Birthdate", "Husbandname", "No of Children", "Child Name", "Child Gender", "Chlld Birthorder", "Status", "Child Birthdate")
        data1 = {"ID": self._uid,
                "Firstname": self._firstname,
                "Middlename": self._middlename,
                "Lastname": self._lastname,
                "Gender": self._gender,
                "Birthdate": self._birthdate,
                "Husbandname": self._husbandname,
                "No of Children": self._no_children,
                "Child Name": self._child_name,
                "Child Gender":self._child_gender,
                "Chlld Birthorder":self._child_birthorder,
                "Status":self._child_status,
                "Child Birthdate":self._child_birthdate}
        
        data1_items = list(data1.items())
        data2 = dict(data1_items[-5:13])
        
        try:
            if os.path.exists(file_path):
                with open("mothers_register.csv", "r", newline = '') as m:
                    reader = csv.DictReader(m)
                    for row in reader:
                        if self._uid in row.values():
                            status = True
                            break

            with open("mothers_register.csv", "a", newline = '') as mregister:
                writer = csv.DictWriter(mregister, fieldnames = fieldnames)
                if status == True:
                    writer.writerow(data2)
                else:
                    if os.stat("mothers_register.csv").st_size > 0:
                        writer.writerow(data1)
                    else:
                        writer.writeheader()
                        writer.writerow(data1)

        except Exception:
            print("Registration not successful. Contact admin for support")
        else:
            print("Registration successful!")

    
    
    
    
    
    
    
        
        
class FatherRegistration(Registration):
    """
    A class to represent registration of fathers in the family genealogy app.
    
    Inherits from the Registration class, validates and set attributes specific to fathers registration.
    It also provides method to write information from users to the fathers_register.csv file
    """    
    def __init__(self):
        super().__init__()
        self._no_children = None
        self._child_name = None
        self._child_gender = None
        self._child_status = None
        self._child_birthdate = None
        self._child_mother = None
        self._no_wife = None
        self._wife_name = None
        self._wife_hierarchy = None
        self._wife_status = None
        self._no_wifechildren = None
        self._wife_birthdate = None
        self._uid = str(uuid.uuid4().fields[-1])[:6]
        self._list_wife_info = []
        self._list_child_info = []
        
    @property
    def no_children(self):
        return self._no_children
    
    @no_children.setter
    def no_children(self, value):
        if not value:
            raise ValueError("field cannot be empty")
        if value.isdigit() == False:
            raise ValueError("Invalid input. Only positive numbers are allowed")
        self._no_children = int(value)

        
    @property
    def child_name(self):
        return self._child_name
    
    @child_name.setter
    def child_name(self, value):
        if not value or len(value) > 50:
            raise ValueError("invalid input")
        self._child_name = value

    
    child_gender = property()
    @child_gender.setter
    def child_gender(self, value):
        if not value or value not in ['male', 'female']:
            raise ValueError("invalid input")
        self._child_gender = value
    
    
    child_status = property()
    @child_status.setter
    def child_status(self, value):
        if not value or value not in ['alive', 'deceased', 'unknown']:
            raise ValueError("invalid input")
        self._child_status = value
    
    
    child_birthdate = property()
    @child_birthdate.setter
    def child_birthdate(self, value):
        if not value:
            raise ValueError("invalid input")
        self._child_birthdate = value
   

    child_mother = property()
    @child_mother.setter
    def child_mother(self, value):
        if not value or len(value) > 50:
            raise ValueError("invalid input")
        self._child_mother = value
        
        
    @property
    def no_wife(self):
        return self._no_wife
    
    @no_wife.setter
    def no_wife(self, value):
        if not value:
            raise ValueError("field cannot be empty")
        if value == '0':
            raise ValueError("invalid input")
        if value.isdigit() == False:
            raise ValueError("Invalid input. Only positive numbers are allowed")
        self._no_wife = int(value)
        
        
    @property
    def wife_name(self):
        return self._wife_name
    
    @wife_name.setter
    def wife_name(self, value):
        if not value or len(value) > 50:
            raise ValueError("invalid input")
        self._wife_name = value
     
    
    wife_hierarchy = property()
    @wife_hierarchy.setter
    def wife_hierarchy(self, value):
        if not value or len(value) > 30:
            raise ValueError("invalid input")
        self._wife_hierarchy = value
        
    wife_status = property()
    @wife_status.setter
    def wife_status(self, value):
        if not value or value not in ['alive', 'deceased', 'divorced', 'unknown']:
            raise ValueError("invalid input")
        self._wife_status = value
        
    
    @property
    def no_wifechildren(self):
        return self._no_wifechildren
    
    @no_wifechildren.setter
    def no_wifechildren(self, value):
        if not value:
            raise ValueError("Field cannot be empty. Please put in '0' if wife has no children")
        if value.isdigit() == False:
            raise ValueError("Invalid input. Only positive numbers are allowed")
        self._no_wifechildren = int(value)
        
    
    wife_birthdate = property()
    @wife_birthdate.setter
    def wife_birthdate(self, value):
        if not value:
            raise ValueError("invalid input")
        self._wife_birthdate = value
        
        
    
    def get_husband_info(self):
        """
        Gets the information of husband
        
        Returns:
            A dict containing information of the husband
        """
        return {
            "ID": self._uid,
            "Firstname": self._firstname,
            "Middlename": self._middlename,
            "Lastname": self._lastname,
            "Gender": self._gender,
            "Birthdate": self._birthdate,
            "No_of_wife": self._no_wife,
            "No_of_children": self._no_children
        }
    
    
    
    def get_wife_info(self):
        """
        Gets the information of wife/wives and appends it to the list _list_wife_info attribute
        
        Returns:
            A list of dict containing information of the wife/wives
        """        
        wife_info = {
            "Wife_name": self._wife_name,
            "Wife_hierarchy": self._wife_hierarchy,
            "Wife_status": self._wife_status,
            "No_of_wife_children": self._no_wifechildren,
            "Wife_birthdate": self._wife_birthdate
        }
        self._list_wife_info.append(wife_info)
    
    
    
    def get_child_info(self):
        """
        Gets the information of each child and appends it to the list _list_child_info attribute
        
        Returns:
            A list of dict containing information of children
        """        
        child_info = {
            "Child_name": self._child_name,
            "Child_gender": self._child_gender,
            "Child_status": self._child_status,
            "Child_birthdate": self._child_birthdate,
            "Child_mother": self._child_mother
        }
        self._list_child_info.append(child_info)
    
    
    def write_data(self):
        """
        Writes the user's inputs to the fathers_register.csv file
        
        It merges husband info (from get_husband_info method), wives info (from _list_wif_info attribute), and
        children info (from _list_child_info attribute) and write them to the fathers_register.csv file
        """        
        husband_info = self.get_husband_info()
        wife_info = self._list_wife_info
        child_info = self._list_child_info
#         print(husband_info)
#         print(f"\n{wife_info}")
#         print(f"\n{child_info}")
        max_length = max(self._no_wife, self._no_children)
        min_length = min(self._no_wife, self._no_children)
        fieldnames = ["ID", "Firstname", "Middlename", "Lastname", "Gender", "Birthdate", "No_of_wife", "Wife_name", "Wife_hierarchy", "Wife_status", "No_of_wife_children", "Wife_birthdate", "No_of_children","Child_name", "Child_gender", "Child_status", "Child_birthdate", "Child_mother"]

        
        try:
            with open("fathers_register.csv", "a", newline = '') as fregister:
                writer = csv.DictWriter(fregister, fieldnames = fieldnames)
                if os.stat("fathers_register.csv").st_size == 0:
                    writer.writeheader()
            
        
            with open("fathers_register.csv", "a", newline = '') as fregister:
                writer = csv.DictWriter(fregister, fieldnames = fieldnames)
                if self._no_children == 0:
                    for num in range(self._no_wife):
                        if num == 0:
                            merged_data = {**husband_info, **wife_info[num]}
                            writer.writerow(merged_data)
                        else:
                            writer.writerow(**wife_info[num])
                else:
                    for i in range(max_length):
                        if min_length == self._no_wife:
                            if i == 0:
                                merged_data = {**husband_info, **wife_info[i], **child_info[i]}
                                writer.writerow(merged_data)
                            elif i < min_length:
                                merged_data = {**wife_info[i], **child_info[i]}
                                writer.writerow(merged_data)
                            else:
                                writer.writerow(child_info[i])

                        elif min_length == self._no_children:
                            if i == 0:
                                merged_data = {**husband_info, **wife_info[i], **child_info[i]}
                                writer.writerow(merged_data)
                            elif i < min_length:
                                merged_data = {**wife_info[i], **child_info[i]}
                                writer.writerow(merged_data)
                            else:
                                writer.writerow(wife_info[i])
        except Exception:
            print("Registration not successful. Contact admin for support")
        else:
            print("Registration successful!")
            
            
            
            
            
            
            
            
            
            
            
            
            
            


def initialize_child_reg(child):
    """
    This function gets inputs from users (children) and passes each input to the corresponding setter method in the 
    ChildRegistration class.
    
    If the setter method raises an error it will continue to prompt the user to enter the correct value.
    It calls the write_data method in the ChildRegistration class to write the user's information to children_register.csv file. 
    
    Args:
        child: An instance of the ChildRegistration class
    """
    c_info = ['firstname', 'middlename', 'lastname', 'gender', 'birthdate', 'fathername', 'mothername', 'birthorder']
    for data in c_info:
        while True:
            try:
                if data == 'firstname':
                    child.firstname = input("Enter your firstname: ").lower()
                elif data == 'middlename':
                    child.middlename = input("Enter your middlename: ").lower()
                elif data == 'lastname':
                    child.lastname = input("Enter your lastname: ").lower()
                elif data == 'gender':
                    child.gender = input("What's your gender (male/female): ").lower()
                elif data == 'birthdate':
                    child.birthdate = input("Enter your date of birth: ")
                elif data == 'fathername':
                    child.fathername = input("Enter your father's fullname: ").lower()
                elif data == 'mothername':
                    child.mothername = input("Enter your mother's fullname: ").lower()
                elif data == 'birthorder':
                    child.birthorder = input("What is your birth order e.g first child: ").lower()
                break
            except ValueError as e:
                print(e)
    child.write_data()
    

    
def initialize_mother_reg(mother):
    """
    This function gets inputs from users (mothers) and passes each input to the corresponding setter method in the 
    MotherRegistration class.
    
    If the setter method raises an error it will continue to prompt the user to enter the correct value.
    It calls the write_data method in the MotherRegistration class to write the user's information to mothers_register.csv file. 
    
    Args:
        mother: An instance of the MotherRegistration class
    """
    m_info = ['firstname', 'middlename', 'lastname', 'gender', 'birthdate', 'husbandname', 'no_children']
    for m_data in m_info:
        while True:
            try:
                if m_data == 'firstname':
                    mother.firstname = input("Enter your firstname: ").lower()
                elif m_data == 'middlename':
                    mother.middlename = input("Enter your middlename: ").lower()
                elif m_data == 'lastname':
                    mother.lastname = input("Enter your lastname: ").lower()
                elif m_data == 'gender':
                    mother.gender = input("What's your gender (male/female): ").lower()
                elif m_data == 'birthdate':
                    mother.birthdate = input("Enter your date of birth: ")
                elif m_data == 'husbandname':
                    mother.husbandname = input("Enter your husband's fullname: ").lower()
                elif m_data == 'no_children':
                    mother.no_children = input("How many children do you have? e.g 1, 2, 3,...: ")
                break
            except ValueError as e:
                print(e)
    
    child_info = ["childname", "child_gender", "child_birthorder", "childstatus", "child_birthdate"]
    if mother.no_children > 0:
        for i in range(1, mother.no_children + 1):
            for c_data in child_info:
                while True:
                    try:
                        if c_data == "childname":
                            mother.child_name = input(f"\nEnter the fullname of your '{i}' child: ").lower()
                        elif c_data == "child_gender":
                            mother.child_gender = input(f"Is {mother.child_name} male or female? ").lower()
                        elif c_data == "child_birthorder":
                            mother.child_birthorder = input("What is your child's birthorder? e.g first child, second child, etc: ").lower()
                        elif c_data == "childstatus":
                            mother.child_status = input(f"Is {mother.child_name} alive, deceased or unknown? ").lower()
                        elif c_data == "child_birthdate":
                            mother.child_birthdate = input(f"Enter {mother.child_name}'s date of birth: ")
                        break
                    except ValueError as e:
                        print(e)
            mother.write_data()
    else:
        mother.write_data()
                        
                        
                
def initialize_father_reg(father):
    """
    This function gets inputs from users (fathers) and passes each input to the corresponding setter method in the 
    FatherRegistration class.
    
    If the setter method raises an error it will continue to prompt the user to enter the correct value.
    It calls the write_data method in the FatherRegistration class to write the user's information to fathers_register.csv file. 
    
    Args:
        father: An instance of the FatherRegistration class
    """
    def father_info():
        f_info = ['firstname', 'middlename', 'lastname', 'gender', 'birthdate', 'no_children', 'no_wife']
        for f_data in f_info:
            while True:
                try:
                    if f_data == 'firstname':
                        father.firstname = input("Enter your firstname: ").lower()
                    elif f_data == 'middlename':
                        father.middlename = input("Enter your middlename: ").lower()
                    elif f_data == 'lastname':
                        father.lastname = input("Enter your lastname: ").lower()
                    elif f_data == 'gender':
                        father.gender = input("Are you male/female? ").lower()
                    elif f_data == 'birthdate':
                        father.birthdate = input("Enter your date of birth: ")
                    elif f_data == 'no_children':
                        father.no_children = input("How many children do you have? Enter a number: ")
                    elif f_data == 'no_wife':
                        father.no_wife = input("How many wife/wives do you have? Enter a number: ")
                    break
                except ValueError as e:
                    print(e)

    def wife_info():           
        wife_info = ['wife_name', 'wife_hierarchy', 'wife_status', 'no_wifechildren', 'wife_birthdate']
        for n in range(1, father.no_wife + 1):
            for val in wife_info:
                while True:
                    try:
                        if val == 'wife_name':
                            father.wife_name = input(f"\nEnter the fullname of your '{n}' wife: ").lower()
                        elif val == 'wife_hierarchy':
                            if father.no_wife > 1:
                                father.wife_hierarchy = input(f"Enter her hierarchy as in... is {father.wife_name} your first wife/second wife etc? ")
                        elif val == 'wife_status':
                            father.wife_status = input(f"Is {father.wife_name} alive/deceased/divorced/unknown? ").lower()
                        elif val == 'no_wifechildren':
                            father.no_wifechildren = input(f"How many children does {father.wife_name} have? Enter a no.: ")
                        elif val == 'wife_birthdate':
                            father.wife_birthdate = input(f"Enter {father.wife_name} date of birth: ")
                        break
                    except ValueError as e:
                        print(e)
            father.get_wife_info()

    def children_info():           
        children_info = ['child_name', 'child_gender', 'child_status', 'child_birthdate', 'child_mother']
        if father.no_children > 0:
            for num in range(1, father.no_children + 1):
                for value in children_info:
                    while True:
                        try:
                            if value == 'child_name':
                                father.child_name = input(f"\nEnter the fullname of your '{num}' child: ").lower()
                            elif value == 'child_gender':
                                father.child_gender = input(f"what is your child's gender? male/female: ").lower()
                            elif value == 'child_status':
                                father.child_status = input(f"Is {father.child_name} alive, deceased, or unknown? ").lower()
                            elif value == 'child_birthdate':
                                father.child_birthdate = input(f"Enter {father.child_name}'s date of birth: ")
                            elif value == 'child_mother':
                                if father.no_wife > 1:
                                    father.child_mother = input(f"Enter {father.child_name}'s mother's fullname: ")
                            break
                        except ValueError as e:
                            print(e)
                father.get_child_info()

    father_info()
    wife_info()
    children_info()
    father.write_data()
    
    
    
    
if __name__ == "__main__": 
    """Initializes registration for children in the family"""  
    child = ChildRegistration()
    initialize_child_reg(child)
    
    """Initializes registration for mothers in the family"""
    mother = MotherRegistration()
    initialize_mother_reg(mother)
    
    """Initializes registration for fathers in the family"""
    father = FatherRegistration()
    initialize_father_reg(father)

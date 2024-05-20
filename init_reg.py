import Registration


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
    child = Registration.ChildRegistration()
    initialize_child_reg(child)
    
    """Initializes registration for mothers in the family"""
    mother = Registration.MotherRegistration()
    initialize_mother_reg(mother)
    
    """Initializes registration for fathers in the family"""
    father = Registration.FatherRegistration()
    initialize_father_reg(father)

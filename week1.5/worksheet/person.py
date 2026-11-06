# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a person, given values for name and birthday
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name == "":
            raise ValueError("name must not be an empty string")
        if not isinstance(birth, date):
            raise ValueError("birth must be a date")

            
    def initials(self):
        #space_1 = self.name.contains(" ")
        #substring = self.name.substring()
        #space_2 = substring.contains(" ")
        #subsubstring = self.name.substring()
        #space_3 = subsubstring.contains(" ")
        #firstname = self.name.substring(0,space_1)
        #first_initial = firstname(1)
        #secondname = self.name.substring(space_2,space_3)
        #thirdname = self.name.substring(space_3,self.name.length)
        #second_initial = secondname(1)
        #third_initial = thirdname(1)
        #initials = first_initial+second_initial+third_initial
        #return initials
        #//////////////////////////////////////////
        #much more siccinct way to do it, looked over python comands for strings again
        return "".join(word[0].upper() for word in self.name.split())

    def is_birthday(self):
        today = date.today()
        return (today.month, today.day) == (self.birth.month, self.birth.day) 
 

        

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

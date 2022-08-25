class Employee:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname


    def getName(self):
         return self.firstname[0]+self.lastname[0]

emp = Employee("nithish", "alakunta")
name=emp.getName();
print(name.upper())
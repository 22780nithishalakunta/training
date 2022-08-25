from employee import Employee
from address import Address
address1=Address("banglore")
address2=Address("hyderabad")

emp1=Employee("Nithish","Alakunta","gudur")
emp2=Employee("Nithish","Alakunta",[address1,address2])
print(address1.display_address())
print(address2.display_address())
print(emp1.display())
print(emp2.display())
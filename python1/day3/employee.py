class Employee:
    def __init__(self,fname,lname,address):
        self.fname=fname
        self.lname=lname
        self.address=address
    def display(self):
        return self.fname[0].upper()+""+self.lname[0].upper(),self.address


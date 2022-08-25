from leave import Leave
class RestrictedLeave(Leave):
    def __init__(self,Employeeid,Name,LeaveBalance,DateOfBirth):
        super().__init__(Employeeid,Name,LeaveBalance)
        self.dob=DateOfBirth
    def display_dob(self):
        return self.dob



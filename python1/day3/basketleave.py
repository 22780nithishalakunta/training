from leave import Leave
class BasketOfLeave(Leave):
    def __init__(self, Employeeid, Name, LeaveBalance, Applyingleave):
        super().__init__(Employeeid,Name,LeaveBalance)
        self.Applyingleave=Applyingleave

    def displayleave(self):
        return self.Applyingleave


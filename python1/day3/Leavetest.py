from leave import Leave
from basketleave import BasketOfLeave
from restrictedleave import RestrictedLeave
r1=RestrictedLeave(22780,"Nithish Alakunta",25,2000-10-30)
b1=BasketOfLeave(22780,"Nithish Alakunta",25,"Sick Leave")
print(b1.display())
print(b1.displayleave())
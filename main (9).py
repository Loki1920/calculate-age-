#calculate age
from datetime import date
dob = date(2000,4,8)
t = date.today()
age = t.year - dob.year - ((t.month,t.day)<(dob.month,dob.day)) 

print(age)
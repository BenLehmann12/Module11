'''
Author:Ben Lehmann
Date Modified: 11/8-11/9
Function: One function will return salary per year, with date and Name, the other will return hourly salary, name and year
'''
from datetime import datetime
class Employee:   #Base
    # Constructor
     def __init__(self, lname, fname):  #Call Back
         self._last_name = str(lname)
         self._first_name = str(fname)

     def set_last_name(self, lname):
         self._last_name = lname
     def set_first_name(self, fname):
         self._first_name = fname

     def display(self):
         return str(self._first_name) +" " + str(self._last_name)

     def __str__(self):
         return str(self._first_name) + " " + str(self._last_name)


class SalariedEmployee(Employee):
    def __init__(self, lname, fname,start_date,salary):  #Call Name
        super().__init__(fname,lname)
        self._start_date = start_date
        self._salary = salary

    def give_raise(self,incr_salary):  #Add to Salary
        self._salary += incr_salary

    def display(self):
        return str(Employee.display(self)) + ", " + str(self._start_date) + "," + str(self._salary)
    def __str__(self):
        return str(Employee.display(self)) + ", " + str(self._start_date) + "," + str(self._salary)

day = datetime.now()
emp = SalariedEmployee('Lehmann','Ben', day.strftime("%x"), 40000)
emp.give_raise(5000)
print(emp.display())

class HourlyEmployee(Employee):
    def __init__(self, lname, fname,start_date,hourly_pay):
        super().__init__(fname,lname)
        self._start_date = start_date
        self._hourly_pay = hourly_pay
    def give_rase(self,price_incr):
        self._hourly_pay += price_incr  #Add to Hourly

    def display(self):
        return str(Employee.display(self)) + ", " + str(self._start_date) + "," + str(self._hourly_pay)
    def __repr__(self):
        return str(Employee.display(self)) + ", " + str(self._start_date) + "," + str(self._hourly_pay)


day = datetime.now()
emp = HourlyEmployee('Lehmann','Ben', day.strftime("%x"), 12.00)
print(emp.display())


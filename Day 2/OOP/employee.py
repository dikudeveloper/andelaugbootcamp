from abc import ABCMeta, abstractmethod

#################################################################################################
# A Class representing Employees of an organization to illustrate their earnings
# Employees may earn a Salary, Commission, or both
# Practical application: Payment of wages in any organization that pays Salary, and Commission
#####


class Employee(object):
    """An Employee of an organization that pays wages in form of Salary or Commission or both
    ---- This is an Abstract Super Class ----

    Private Attributes (Should only be accessed within this Class):
        __first_name: Employee's first name
        __last_name: Employee's last name
        __employee_id: Employee's ID number
    """

    # designs Employee to be an Abstract Base Class
    # Implication: You cannot create an Instance of this Class. It is only meant to be Inherited from
    __metaclass__ = ABCMeta

    def __init__(self, first, last, employeeid):
        """constructor to initialize an object of this class"""
        self.__first_name = first
        self.__last_name = last
        self.__employee_id = employeeid

    # set first_name
    def set_first_name(self, first):
        """Set the Employee's first name"""
        self.__first_name = first

    # get first_name
    def get_first_name(self):
        """Return the Employee's first name"""
        return self.__first_name

    # set last_name
    def set_last_name(self, last):
        """Set the Employee's last name"""
        self.__last_name = last

    # get last_name
    def get_last_name(self):
        """Return the Employee's last name"""
        return self.__last_name

    # set employee_id
    def set_employee_id(self, employeeid):
        """Set the Employee's Id"""
        self.__employee_id = employeeid

    # get employee_id
    def get_employee_id(self):
        """Return the Employee's Id"""
        return self.__employee_id

    # An abstract Method to be overidden by subclasses
    @abstractmethod
    def employee_earnings(self):
        """"Return the earnings of an Employee."""
        pass

    # return the String representation of Employee object
    def __repr__(self):
        return "({} {}: Employee ID: {})".\
            format(self.get_first_name(), self.get_last_name(), self.get_employee_id())

from employee import Employee


class SalaryEmployee(Employee):
    """A Salary Employee of an organization
    --- SalaryEmployee extends abstract class Employee ---

    Private Attributes:
    __monthly_salary: salary earned by a SalaryEmployee
    """

    def __init__(self, first, last, employeeid, salary):
        """ Invoke the base class constructor to initialize __first_name, __last_name, __employee_id
        salary: monthly salary earned by a SalaryEmployee
        """
        super().__init__(first, last, employeeid)
        self.set_monthly_salary(salary)

    # set salary
    def set_monthly_salary(self, salary):
        if salary < 0:
            self.__monthly_salary = 0
        self.__monthly_salary = salary

    # get salary
    def get_monthly_salary(self):
        return self.__monthly_salary

    # Calculate earnings -- override abstract method, earnings, in Base class
    def employee_earnings(self):
        return self.get_monthly_salary()

    # return a String representation of a SalaryEmployee object
    def __repr__(self):
        return "(Salary Employee: {}\nMonthly Salary: {})".format(super().__repr__(), self.get_monthly_salary())




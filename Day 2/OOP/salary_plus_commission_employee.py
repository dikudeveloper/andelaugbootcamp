from commission_employee import CommissionEmployee


class SalaryPlusCommission(CommissionEmployee):
    def __init__(self, first, last, employeeid, sales, rate, salary):
        super().__init__(first, last, employeeid, sales, rate)
        self.set_monthly_salary(salary)

    def set_monthly_salary(self, salary):
        if salary < 0:
            self.__monthly_salary = 0
        self.__monthly_salary = salary

    def get_monthly_salary(self):
        return self.__monthly_salary

    def employee_earnings(self):
        self.get_monthly_salary() + super().employee_earnings()

    def __repr__(self):
        return "Salary plus commission employee %s; Salary plus commission: %.3f" % \
               (super().__repr__(), self.get_monthly_salary())

from employee import Employee


class CommissionEmployee(Employee):
    """A Commission Employee of an organization

    Attributes:
        total_sales: total sales made by this Employee during the month
        __commission_rate: commission per sale made by this Employee during the month
    """

    def __init__(self, first, last, employeeid, sales, rate):
        super().__init__(first, last, employeeid)
        self.set_total_sales(sales)
        self.set_commission_rate(rate)

    # set commission rate -- rate is between 0 to 100%
    def set_commission_rate(self, rate):
        if rate>0.0 and rate <=1.0:
            self.__commission_rate = rate
        else:
            self.__commission_rate = 0.0

    # get commission rate
    def get_commission_rate(self):
        return self.__commission_rate

    # set total sales amount
    def set_total_sales(self, sales):
        if sales < 0:
            self.__total_sales = 0
        self.__total_sales = sales

    # get total sales amount
    def get_total_sales(self):
        return self.__total_sales

    # Calculate earnings -- override abstract method, earnings, in Base class
    def employee_earnings(self):
        return self.get_commission_rate() * self.get_total_sales()

    # return a String representation of a SalaryEmployee object
    def __repr__(self):
        return "Commission Employee: {}\nTotal Sales: {}; Commission Rate: {}"\
            .format(super().__repr__(), self.get_total_sales(), self.get_commission_rate())

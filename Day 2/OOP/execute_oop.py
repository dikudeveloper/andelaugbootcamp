from employee import Employee
from salary_employee import SalaryEmployee
from commission_employee import CommissionEmployee
from salary_plus_commission_employee import SalaryPlusCommission


# Implementation of Object Oriented Programming Concepts:
# ----- Inheritance, Encapsulation, Abstraction, and Polymorphism ------

def main():
    salary_employee = SalaryEmployee('Joseph', 'Diku', 1, 1000)
    commission_employee = CommissionEmployee('Lawrence', 'Mr. Moustache', 100, 20, 0.01)
    salary_plus_commission_employee = SalaryPlusCommission('Henry', 'Mukasa', 5, 50, 0.2, 500)
    print('Employees when individually processed:')
    print("{}\nearning {:.3f}\n\n".format(salary_employee, salary_employee.employee_earnings()))
    print("{}\nearning {:.3f}\n\n".format(commission_employee, commission_employee.employee_earnings()))
    # print("{:f}\nearning {:.3f}\n\n".format(salary_plus_commission_employee, salary_plus_commission_employee.employee_earnings()))

    # Now process Employees polymorphically
    employees = [salary_employee, commission_employee, salary_plus_commission_employee]
    print('Employees when Polymorphically processed:')

    for current_employee in employees:
        print(current_employee)
        if isinstance(current_employee, SalaryPlusCommission):
            salarypluscommissionemployee = current_employee
            salarypluscommissionemployee.set_monthly_salary(1.20 * salarypluscommissionemployee.get_monthly_salary())
            print('Earnings with a 20 percent increment: %f' % salarypluscommissionemployee.get_monthly_salary())
    print('Earnings: {}'.format(current_employee.employee_earnings()))

    # Get Type name for each object in the employees list
    count = 0
    is_True = False
    while count < len(employees):
        print("Employee %d is a %s\n" % (count, employees[count]))
        count += 1

if __name__ == '__main__':
    main()





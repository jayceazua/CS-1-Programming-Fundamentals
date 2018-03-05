# Group our data to reuse

class Employee:
    # class variables - shared among all employees
    raise_amt = 1.04
    num_of_emps = 0
    # by default this is needed init method...
    def __init__(self, first, last, pay):
        # here are instance variables - can be unique
        self.first = first
        self.last = first
        self.pay = pay
    # keeps tract of how many instances it was created
        Employee.num_of_emps += 1
    # always put self when creating methods
    @property
    def email(self):
        return '{}.{}'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

        # special methods -- dunders
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.firstname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay
    # Decorators

    @classmethod # working with class methods cls is like passing self
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt

    @classmethod # alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    # check if you are using either cls or self it not use a static.
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# creating subclasses
# Developers - instantiated: represent as or by an instance also known as construction
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # super() does not work for inheritance - creating subclasses
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __len__(self):
        return len(self.fullname())

# Managers
class Manager(Employee):
    def __init__(self, fist, last, pay, employees=None):
        # super() does not work for inheritance - creating subclasses
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# dunder _ _ special method _ _
# look under the hood and how special methods work.
repr()
# unambigious and used for debugging for other developers
str()
# readable representation and display for the end user

print(isinstance())
print(issubclass())

dev_1 = Developer('Jayce', 'Azua', 94000, "Python")

print(dev_1.pay)
dev_1.apply_raise()

print(dev_1.prog_lang)

print(1+2)

print(int.__add__(1,2))
print(str.__str__('a', 'b'))
print('Hello'.__len__()) # same ass len('Hello')

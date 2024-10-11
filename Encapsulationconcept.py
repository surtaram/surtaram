# Encapsulation

class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public member
        self._department = 'IT'  # Protected Member
        self.__salary = salary  # private member

    # Public method to access private vatiable
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary amount!")


emp = Employee("John", 50000)

print(emp.name)
print(emp._department)


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit amount is {amount} and updated balance is {self.__balance}")
        else:
            print("Amound cannot be negative")

    def withdraw(self, amount):
        if 0 < amount >= self.__balance:
            self.__balance -= amount
            print(f"withdraw amound is {amount} and updated balance is {self.__balance}")
        else:
            print("Please enter valid amount")

obj=BankAccount("12345",9000)
obj.deposit(9000)
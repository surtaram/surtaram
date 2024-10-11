myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32, "dadsa": 45, "Dasdadsa": 24224,
          "saasa": 31414}

sorted_dict_key = {key: value for key, value in sorted(myDict.items(), key=lambda myDict: myDict[0])}
print(sorted_dict_key)


# polymorphism :-


class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog Barks")


class Cat(Animal):
    def sound(self):
        print("Cat Meows")


animal = Animal()
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()
animal.sound()


# Encapsulation

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit amount is {amount},New balance is {self.__balance}")
        else:
            print("Amount must positive")

    def withdrawl(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw amount is {amount},New balanace is {self.__balance}")
        else:
            print("Amount must be less the current balance ")

my_account=BankAccount("123434",4000)
print("Account number:",my_account.account_number)
my_account.deposit(3000)
my_account.withdrawl(9000)
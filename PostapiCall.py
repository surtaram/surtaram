class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Full_time_employee(Employee):
    def calculate_salary(self):
        bonus = self.base_salary * 0.5
        return self.base_salary + bonus


class Part_time_employee(Employee):
    def calculate_salary(self):
        hours = 80
        hourly_rated = self.base_salary // 160
        return hours * hourly_rated


if __name__ == "__main__":
    emp1 = Full_time_employee("jogger", 9000)
    print(emp1.calculate_salary())
    emp2 = Part_time_employee("ramesh", 10000)
    print(emp2.calculate_salary())


# multilevel
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Makes sounds")


class Mammles(Animal):
    def has_hair(self):
        return True


class Dog(Mammles):
    def speak(self):
        print(f"{self.name} barks")


# multiple

class Animal1:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Sound")


class Canine:
    def run(self):
        print(f"{self.name} runs.")


class Dog1(Animal, Canine):
    def speak(self):
        print(f"{self.name} barks")


dog = Dog1("Doggy")
dog.run()
dog.speak()

d1 = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
#
# key=list(d1.keys())
# key.sort()
# print(key)
#
# sorted_dict_key={i:d1[i] for i in key}
# print(sorted_dict_key)

sorted_value = {key: value for key, value in sorted(d1.items(), key=lambda d1: d1[1])}

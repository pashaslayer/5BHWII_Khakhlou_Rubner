from enum import Enum

"""
programmiere in Python:

- eine Firma
- Es gibt Personen, Mitarbeiter, Abteilungsleiter
- Es gibt mehrere Abteilungen, jede Mitarbeiter ist in einer Abteilung
- Es gibt beide Geschlechter

- modelliere die Objekte über Vererbung
- erzeuge zum Schluss ein Firmenobjekt

 biete folgende Methoden an:
 - man muss alle Objekte instanzieren können
 - wieviele Mitarbeiter, Gruppenleiter gibts in der Firma
 - wieviel Abteilungen gibt es
 - welche Abteilung hat die größte Mitarbeiterstärke
 - wie ist der Prozentanteil Frauen Männer

Maximiere die Logik-Kapselung...Methoden und Datenstrukturen sollten in den passenden Klassen implementiert werden.
"""


class Gender(Enum):
    MALE = 1
    FEMALE = 2


class Person:
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender


class Employee(Person):
    def __init__(self, firstname, lastname, gender, salary):
        super().__init__(firstname, lastname, gender)
        self.salary = salary


class DepartmentChief(Person):
    def __init__(self, firstname, lastname, gender, salary):
        super().__init__(firstname, lastname, gender)
        # Als Unterschied zu einem Employee wird sein Gehalt um 50% erhöht
        self.salary = salary * 1.50


class Department:
    def __init__(self, name):
        self.name = name
        self.chiefs = []
        self.employees = []

    def get_employees_and_chiefs_amount(self):
        return len(self.employees), len(self.chiefs)

    def get_female_male_percentage(self):
        total = len(self.employees)
        males = 0
        for x in self.employees:
            if x.gender == Gender.MALE:
                males += 1

        male_percentage = males / total
        female_percentage = (total-males) / total

        print("")
        print(self.name)
        print(f"Males: {male_percentage:.0%}")
        print(f"Females: {female_percentage:.0%}")


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.departments = []

    def get_total_employees_and_chiefs(self):
        total_employees = 0
        total_chiefs = 0
        for department in self.departments:
            employees, chiefs = department.get_employees_and_chiefs_amount()
            total_employees += employees
            total_chiefs += chiefs

        return total_employees, total_chiefs

    def get_department_count(self):
        return len(self.departments)

    def get_biggest_department(self):
        return max(self.departments, key=lambda d: len(d.employees))


employee1 = Employee("Ivan", "Worker", Gender.MALE, 1540.50)
employee2 = Employee("Markus", "Worker", Gender.MALE, 1450.90)
employee3 = Employee("Lopez", "Worker", Gender.MALE, 1260.40)
employee4 = Employee("Supra", "Worker", Gender.MALE, 1845.45)
employee5 = Employee("Maya", "Worker", Gender.FEMALE, 1333.30)
employee6 = Employee("Rita", "Worker", Gender.FEMALE, 1780.50)

chief1 = DepartmentChief("Manuel", "Chief", Gender.MALE, 1780.50)
chief2 = DepartmentChief("Lena", "Chief", Gender.FEMALE, 1800.00)
chief3 = DepartmentChief("Matilda", "Chief", Gender.FEMALE, 1800.00)


department_supply = Department("supply management")
department_production = Department("production")
department_sales = Department("sales department")

department_supply.employees.append(employee1)
department_supply.employees.append(employee2)
department_supply.chiefs.append(chief1)


department_production.employees.append(employee3)
department_production.employees.append(employee4)
department_production.employees.append(employee5)
department_production.chiefs.append(chief2)


department_sales.employees.append(employee6)
department_sales.chiefs.append(chief1)
department_sales.chiefs.append(chief3)


company = Company("SportSpot")

company.departments.append(department_supply)
company.departments.append(department_production)
company.departments.append(department_sales)


#####################################################
# Wie viele Mitarbeiter, Gruppenleiter hat die Firma?
#####################################################
employees, chiefs = company.get_total_employees_and_chiefs()
print(f"Mitarbeiter: {employees}")
print(f"Abteilungsleiter: {chiefs}")

############################################
# Wie viele Abteilungen hat das Unternehmen?
############################################
departments = company.get_department_count()
print(f"Abteilungen: {departments}")

###################################################
# welche Abteilung hat die größte Mitarbeiterstärke
###################################################
biggest_department = company.get_biggest_department()
print(f"Größte Abteilung: {biggest_department.name}")

#########################################
# wie ist der Prozentanteil Frauen Männer
#########################################
department_production.get_female_male_percentage()
department_sales.get_female_male_percentage()
department_supply.get_female_male_percentage()

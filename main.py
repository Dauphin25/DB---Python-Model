from positions import Position
from employee import Employee
import random as rd

names = ["John", "Emma", "Michael", "Sophia", "James", "Olivia", "William", "Ava", "Alexander", "Isabella",
         "Daniel", "Mia", "Matthew", "Charlotte", "David", "Amelia", "Joseph", "Emily", "Andrew", "Samantha",
         "Benjamin", "Ella", "Christopher", "Madison", "Joshua", "Abigail", "Ethan", "Grace", "Ryan", "Avery"]

surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez",
            "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson",
            "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Lewis", "Robinson"]


def generate_employees():
    # Generate 30 random employees
    random_employees = []
    for _ in range(30):
        name = rd.choice(names)
        surname = rd.choice(surnames)
        age = rd.randint(18, 90)
        position = Position.get_random_position()
        employee = Employee(name, surname, age, position)
        random_employees.append(employee)

    return random_employees


if __name__ == '__main__':
    emp1 = Employee('john', 'Smith', 18, Position.JUNIOR_DEVELOPER)
    emp2 = Employee('Emma', 'Johnson', 25, Position.INTERN)
    emp3 = Employee('Michael', 'Williams', 30, Position.TECHNICAL_DEVELOPER)
    emp4 = Employee('Sophia', 'Brown', 28, Position.MIDDLE_DEVELOPER)
    emp5 = Employee('James', 'Jones', 35, Position.MIDDLE_DEVELOPER)
    emp6 = Employee('Olivia', 'Miller', 22, Position.INTERN)
    emp7 = Employee('William', 'Davis', 29, Position.JUNIOR_DEVELOPER)
    emp8 = Employee('Ava', 'Garcia', 27, Position.INTERN)
    emp9 = Employee('Alexander', 'Rodriguez', 32, Position.JUNIOR_DEVELOPER)
    emp10 = Employee('Isabella', 'Martinez', 26, Position.SENIOR_DEVELOPER)
    emp1.add_to_table()
    emp2.add_to_table()
    emp3.add_to_table()
    emp4.add_to_table()
    emp5.add_to_table()
    emp6.add_to_table()
    emp7.add_to_table()
    emp8.add_to_table()
    emp9.add_to_table()
    emp10.add_to_table()
    emp4.delete()
    print(emp5.calculate_annual_salary())
    print(emp5 > emp6)
    emp2.promote(Position.SENIOR_DEVELOPER)
    emp2.update()
    print(emp6.is_eligible_for_retirement())
    print(Employee.get_all())

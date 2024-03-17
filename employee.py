from positions import Position
from database import c


class Employee(object):

    counter = 0

    def __init__(self, name, surname, age, position):
        self.id = Employee.counter
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = position.value
        self.position = position.name
        Employee.counter += 1

    def __repr__(self):
        return "Employee id->{}, name->{}, surname->{}, age->{}, position->{}, salary->{}".format(
            self.id, self.name, self.surname, self.age,
            self.position, self.salary
        )

    def __lt__(self, other):
        if type(self) is type(other):
            return self.age < other.age
        else:
            return None

    def __gt__(self, other):
        if type(self) is type(other):
            return self.age > other.age
        else:
            return None

    def __eq__(self, other):
        if type(self) is type(other):
            return self.age == other.age
        else:
            return False

    @classmethod
    def get_employee(cls, pk):
        result = c.execute("SELECT * FROM employees WHERE employee_id = ?", (pk,))
        values = result.fetchone()

        if values is None:
            return None
        return Employee(values[1], values[2], values[3], Position.to_position(values[5]))

    @classmethod
    def get_all(cls):
        c.execute("SELECT * FROM employees")
        values = c.fetchall()
        return values

    @classmethod
    def filter_by(cls, **kwargs):

        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key}=?")
            values.append(value)

        where_clause = " AND ".join(conditions)
        query = f"SELECT * FROM employees WHERE {where_clause}"

        c.execute(query, tuple(values))
        rows = c.fetchall()

        employees = []
        for row in rows:
            # Assuming column indices for name, surname, age, position
            emp = Employee(row[1], row[2], row[3], Position.to_position(row[5]))
            emp.id = row[0]  # Assuming column index for employee_id
            employees.append(emp)

        return employees

    def add_to_table(self):
        c.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)", (
            self.id, self.name, self.surname, self.age, self.salary, self.position
        ))

    def delete(self):
        c.execute("DELETE FROM employees WHERE employee_id=?", (self.id,))

    def update(self):
        c.execute("UPDATE employees SET name=?, surname=?, age=?, salary=?, position=? WHERE employee_id=?", (
            self.id, self.name, self.surname, self.age, self.salary, self.position
        ))

    def calculate_annual_salary(self):
        return self.salary * 12

    def promote(self, new_position):
        self.position = new_position.name
        self.salary = new_position.value

    def demote(self, new_position):
        self.position = new_position.name
        self.salary = new_position.value

    def is_eligible_for_retirement(self):
        retirement_age = 65
        return self.age >= retirement_age

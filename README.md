# Employee Management System

This Python project is an Employee Management System that allows you to manage employees' information, such as their names, surnames, ages, positions, and salaries. The system is built with simplicity and flexibility in mind, making it easy to add, delete, update, and retrieve employee records.

## Features

- **Employee Class**: Defines the structure of an employee, including attributes like name, surname, age, position, and salary.
- **Position Enum**: Defines various positions within the company, with associated salary ranges.
- **SQLite Database**: Utilizes an SQLite database to store and manage employee records persistently.
- **CRUD Operations**: Supports basic CRUD (Create, Read, Update, Delete) operations for employee records.
- **Random Employee Generator**: Includes a function to generate random employee data for testing purposes.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. Additionally, ensure you have the following Python modules installed:

- `sqlite3`: SQLite database library
- `random`: Random number generation library

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/employee-management-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd employee-management-system
    ```

3. Run the project:

    ```bash
    python main.py
    ```

## Usage

The `main.py` file contains sample usage of the Employee Management System. You can modify and extend this file according to your specific requirements.

### Examples

```python
# Create employees
emp1 = Employee('John', 'Smith', 18, Position.JUNIOR_DEVELOPER)
emp2 = Employee('Emma', 'Johnson', 25, Position.INTERN)
...

# Add employees to the database
emp1.add_to_table()
emp2.add_to_table()
...

# Update an employee's information
emp2.promote(Position.SENIOR_DEVELOPER)
emp2.update()
...

# Retrieve all employees from the database
all_employees = Employee.get_all()
...

# Delete an employee from the database
emp4.delete()
...
```

## Contributors

- [Dauphin25]([https://github.com/Dauphin25)




"""
Create a sample class named Employee with two attributes id and name
employee :
    id
    name
object initializes id and name dynamically for every Employee object created.

emp = Employee(1, "coder")
"""

class Employee:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
    def print(self):
        print(self.id, self.name)

emp1 = Employee(1, "coder")
emp1.print()
del emp1.id
# Deleting the object itself
try:
    print(emp1.id)
except NameError:
    print("emp1.id is not defined")

del emp1
try:
    emp1.print()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")
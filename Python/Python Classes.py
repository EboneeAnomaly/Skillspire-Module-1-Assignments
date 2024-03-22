class MyClass:
    x = 10
# this is our class and what it contains.
newObject = MyClass()

print(newObject.x)
# in the above we ask the computer to unpack the information stored
# in 'newObject' by using .x. If you removed .x, it would show you the way
# that the computer sees our classes.

# An example of classes and passing the information to the classes
class Employee:
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department

Eliza = Employee(189823,100000,"COO")
Helen = Employee(188590, 150000, "CEO")

print("Eliza's ID: ", Eliza.ID)
print("Helen's ID: ", Helen.ID, Helen.salary)
Helen.printEmployeeInfo()


class Person:
    def __init__(self, Name, ID):
        self.Name = Name
        self.ID = ID
    def display(self):
        print(f"Name: {self.Name}, ID: {self.ID}")

class Employee(Person):
    def __init__(self, Name, ID, Salary, Post):
        super().__init__(Name, ID)
        self.Salary = Salary
        self.Post = Post

    def display2(self):
        print(f"Name: {self.Name}, ID: {self.ID}, Salary: {self.Salary}, Post: {self.Post}")


Anna_Smith = Person("Anna Smith", 100500)

Martin_Jones = Employee("Martin Jones", 100200, 150000, "Upper Management")

Anna_Smith.display()
Martin_Jones.display2()


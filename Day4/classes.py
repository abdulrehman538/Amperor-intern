                                                    #Class → creates → Objects
                                                    #Objects → contain → Attributes (data)
                                                    #Objects → use → Methods (behavior)
                                                    #Methods → access → Attributes using self

class students:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")
student1 = students("Abdul", 25, "Lahore")
student2 = students("Ali", 24, "Karachi")   
student1.display()



class staff:
    def __init__(self, id, name, department):
        self.id, self.name, self.department = id, name, department
    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Department: {self.department}")
a = staff(1, "sara", "HR")
b = staff(2, "John", "IT")
a.display()
b.display()

class Student:
    def __init__(self,name,age,year):
        self.name = name
        self.age = age
        self.year = year

    def show_details(self):
        print("The student details are: ")
        print(f"The name of the student is: {self.name}")
        print(f"The age of the student is: {self.age}")
        print(f"The year the student is in: {self.year}")

class School(Student):
    def __init__(self, name, age, year, sport, subject):
        super().__init__(name, age, year)
        self.sport = sport
        self.subject = subject

    def more_details(self):
        print(f"The students favourite sport is: {self.sport}" )
        print(f"The students favourite subject is: {self.subject}")


student1 = School("Bob","12","7","Football","P.E")
student1.show_details()
student1.more_details()


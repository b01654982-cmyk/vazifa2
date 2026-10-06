class StudentProfile:
    def __init__(self, name, age, grade,auid):
        self.name = name
        self.age = age
        self.grade = grade
        self.auid = auid

    def __str__(self) -> str:
        return f"Ism: {self.name}, Yoshi: {self.age}, Bosqich: {self.grade}, AUID :{self.auid}"




name = "Behruz"
age = 18
grade = 1
auid = "ABTAIM001"

person1 = StudentProfile(name,age,grade,auid)

print(person1)


class
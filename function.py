class StudentProfile:
    def __init__(self, name, age, grade,auid):
        self.name = name
        self.age = age
        self.grade = grade
        self.auid = auid

    def __str__(self) -> str:
        return f"Ism: {self.name}, Yoshi: {self.age}, Bosqich: {self.grade}, AUID :{self.auid}"




name = "Behruz"
age = 28
grade = 1
auid = "ABT26AIM001"

person1 = StudentProfile(name,age,grade,auid)

print(person1)

# 1. StudentProfile
class StudentProfile:
    def __init__(self, name, age, grade, auid):
        self.name = name
        self.age = age
        self.grade = grade
        self.auid = auid

    def __str__(self) -> str:
        return f"Ism: {self.name}, Yoshi: {self.age}, Bosqich: {self.grade}, AUID: {self.auid}"


person1 = StudentProfile("Ahrorjon", 22, 3, "ABT24CCS008")
print(person1)


# 2. Teacher
class Teacher:
    def __init__(self, name, subject, experience, salary):
        self.name = name
        self.subject = subject
        self.experience = experience
        self.salary = salary

    def __str__(self) -> str:
        return f"O'qituvchi: {self.name}, Fan: {self.subject}, Tajriba: {self.experience} yil, Maosh: {self.salary}"


teacher1 = Teacher("Behruz", "Python", 3, 5000000)
print(teacher1)


# 3. Book
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self) -> str:
        return f"Kitob: {self.title}, Muallif: {self.author}, Sahifa: {self.pages}, Narx: {self.price}"


book1 = Book("Python Basics", "Ali Valiyev", 250, 50000)
print(book1)


# 4. Car
class Car:
    def __init__(self, name, make, model, year):
        self.name = name
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"Ism: {self.name}, Marka: {self.make}, Model: {self.model}, Yil: {self.year}"


car1 = Car("Mening mashinam", "BMW", "M5", 2024)
print(car1)


# 5. Phone
class Phone:
    def __init__(self, brand, model, memory, price):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.price = price

    def __str__(self) -> str:
        return f"Brend: {self.brand}, Model: {self.model}, Xotira: {self.memory}, Narx: {self.price}"


phone1 = Phone("Infinix", "Hot 40", "256GB", 2000000)
print(phone1)


# 6. University
class University:
    def __init__(self, name, city, students, founded):
        self.name = name
        self.city = city
        self.students = students
        self.founded = founded

    def __str__(self) -> str:
        return f"Universitet: {self.name}, Shahar: {self.city}, Talabalar: {self.students}, Tashkil topgan: {self.founded}"


university1 = University("Acharya University", "Buxoro", 3000, 2024)
print(university1)


# 7. Laptop
class Laptop:
    def __init__(self, brand, processor, ram, storage):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def __str__(self) -> str:
        return f"Brend: {self.brand}, Processor: {self.processor}, RAM: {self.ram}, Xotira: {self.storage}"


laptop1 = Laptop("HP", "Intel Core i3", "8GB", "256GB SSD")
print(laptop1)


# 8. FootballPlayer
class FootballPlayer:
    def __init__(self, name, club, position, number):
        self.name = name
        self.club = club
        self.position = position
        self.number = number

    def __str__(self) -> str:
        return f"Futbolchi: {self.name}, Klub: {self.club}, Pozitsiya: {self.position}, Raqam: {self.number}"


player1 = FootballPlayer("Bellingham", "Real Madrid", "Midfielder", 5)
print(player1)


# 9. Movie
class Movie:
    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def __str__(self) -> str:
        return f"Kino: {self.title}, Janr: {self.genre}, Yil: {self.year}, Reyting: {self.rating}"


movie1 = Movie("Interstellar", "Sci-Fi", 2014, 8.7)
print(movie1)


# 10. BankAccount
class BankAccount:
    def __init__(self, owner, account_number, balance, currency):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    def __str__(self) -> str:
        return f"Egasi: {self.owner}, Hisob: {self.account_number}, Balans: {self.balance}, Valyuta: {self.currency}"


account1 = BankAccount("Behruz", "123456789", 1500000, "UZS")
print(account1)


# 11. Product
class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"Mahsulot: {self.name}, Kategoriya: {self.category}, Narx: {self.price}, Miqdor: {self.quantity}"


product1 = Product("Keyboard", "Computer", 250000, 10)
print(product1)


# 12. Employee
class Employee:
    def __init__(self, name, position, department, salary):
        self.name = name
        self.position = position
        self.department = department
        self.salary = salary

    def __str__(self) -> str:
        return f"Xodim: {self.name}, Lavozim: {self.position}, Bo'lim: {self.department}, Maosh: {self.salary}"


employee1 = Employee("Sardor", "Developer", "IT", 7000000)
print(employee1)


# 13. Animal
class Animal:
    def __init__(self, name, kind, age, color):
        self.name = name
        self.kind = kind
        self.age = age
        self.color = color

    def __str__(self) -> str:
        return f"Hayvon: {self.name}, Turi: {self.kind}, Yoshi: {self.age}, Rangi: {self.color}"


animal1 = Animal("Rex", "It", 3, "Qora")
print(animal1)


# 14. Computer
class Computer:
    def __init__(self, brand, cpu, ram, gpu):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu

    def __str__(self) -> str:
        return f"Kompyuter: {self.brand}, CPU: {self.cpu}, RAM: {self.ram}, GPU: {self.gpu}"


computer1 = Computer("ASUS", "Intel i7", "16GB", "RTX 4060")
print(computer1)


# 15. Game
class Game:
    def __init__(self, title, genre, platform, price):
        self.title = title
        self.genre = genre
        self.platform = platform
        self.price = price

    def __str__(self) -> str:
        return f"O'yin: {self.title}, Janr: {self.genre}, Platforma: {self.platform}, Narx: {self.price}"


game1 = Game("FC Mobile", "Football", "Android", 0)
print(game1)


# 16. Country
class Country:
    def __init__(self, name, capital, population, language):
        self.name = name
        self.capital = capital
        self.population = population
        self.language = language

    def __str__(self) -> str:
        return f"Mamlakat: {self.name}, Poytaxt: {self.capital}, Aholi: {self.population}, Til: {self.language}"


country1 = Country("Uzbekistan", "Tashkent", 38000000, "Uzbek")
print(country1)


# 17. Restaurant
class Restaurant:
    def __init__(self, name, food, address, rating):
        self.name = name
        self.food = food
        self.address = address
        self.rating = rating

    def __str__(self) -> str:
        return f"Restoran: {self.name}, Taom: {self.food}, Manzil: {self.address}, Reyting: {self.rating}"


restaurant1 = Restaurant("Osh Markazi", "Osh", "Buxoro", 4.8)
print(restaurant1)


# 18. ProgrammingCourse
class ProgrammingCourse:
    def __init__(self, name, language, duration, price):
        self.name = name
        self.language = language
        self.duration = duration
        self.price = price

    def __str__(self) -> str:
        return f"Kurs: {self.name}, Til: {self.language}, Davomiyligi: {self.duration}, Narx: {self.price}"


course1 = ProgrammingCourse("Python Backend", "Python", "6 oy", 1500000)
print(course1)
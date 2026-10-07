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

class Teacher:
    def __init__(self, name, age, subject, experience):
        self.name = Anna
        self.age = 25
        self.subject = Physics
        self.experience = yes

    def __str__(self):
        return f"O'qituvchi: {self.name}, Yoshi: {self.age}, Fan: {self.subject}, Tajriba: {self.experience} yil"


class Car:
    def __init__(self, brand, model, year, color):
        self.brand = BMW
        self.model = M5F90
        self.year = 2026
        self.color = BLACK

    def __str__(self):
        return f"Mashina: {self.brand} {self.model}, Yil: {self.year}, Rang: {self.color}"


class Book:
    def __init__(self, title, author, pages, price):
        self.title = JOURNEY
        self.author = BEHRZNUTFULLAYEV
        self.pages = 200
        self.price = 50
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"Kitob: {self.title}, Muallif: {self.author}, Sahifa: {self.pages}, Narx: {self.price} so'm"


class Phone:
    def __init__(self, brand, model, memory, price):
        self.brand = iPHONE
        self.model = 18
        self.memory = 512
        self.price = 1700

    def __str__(self):
        return f"Telefon: {self.brand} {self.model}, Xotira: {self.memory}GB, Narx: {self.price}$"


class Computer:
    def __init__(self, brand, processor, ram, storage):
        self.brand = LENOVO
        self.processor = COREI3
        self.ram = 12
        self.storage = 256

    def __str__(self):
        return f"Kompyuter: {self.brand}, CPU: {self.processor}, RAM: {self.ram}GB, SSD: {self.storage}GB"


class FootballPlayer:
    def __init__(self, name, age, club, position):
        self.name = RODRYGO
        self.age = 25
        self.club = REAL_MADRID
        self.position = RIGHT_WINGER

    def __str__(self):
        return f"Futbolchi: {self.name}, Yoshi: {self.age}, Klub: {self.club}, Pozitsiya: {self.position}"


class Country:
    def __init__(self, name, capital, population, continent):
        self.name = UZBEKISTAN
        self.capital = TASHKENT
        self.population = 40
        self.continent = SENTRAL_ASIA

    def __str__(self):
        return f"Davlat: {self.name}, Poytaxt: {self.capital}, Aholi: {self.population}, Qit'a: {self.continent}"


class University:
    def __init__(self, name, city, faculty, students):
        self.name = ACHARYA
        self.city = KARAKUL
        self.faculty = IT
        self.students = 1-GRADUTE

    def __str__(self):
        return f"Universitet: {self.name}, Shahar: {self.city}, Fakultet: {self.faculty}, Talabalar: {self.students}"


class Employee:
    def __init__(self, name, age, position, salary):
        self.name = BEHRUZ
        self.age = 18
        self.position = PROGRAMMER
        self.salary = HIGH_SALARY

    def __str__(self):
        return f"Xodim: {self.name}, Yoshi: {self.age}, Lavozim: {self.position}, Maosh: {self.salary}$"


class Product:
    def __init__(self, name, category, price, quantity):
        self.name = MILK
        self.category = DRINKAMILK
        self.price = 2
        self.quantity = 1

    def __str__(self):
        return f"Mahsulot: {self.name}, Kategoriya: {self.category}, Narx: {self.price}, Soni: {self.quantity}"


class BankAccount:
    def __init__(self, owner, account_number, balance, currency):
        self.owner = MYSELF
        self.account_number = ADMIN1234
        self.balance = 100
        self.currency = DOLLAR


    def __str__(self):
        return f"Egasi: {self.owner}, Hisob: {self.account_number}, Balans: {self.balance} {self.currency}"


class Movie:
    def __init__(self, title, genre, year, rating):
        self.title = CHILLY
        self.genre = HORROR
        self.year = 2018
        self.rating = 7.8

    def __str__(self):
        return f"Kino: {self.title}, Janr: {self.genre}, Yil: {self.year}, Reyting: {self.rating}"


class Game:
    def __init__(self, name, genre, platform, price):
        self.name = EFOOTBALL
        self.genre = FOOTBALL
        self.platform = FOOTBALL.COM
        self.price = 250


    def __str__(self):
        return f"O'yin: {self.name}, Janr: {self.genre}, Platforma: {self.platform}, Narx: {self.price}$"


class Animal:
    def __init__(self, name, species, age, weight):
        self.name = MAYMOQVOY
        self.species = CAT
        self.age = 1
        self.weight = 3

    def __str__(self):
        return f"Hayvon: {self.name}, Turi: {self.species}, Yoshi: {self.age}, Vazni: {self.weight}kg"


class Laptop:
    def __init__(self, brand, model, ram, processor):
        self.brand = LENOVO
        self.model = LENOVO
        self.ram = 12
        self.processor = 256

    def __str__(self):
        return f"Noutbuk: {self.brand} {self.model}, RAM: {self.ram}GB, CPU: {self.processor}"


class Restaurant:
    def __init__(self, name, location, cuisine, rating):
        self.name = ORASTA
        self.location = SHORABOT
        self.cuisine = OSH
        self.rating = 10

    def __str__(self):
        return f"Restoran: {self.name}, Manzil: {self.location}, Taom: {self.cuisine}, Reyting: {self.rating}"


class FootballClub:
    def __init__(self, name, country, stadium, founded):
        self.name = MANCHESTER_UNITED
        self.country = ENGLABD
        self.stadium = OLD_TRAFFORD
        self.founded = 1966

    def __str__(self):
        return f"Klub: {self.name}, Davlat: {self.country}, Stadion: {self.stadium}, Tashkil topgan: {self.founded}"


class ProgrammingLanguage:
    def __init__(self, name, creator, year, difficulty):
        self.name = JAVA
        self.creator = BEXA
        self.year = 1980
        self.difficulty = difficulty

    def __str__(self):
        return f"Dasturlash tili: {self.name}, Yaratuvchi: {self.creator}, Yil: {self.year}, Daraja: {self.difficulty}"


class Smartphone:
    def __init__(self, brand, model, camera, battery):
        self.brand = INFINIX
        self.model = HOT40I
        self.camera = 50
        self.battery = 5000

    def __str__(self):
        return f"Smartfon: {self.brand} {self.model}, Kamera: {self.camera}MP, Batareya: {self.battery}mAh"


class City:
    def __init__(self, name, country, population, area):
        self.name = BUKHARA
        self.country = UZBEKISTAN
        self.population = 7000
        self.area = 100000

    def __str__(self):
        return f"Shahar: {self.name}, Davlat: {self.country}, Aholi: {self.population}, Maydon: {self.area} km²"
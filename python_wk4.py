class Person:
    # Constructor to initialize attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Method to introduce the person
    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Prompt the user for input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

# Create an instance of the Person class using the input
person = Person(name, age, gender)

# Call the introduce method
person.introduce()

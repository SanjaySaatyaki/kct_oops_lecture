name = "Sanjay"
age = 28

##Built-In Objects
#Objects
#--------------------
# print(type(name))
# print(type(age))

# # Methods
# print(name.upper())
# print(age.is_integer())
#--------------------
## Custom Class
#--------------------
# class Dog:
#     def bark(self):
#         print("Whof Whoff")

# dog = Dog()
# dog.bark()
# print(type(dog))

# dog2 = Dog()
# dog2.bark()
#--------------------
## Custom Class with Init
#--------------------
# class Dog:
#     # when a Object is instantiated 
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
    
#     def bark(self):
#         print("Whof Whoff")

# dog1 = Dog("Scootch","Lab")

# print(dog1.name)
# print(dog1.breed)

# dog2 = Dog("Bruno","Beagle")
# print(dog2.name)
# print(dog2.breed)
#--------------------
# Multiple Classes
#--------------------
# class Owner:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
# class Dog:
#     # when a Object is instantiated 
#     def __init__(self, name, breed, owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner
    
#     def bark(self):
#         print("Whof Whoff")

# owner1 = Owner("Sanjay","123")
# dog1 = Dog("Scootch","Lab",owner1)

# all_attributes = dir(dog1)
# print(all_attributes)

# print(f"{dog1.owner.name} is the owner of {dog1.name} and it is {dog1.breed}")
#----------------
#Example 2:
#----------------
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years")

# person1 = Person("Bob",28)
# person1.greet()
#----------------
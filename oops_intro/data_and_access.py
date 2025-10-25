#--------------------
# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password

#     def sayHiToUser(self, user):
#         print(
#             f"Sending message to {user.username}: Hi {user.username}, it's {self.username} ;)"
#         )

# user1 = User("Sanjay", "sanjayabs97@gmail.com", "123")
# user2 = User("Alex", "Alex@gmail.com", "abc")
# user1.sayHiToUser(user2)

# # user1.email = "Hello world@gmail.com"
# # print(user1.email)
#--------------------

# Accessing and Modying Data:
# Make Data private/protected and use getters and setters
# adding _ to the start of attribute name is convention for protected attributes
#-------------
# class User2:
#     def __init__(self, username, email, password):
#         self.username = username
#         self._email = email
#         self.password = password
    
#     def get_email(self):
#         return self._email

#     def clean_email(self):
#         return self._email.lower().strip()

# user2 = User2("Sanjay", " Sanjayabs97@gmail.com", "123")
# # Dont use outside class. Not as per convention
# # print(user2._email)

# print (user2.clean_email())
#-----------------------
# 'The "Consenting Adults" Philosophy
# adding __ to the start of attribute name is convention for private attributes
# Python internally does name mangling
class User2:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.password = password
    
    def get_email(self):
        return self.__email

    def clean_email(self):
        return self.__email.lower().strip()

user2 = User2("Sanjay", " Sanjayabs97@gmail.com", "123")

print(user2.__email)
print (user2.clean_email())



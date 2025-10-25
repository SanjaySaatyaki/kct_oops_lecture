class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.dob = None

    def __str__(self):
        return f'{self.name} born on {self.dob} works as {self.position}'
    
    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder():
    def __init__(self):
        self.person = Person()
    
    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

class PersonBirthBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.dob = date_of_birth
        return self

pb = PersonBirthBuilder()
me = pb.called("Sanjay").works_as_a("Lead Engineer").born("20-03-97").build()

print(me)
class Person:
    def __init__(self):
        # address
        self.street_number = None
        self.post_code = None
        self.city = None

        # employment
        self.company = None
        self.position = None
        self.annual_income = None
    
    def __str__(self):
        return f'Address: {self.street_number}, {self.post_code}, {self.city} ' + \
                f'Employed at {self.company} as {self.position} and earning {self.annual_income}'


class PersonBuilder:
    def __init__(self, person=Person()):
        if person is None:
            self.person = Person()
        else:
            self.person = person
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)
    
    def build(self):
        return self.person
    

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)
    
    def at(self, company_name):
        self.person.company = company_name
        return self
    
    def as_a(self, position):
        self.person.position = position
        return self
    
    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_number = street_address
        return self

    def with_postcode(self, postcode):
        self.person.post_code = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self

pb = PersonBuilder()
person = pb\
        .lives.at('1234').in_city('cbe').with_postcode('641039')\
        .works.at('ABC Company').as_a('Engineer').earning(1234).build()

print(person)
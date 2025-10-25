# Class should have primary responsibilty shouldnt take other responsiblities

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count +=1
        self.entries.append(f"{self.count} : {text}")
    
    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)
    
j = Journal()
j.add_entry('I am happy')
j.add_entry('I ate well')
print(f"Journal Entries: \n{j}")

## Breaking Single Responsiblity Principle
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count +=1
        self.entries.append(f"{self.count} : {text}")
    
    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)
    
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass

j = Journal()
j.add_entry('I am happy')
j.add_entry('I ate well')
print(f"Journal Entries: \n{j}")

# secondary resposiblitis of presistance. by providing functionalities for saving
# Complete application. other functionality need to have the same functions like load and 

class presistance_manager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()
        print(f"saved to file{filename}")

file = r'journal.txt'
presistance_manager.save_to_file(j, file)

with open(file) as f:
    print(f.read())

# Dont overload class with mulitple responsibilites
# Class should have single reason to change and it should be related to primary responsiblities

# Dependency Inversion Principle
# High level shouldnt depend on low level module. it should depend on abstraction
from enum import Enum
from abc import abstractmethod

class relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBILING =2

class person:
    def __init__(self, name):
        self.name = name

# class relationships:
#     def __init__(self):
#         self.relations = []
    
#     def add_parent_and_child(self, parent, child):
#         self.relations.append(
#             (parent, relationship.PARENT, child)
#         )
#         self.relations.append(
#             (child, relationship.CHILD, parent)
#         )

# class research:
#     def __init__(self, relationships):
#         relations = relationships.relations
#         for r in relations:
#             if r[0].name =='John' and r[1] == relationship.PARENT:
#                 print(f'Job has a child called {r[2].name}')

# parent = person('John')
# child1 = person('chris')
# child2 = person('matt')

# relationships_collector = relationships()
# relationships_collector.add_parent_and_child(parent,child1)
# relationships_collector.add_parent_and_child(parent,child2)

# research(relationships_collector)

# research wont work if the storage datastructure changes
# lowlevel module should tell how to do search

#----------------
class relationship_browser:
    @abstractmethod
    def find_all_childern_of(self, name): pass

#low level module
class relationships(relationship_browser):
    def __init__(self):
        self.relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, relationship.PARENT, child)
        )
        self.relations.append(
            (child, relationship.CHILD, parent)
        )
    
    def find_all_childern_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == relationship.PARENT:
                yield r[2].name

#high level module
class research:
    def __init__(self, browser):
        for p in browser.find_all_childern_of('John'):
            print(f'Job has a child called {p}')

parent = person('John')
child1 = person('chris')
child2 = person('matt')

relationships_collector = relationships()
relationships_collector.add_parent_and_child(parent,child1)
relationships_collector.add_parent_and_child(parent,child2)

research(relationships_collector)


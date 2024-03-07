#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge=[]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
    
    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)


mike = Student("Mike", "Tyson")
print(mike.learn("ugali"))
print(mike.learn("ugali2"))



    
    
    
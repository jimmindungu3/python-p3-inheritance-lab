#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, some_string):
        return self.knowledge.append(some_string)
    



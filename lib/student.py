#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name, knowledge = []):
        super().__init__(first_name, last_name, knowledge)
    
    def learn(self, string):
         return self.knowledge.append(string)
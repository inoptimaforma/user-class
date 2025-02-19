import random
import string
import datetime
import re
import unittest

class User:
    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday
    
    def get_details(self):
        return "ID: " + str(self.user_id) + " Name: " + self.name + " " + self.surname + " Email: " + self.email + " Age: " + str(self.get_age())
    
    def get_age(self):
        current = datetime.date.today()
        age = current.year - self.birthday.year - ((current.month, current.day) < (self.birthday.month, self.birthday.day))
        return age
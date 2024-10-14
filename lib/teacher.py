#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
    ]

    def __init__(self, first_name, last_name):
        # Call the User class initializer to set first_name and last_name
        super().__init__(first_name, last_name)
        # Initialize the knowledge attribute as a list
        self.knowledge = Teacher.knowledge


    def teach(self):
        # Returns a random piece of knowledge from the knowledge list
        return random.choice(self.knowledge)
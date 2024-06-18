#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]




approved_jobs = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Default Name", job="General Management"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            self._job = None

# Example usage:
person1 = Person("alice smith", "ITC")
print(person1.name)   
print(person1.job)   

person2 = Person("", "Sales")  
print(person2.name)   
print(person2.job)   

person3 = Person("Bob", "Chef")   
print(person3.name)     
print(person3.job)  

person4 = Person(123, "Marketing")      
print(person4.name)     
print(person4.job)  
from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person : Person = {'name':'James','age':3}

print(new_person)
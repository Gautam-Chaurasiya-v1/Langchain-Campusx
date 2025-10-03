from pydantic import BaseModel , EmailStr , Field
from typing import Optional


class Student(BaseModel):

    name : str = 'nitin'
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0,le=10,default=9,description='It is a decimal value repersenting the cgpa of the student')


new_student = {'name':'James','age' : 23 , 'email': 'james@gmail.com'  }

student = Student(**new_student)

student_dict = dict(student)

print(student_dict)

student_json = student.model_dump_json()

print(student_json)

print(student.name,type(student.name))
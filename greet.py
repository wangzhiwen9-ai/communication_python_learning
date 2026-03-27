#1. Variable, input and output
from operator import truediv

name = input("please enter your name :")
age = int(input("please enter your age :"))
print(f"Hello,{name},you are {age} years old ,welcome to python & communication !")

#2. Define variables of different type
name = "Ai communication learner"
age = 19
is_student = True
score = [100,95,93]
print(f'Name:{name},Type{type(name)}')
print(f'Age:{age},Type{type(age)}')
print(f"Is student:{is_student},Type{type(is_student)}")
print(f'Store List:{score},Type:{type(score)}')

#3. variable type conversion
print("\nType conversion demo:")
print(f"Number to string: str({age})->’{str(age)}'")
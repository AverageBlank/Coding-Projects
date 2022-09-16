# Imports
from quitting import eq
from time import sleep
from name import func_name
from age import func_age
from classes import func_grades
from converting_database import func_excel

# Variable
current_students = 1
loop = 1
result = {}

# Defining
# Loop
while True:
    # Name
    name = func_name().title()

    # Age
    age = func_age(d=name)

    # Class
    grade,c,final,l2n,st,st5,l3n = func_grades(e=name)
    sleep(1)

    # Total
    total = sum(grade.values()) - c
    print(f'The total is {total}.')
    
    # Average
    avg = total/(len(grade.values()) - 1)
    print(f'The average is {avg:.2f}')

    database = [name,age,grade,total,avg,final]

    # Adding students
    while loop != 2:
        student = input('Do you want to add another student(Type in either yes or no)? ').lower()
        sleep(1)
        if student != 'yes' and student != 'no':
            print('Please type in either yes or no.')
            sleep(1)
            eq()
            continue
        elif student == 'yes':
            result.update({current_students:database})
            current_students += 1
            break
        elif student == 'no':
            loop = 2
    else:
        result.update({current_students:database})
        func_excel(x=result,z=l2n,p=st,q=st5,r=l3n)
        break

print('The program has quit succesfully.    ')

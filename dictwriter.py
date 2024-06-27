import csv 
student_list = []

name = input('Enter name: ').strip().title()
course = input('Enter Course: ').strip().upper()

with open('student.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "course"])
    writer.writerow({"name": name, "course": course})
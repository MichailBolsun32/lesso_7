grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_students = list(students)
list_students.sort()

dict_grades_students =dict()

for i in range(len(grades)):
     dict_grades_students[list_students[i]] = sum(grades[i]) / len(grades[i])

print(dict_grades_students)
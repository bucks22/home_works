grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_list = sorted(list (students))
av1 = sum(grades[0])/len(grades[0])
av2 = sum(grades[1])/len(grades[1])
av3 = sum(grades[2])/len(grades[2])
av4 = sum(grades[3])/len(grades[3])
av5 = sum(grades[4])/len(grades[4])
class_ = {student_list[0]:av1,
          student_list[1]:av2,
          student_list[2]:av3,
          student_list[3]:av4,
          student_list[4]:av5}
print(class_)
key_input = input('Введите имя ученика из списка: ')
if key_input in class_:
    print('Средняя оценка ученика', key_input, ':', class_[key_input])
else:
    print('Ученик', key_input, 'не найден в списке')


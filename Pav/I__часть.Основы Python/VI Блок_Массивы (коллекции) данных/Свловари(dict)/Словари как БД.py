class_studens = {
    '5A': ['Даша', 'Миша', 'Игорь'],
    '5B': ['Евпатий', 'Ева', 'Игорь']
}

# Добавление нового ученика в класс
# class_studens['5A'].append('dada')
# print(class_studens['5A'])

# Поиск учеников
# def find_student(name):
    # for class_name, students in class_studens.items():
    #     if name in students:
    #         return f"{name} находится в классе {class_name}"
    #
    #     return "Человка нет"
#     classes_student = [class_name for class_name, students in class_studens.items() if name in students]
#
#     return f'{name} находится в классе {" ".join(classes_student)}' if classes_student else f'{name} не найден'
#
# print(find_student('Игорь'))
#
# total_stude = 0
# for student in class_studens.values():
#     total_stude += len(student)

total_stude = sum(len(students) for students in class_studens.values())

print(f'общее количество учеников {total_stude}')

# Перемещение ученика из одного класса в другой

def transfer_student(name, from_class, to_class):
    if name in class_studens[from_class]:
        class_studens[from_class].remove(name)
        class_studens[to_class].append(name)
        print(f'Ученик {name} перемещен из {from_class} в {to_class}')
    else:
        print(f'Ученик {name} не найден в классе {from_class}')
transfer_student('Игорь', '5A', '5B')

# Группировка учеников по группе "Е"

student_with_e = []
for students in class_studens.values():
    for student in students:
        if student.startswith('Е'):
            student_with_e.append(student)
print(f'Ученики, чье имя начианется на "Е": {student_with_e}')
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

# total_stude = sum(len(students) for students in class_studens.values())
#
# print(f'общее количество учеников {total_stude}')
#
# # Перемещение ученика из одного класса в другой
#
# def transfer_student(name, from_class, to_class):
#     if name in class_studens[from_class]:
#         class_studens[from_class].remove(name)
#         class_studens[to_class].append(name)
#         print(f'Ученик {name} перемещен из {from_class} в {to_class}')
#     else:
#         print(f'Ученик {name} не найден в классе {from_class}')
# transfer_student('Игорь', '5A', '5B')
#
# # Группировка учеников по группе "Е"
#
# student_with_e = []
# for students in class_studens.values():
#     for student in students:
#         if student.startswith('Е'):
#             student_with_e.append(student)
# print(f'Ученики, чье имя начианется на "Е": {student_with_e}')

# project_tasks = {
#     'Веб-разработка': ['Дизайн интерфейса', 'Разработка бэкенда', 'Тестирование'],
#     'Маркетинговая кампания': ['Анализ рынка', 'Разработка стратегии', 'Реклама']
# }
# for key, value in project_tasks.items():
#     if key == 'Веб-разработка':
#         value.append('SEO оптимизация')
#         print(f'Задачи проекта "{key}": {value}')

# keyword = 'Разработка'
# tasks_with_keyword = {}
# project_tasks['Веб-разработка'].append('SEO оптимизация')
#
# for project, tasks in project_tasks.items():
#     tasks_with_keyword[project] = []
#     for task in tasks:
#         if keyword in task:
#             tasks_with_keyword[project].append(tasks)
#
# print(f'Задачи проекта "Веб-разработка": {project_tasks["Веб-разработка"]}')
# print(f'Задачи, содержащие "{keyword}": {tasks_with_keyword}')
# project_tasks = {
#     'Веб-разработка': ['Дизайн интерфейса', 'Разработка бэкенда', 'Тестирование'],
#     'Маркетинговая кампания': ['Анализ рынка', 'Разработка стратегии', 'Реклама']
# }
#
# keyword = 'Разработка'
# tasks_with_keyword = {}
#
# # Добавление новой задачи в проект
# project_tasks['Веб-разработка'].append('SEO оптимизация')
#
# for project, tasks in project_tasks.items():
#     tasks_with_keyword[project] = []
#     for task in tasks:
#         if keyword in task:
#             tasks_with_keyword[project].append(task)
#
#
# print(f'Задачи проекта "Веб-разработка": {project_tasks["Веб-разработка"]}')
# print(f'Задачи, содержащие "{keyword}": {tasks_with_keyword}')

# project_tasks = {
#     'Веб-разработка': ['Дизайн интерфейса', 'Разработка бэкенда', 'Тестирование'],
#     'Маркетинговая кампания': ['Анализ рынка', 'Разработка стратегии', 'Реклама']
# }
# project_tasks['Веб-разработка'].append('SEO оптимизация')
# print(f'Задачи проекта "Веб-разработка": {project_tasks["Веб-разработка"]}')
# print('*' * 100)
# word = "Разработка"
# filtr_dict = {}
# for key, values in project_tasks.items():
#     filtr_dict[key] = []
#     for value in values:
#         if word in value:
#             filtr_dict[key].append(value)
# print(filtr_dict)

# count = 0
# for value in project_tasks.values():
#     count += len(value)
# print(count)
#
# count_t = sum(len(value) for value in project_tasks.values())
# print(count_t)

# for key, values in project_tasks.items():
#     project_tasks[key].append('Анализ конкурентов')
#
# print(project_tasks)
# daily_plan = {}
# for project, tasks in project_tasks.items():
#     if tasks:  # Проверка на наличие задач в проекте
#         daily_plan[project] = tasks[0]  # Добавление первой задачи в план
#
# # План на день с использованием генератора
# daily_plan = {project:tasks[0] for project, tasks in project_tasks.items() if tasks}
#
# print(f'План работы на день: {daily_plan}')

# for key, tasks in project_tasks.items():
#     for task in tasks:
#         if task == "Реклама":
#             tasks.pop()
# print(project_tasks)


# categories = {'Разработка':[], 'Маркетинг':[]}
# for tasks in project_tasks.values():
#     for task in tasks:
#         if 'Разработка' in task:
#             categories['Разработка'].append(task)
#         elif 'Маркетинг' in task:
#             categories['Маркетинг'].append(task)
# print(categories)

project_tasks = {
    'Веб-разработка': ['Дизайн интерфейса', 'Разработка бэкенда', 'Тестирование'],
    'Маркетинговая кампания': ['Анализ рынка', 'Разработка стратегии', 'Реклама']
}


employees = ['Даша', 'Игорь', 'Михаил']

# Распределение задач между сотрудниками (без генератора)
task_assignment = {}

# Инициализация пустых списков для каждого сотрудника
for employee in employees:
    task_assignment[employee] = []

# Распределение задач между сотрудниками
for project, tasks in project_tasks.items():
    for i, task in enumerate(tasks):
        assigned_employee = employees[i % len(employees)]
        task_assignment[assigned_employee].append(f'{task} ({project})')

print(task_assignment)

for project, tasks in project_tasks.items():
    print(f'Проект "{project}":')
    for task in tasks:
        print(f' - {task}')
    print()

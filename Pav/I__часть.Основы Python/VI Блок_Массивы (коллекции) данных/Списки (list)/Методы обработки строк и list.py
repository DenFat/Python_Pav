# words_s = 'яблоко, банан, вишня, апельсин'
# words_list = words_s.split(', ')
# print(words_list)

# my_list = ['один', 'два', 'три']
# string_list = ', '.join(my_list)
# print(string_list)

# data_s = 'Игорь:25:инженер'
# name, age, prof = data_s.split(':')
# print(f' Имя: {name}')
# print(f' Возраст: {age}')
# print(f' Профессия: {prof}')

# words = ['яблоко', 'банан', 'вишня']
# delimeter = ', '
# # res_s = delimeter.join(words)
# # print(res_s)
# res_s = ''
# for i, word in enumerate(words):
#     res_s += word
#     if i < (len(words) - 1):
#         res_s += delimeter
#
# print(res_s)

# s = 'один два три'
# print(s.replace('два', 'четыре'))

# txt = 'Я люблю яблоки, яблоки очень вкусные!'
# # new_txt = txt.replace('яблоки', 'Игори')
# new_txt = txt.replace('яблоки', 'Игори', 1)
# print(new_txt)

# sen = 'Python - это замечательный язык программирования'
# words = sen.split(' ')
# reverse_word = ' '.join(reversed(words))
# print(reverse_word)

# text = 'Кот это забавное животное, а собака - и подавно, та еще красавица'
# banned_words = ['забавное', 'красавица']
# for word in banned_words:
#     text = text.replace(word,'*' * len(word))
# print(text)

# dates_string = '2023-10-05,2023/10/6;2023.10.07'
# print(dates_string.replace('/','-').replace('.','-').replace(';',',').split(','))

# words = ['При#ет', 'Мир*!', 'Питон', 'это', 'замеч_ательно']
# s = ' '.join(words)
# string = s.replace('#', '').replace('*','').replace('_','')
# print(string)

items_string = 'apple=0.5#;orange/0.3&banana:0.4'
string = items_string.replace('=', ':').replace('#','').replace('/',':').replace('&',';')
items_list = string.split(';')
total_cost = 0
for item in items_list:
    name, cost = item.split(':')
    total_cost += float(cost)

print(f'Общая цена составляет {total_cost:.2f} $')
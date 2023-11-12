# fru = ['apple', 'banana', 'data']
# for fruit in fru:
#     print(fruit, end=' ')

# number = [1,2,3,4,5,6,3]
# print('Сравнение текущего элемента со следующим')
# prev_num = None
# for i in number:
#     if prev_num is not None:
#         if prev_num < i:
#             print(f'{prev_num} меньше {i}')
#         else:
#             print(f'{prev_num} не меньше {i}')
#     prev_num = i

# words = ['apple', 'cherry', 'banana', 'date','grade']
#
# print('Слова начинающиеся с буквы "a"')
# for word in words:
#     if word[0] == 'a':
#         print(word)

# numbers = [1,2,3,4,5]
#
# print(f'До: {numbers}')
# index = 0
# for i in numbers:
#     numbers[index] = i*2
#     index += 1
# print(f'После: {numbers}')

names = ['Игорь', 'Брат Игоря', 'Зять Игоря']
score = [85,99,66]

index = 0
for i in names:
    print(f'{i} имеет оценку {score[index]}')
    index += 1
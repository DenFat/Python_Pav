# print([num for num in range(5)])
# print([num*2 for num in range(5)])
#
# print([sym for sym in 'Игорь'])
# print([sym for sym in 'Игорь'])

# a = 5
# b = 3
# if a > b:
#     res = 'a больше'
# else:
#     res = 'a не больше'
# print(res)

# res = 'a больше' if a > b else 'a не больше'
# print(res)

# a = 5
# b = 10

# if a > b:
#     print('a больше b')
# else:
#     print('b больше a')

# print ('a больше b' if a > b else 'b больше a')
# print ('a больше b') if a > b else print('b больше a')

# digit_list = [num for num in range(5) if num % 2 == 0]  # ФИЛЬТР по четности
# print(digit_list)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_num_list = [num for num in numbers if num % 2 != 0]  # ФИЛЬТР по нечетности
# print(odd_num_list)

# words = ['Игорь', 'Иииииииигорь', 'Маша', 'Даша']
# long_words = [word for word in words if len(word)>5]
# print(long_words)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # new_list = []
# # for i in numbers:
# #     if i % 2 == 0:
# #         new_list.append(i)
# # print(new_list)
#
# evens = []

# num_list = [num * 2 if num % 2 == 0 else num for num in range(5)]
# print(num_list)

# words = ['Игорь', 'Игггггггггггггорь', 'cherry']
# print([ word if len(word) <= 5 else word[:5] + '...' for word in words])

# print([num* 2 for num in range(10) if num % 2 == 0])
# print([num* 2 if num % 2 == 0 else num for num in range(10)])


print(', '.join([str(num) for num in range(31)]))
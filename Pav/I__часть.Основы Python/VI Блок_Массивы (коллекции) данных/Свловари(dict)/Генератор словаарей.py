# squaers = {x: x*x for x in range(6)}
# squaers = {f'Квадрат {x}': x*x for x in range(6)}
# squaers = {'Квадрат ' + str(x): x*x for x in range(6)}
# print(squaers)

# words = ['Игорь', 'Даша', 'Вася']
# print({x: len(x) for x in words})
# print({x[0]: x for x in words})
# print({x: x[::-1] for x in words})

s = 'hello'
# print({char: s.count(char) for char in s})
# print({char: ord(char) for char in s})

# nums = range(1,10)
# print({num: num**2 for num in nums if num % 2 == 0})

# words = ['apple', 'cat', 'dog', 'bat']
# print({word: len(word) for word in words if len(word) > 3})

# data = {'a': 10, 'b': 15, 'c': 5}
# print({k: v for k, v in data.items() if v > 10})

# num = [1, 2, 3, 4, 5]
# print({n: 'чет' if n % 2 == 0 else 'нечет' for n in num})

# import random
# def foo(a = 10):
#     num = range(1,a)
#     return {i: random.randint(1,20) for i in num}
# print(foo())
# print(foo(6))

# import random
# import string
# def foo(length = 5):
#     letters = string.ascii_lowercase  # Строка содержащая все строчные буквы английского алфавита "abcd..."
#     # return {i: random.sample(letters, length) for i in range(10)}
#     return {a: ''.join(random.choice(letters) for _ in range(length)) for a in range(1,6)}
# print(foo())

# print(sum(range(1,11)))
# num_dict = {i: i for i in range(1,11)}
# sum_of_values = sum(num_dict.values())
# print(sum_of_values)

# my_dict = {i: str(i) for i in range(1,6)}
# print(my_dict)

# my_dict = {i: i for i in range(1,15)}
# print(f'Минимальное значение {min(my_dict.values())}, максимальное значение {max(my_dict.values())}')

# string = "Мама мыла раму и окно"
# print({i: i for i in string.split()})


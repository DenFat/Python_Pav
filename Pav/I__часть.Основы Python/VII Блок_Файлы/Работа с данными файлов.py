# with open('text.txt', 'w+', encoding='utf-8') as file:
#     file.write('Игорь - это всё что у нас есть\n'
# 'Ехали медведики на велосипедике \n'
# 'Я хочу заниматься программированием')
#     file.seek(0)
#     data = file.read()
#     # modifid_data = data.replace('а', 'А')
#     modifid_data = data.upper()
#     file.seek(0)
#     file.write(modifid_data)
#
# print(modifid_data)

with open('text_1.txt', 'w+', encoding='utf-8') as file:
    file.write('Это первая строка')

    file.seek(0)

    words = file.readline()

    print(words)

    words = words.split()

    words2 = (words[1:])

    words = ' '.join(words2)

    file.seek(0)
    file.truncate()
    file.write('\n' + words)
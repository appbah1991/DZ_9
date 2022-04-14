list_1 = list(input('Введите элементы первого списка через запятую: ').split(','))
list_2 = list(input('Введите элементы второго списка через запятую: ').split(','))
for elem in list_2:
    list_1.remove(elem)
print(list_1)
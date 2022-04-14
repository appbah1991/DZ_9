quant = int(input('Введите количество элементов: '))
list_1 = []
while quant > 0:
        element = input()
        list_1.append(element)
        quant += -1
list_1.sort()
print(list_1)
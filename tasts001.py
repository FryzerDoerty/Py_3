#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
len_1 = int(input('Введите длину первого набора чисел: '))
len_2 = int(input('Введите длину второго набора чисел: '))
list_1 = []
list_2 = []

for b in range(len_1):
    list_1.append(int(input('Введите число первого набора чисел: ')))
    
for c in range(len_2):
    list_2.append(int(input('Введите число второго набора чисел: ')))
 
list_1 = list(set(list_1))
list_1.sort()
list_2 = list(set(list_2))
list_2.sort()
#print(list_1)
#print(list_2)
for i in range(len(list_2)):
    for j in range(len(list_1)):
        if list_2[i]==list_1[j]:
            print(list_2[i])
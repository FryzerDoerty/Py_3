#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
len_1 = int(input('Введите длину первого набора чисел: '))
list_1 = []
for b in range(len_1):
    list_1.append(int(input('Введите число первого набора чисел: ')))
i=1
max = list_1[0] + list_1[1] + list_1[len(list_1)-1]
max_1 = list_1[len(list_1)-1]+ list_1[len(list_1)-2] + list_1[0]
while(i<len(list_1)):
        if(max<(list_1[i]+list_1[i+1] + list_1[i-1])):
            max = list_1[i]+list_1[i+1] + list_1[i-1]
        i+=2
if(max<max_1):
     max = max_1
print(max)

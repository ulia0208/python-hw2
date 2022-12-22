# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

from random import randint
n=randint(3,10)
my_list=[randint(-10,10) for i in range(n)]
print(my_list)

my_list2=[]
for i in range(n):
    my_list2.append(my_list[i])

for i in range(n):
    k=randint(0,len(my_list)-1)
    my_list2[i]=my_list[k]
    my_list.remove(my_list[k])
print(my_list2)

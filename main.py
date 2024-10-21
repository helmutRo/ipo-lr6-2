
import random
numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2] #значения для заполнения матрицы 
x = 0 #счётчик кратных 3 
a = list() #строка матрицы
b = int(random.random() * 5 + 4) #колво столбиков в матрице
c = int(random.random() * 5 + 4) #колво строк в матрице
for i in range(b): 
    a = [random.choice(numbers) for i in range(c)] #строки заполняются рандомными числами из numbers
    print(*a) #вывод строки
    for d in a:
        x += (d if d % 3 else 0 ) #в счетчик прибавляются если числа кратные трем
print (f"сумма всех элементов кратных 3: {x}") #вывод суммы
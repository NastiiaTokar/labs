import math

#Введення початкових значень

a = 6 #Початок
b = 9 #Кінець
h = 0.2 #Крок
x = 3

# Функція для табулювання lg(x*ln(x)+sin(x))

def func1 (x): #Створення функції
    if x <= 0: #Перевірка, x має бути більше за 0
        return None #Немає значення - відсутність результату
    try:
        result = x * math.log(x) + math.sin(x) #Обчислення
        if result > 0: #Перевірка чи більше 0
            return math.log10(result) #Обчислення
        else:
            return None
    except ValueError: #Обробка вийнятків - помилок
        return None
    
# Функція для табулювання log3(sin(x)+4)

def func2(x):
    try:
        result = math.sin(x)+4
        if result > 0:
            return math.log(result, 3) #Логарифм за основою 3
        else:
            return None
    except ValueError:
        return None
    
    # Функція для табулювання 1/16 + sec(x)

def func3(x):
    try:
        return 1/16 + math.cos(x) #Обчислення секанса
    except ValueError:
        return None
    
# Табуляція функцій на проміжку [a,b] з кроком h

x = a #Змінній x присвоюється значення a
print (f"{'x':<10}{'f(x)':<20}") #Виводить заголовки стовпців для таблиці
while x <= b: #Цикл виконується, поки x не досягне b
    if x < 7:
        y = func1(x)
        print (f"{x:^15.2f}{y:^15.5f}") #Використання першої функції
    elif 7 <= x < 8: #Перевірка умови
        y = func2(x)
        print (x, y)#Використання другої функції
    else: #Запасний варіант
        y = func3(x)
        print (x, y) #Використання третьої функції      
    x += h 
    x = round (x, 3)
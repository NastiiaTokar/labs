import math

# Параметри
m = 9
a = 0 
b = 0.5 
h = 0.005 
d = 0.001 

# Функція для обчислення члена ряду
def term(m, n, x): 
    product = (-1)**n  
    for i in range(n): 
        product *= (m + i) 
    return product * x**n / math.factorial(n)  

# Функція для табулювання ряду
def tabulate_series(m, a, b, h, d):
    x = a  
    while x <= b:
        sum_series = 1 
        n = 1 
        while True: 
            next_term = term(m, n, x) 
            if abs(next_term) < d:  
                break  
            sum_series += next_term
            n += 1 
        print(f"x = {x}, f(x) = {1+sum_series}")
        x += h  
        x = round(x, 3)

# Виконування табулювання
tabulate_series(m, a, b, h, d)
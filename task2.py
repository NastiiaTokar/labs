import math
import math as m
result = m.sqrt(16) ''

# Значення аргументів
x = 0.357 
y = 2.031

# Операції
cos_y = math.cos(y)
tan_x = math.tan(x)
sqrt_term = math.sqrt(y-x)
ln_term = math.log(y ** 3)
result = (x ** cos_y) - (tan_x ** sqrt_term) - (19.12 * ln_term)

# Результати
print ("Результат виразу для x = {x} і y = {y}")
print ("x^cos(y) - tan(x)^(sqrt(x)) - 19.12 * ln(y^3) =", result)
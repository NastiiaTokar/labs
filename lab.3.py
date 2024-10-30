# Функція для формування числа M з кожного K символу числа N

def form_m(N, K):
    M = ""  # Ініціалізація порожнього рядка для числа M
    for i in range(len(N)):  # Перебираємо всі індекси символів числа N
        if (i + 1) % K == 0:  # Якщо позиція символу кратна K, додаємо його до M
            if i + 1 < len(N): 
                M += N[i + 1] 
            else:
                M += N[i] 
        
    return M  # Повертаємо сформоване число M

# Функція для перевірки, чи є число M "щасливим"

def is_lucky(M):
    if M == "":  # Перевіряємо, що M не порожнє
        return "NO"
    
    # Обчислення суми цифр для перевірки на кратність 3

    sum_digits = 0
    for digit in M:  # Перебираємо всі символи в M
        sum_digits += int(digit)
    
    if sum_digits % 3 == 0:  # Якщо сума цифр кратна 3, то число щасливе
        return "YES"
    else:
        return "NO"

# Основна частина програми

def main():
    N = input("Введіть число N: ")  # Введення числа N
    K = int(input("Введіть ключ K (від 1 до 10): "))  # Введення ключа K
    
    M = form_m(N, K)  # Формуємо число M
    print(f"Число M: {M}")  # Виводимо число M
    
    result = is_lucky(M)  # Перевіряємо, чи є число M щасливим
    print(result)  # Виводимо результат: "YES" або "NO"

# Викликаємо основну функцію
main()

def reformat_list(N):
    return N[2:] + N[:2]

N = "12345"
reformatted_N = reformat_list(N)
print("Переформатований список:", reformatted_N)

def sum_of_digits(N):
    return sum(int, N)

def make_divisible_by_3(N):
    if sum_of_digits(N) % 3 != 0:
        N += '0' 
    return N

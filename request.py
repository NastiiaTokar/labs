import requests
# URL, до якого ви хочете виконати HTTP-запит
url = "https://httpbin.org/get"  # або будь-який інший URL
# Виконання GET-запиту до вказаного URL
response = requests.get(url)
# Виведення вмісту відповіді на екран
print(response.text)
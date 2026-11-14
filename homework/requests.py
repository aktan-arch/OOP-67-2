import requests

# 1. GET - данные получить
response = requests.get("https://api.github.com/users/aktan-arch")
print(response.status_code)  # 200 = ок, 404 = нету
data = response.json()  # ответ -> словарь
print(data['login'], data['public_repos'])

# 2. PARAMS - поиск
response2 = requests.get(
    "https://api.github.com/search/users",
    params={"q": "aktan"}  # ищем по слову aktan
)
print("Найдено:", response2.json()['total_count'])

# 3. HEADERS - кто мы
headers = {"User-Agent": "Moya programma"}
response3 = requests.get("https://httpbin.org/headers", headers=headers)
print(response3.json())

# 4. POST - данные отправить
response4 = requests.post(
    "https://httpbin.org/post",
    data={"name": "Aktan", "age": 18}  # отправляем это
)
print(response4.json()['form'])

# 5. Проверка ошибок
response5 = requests.get("https://api.github.com/users/netakogocheloveka12345")
if response5.status_code == 200:
    print("Есть такой!")
else:
    print("Ошибка:", response5.status_code)

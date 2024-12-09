import requests
import json
import matplotlib.pyplot as plt

# Запит даних з API НБУ
url_string = "https://bank.gov.ua/NBU_Exchange/exchange_site?json&start=20241007&end=20241011&valcode=usd"
my_response = requests.get(url_string)

if my_response.status_code == 200:
    response_json = json.loads(my_response.content)

    # Збираємо дані для графіка
    dates = [item['exchangedate'] for item in response_json]  # Дати
    rates = [item['rate'] for item in response_json]  # Курси

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(dates, rates, marker='o', linestyle='-', color='b', label='USD/UAH')
    plt.xlabel('Дата')
    plt.ylabel('Курс (UAH)')
    plt.title('Зміна курсу USD до UAH (за вибраний період)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print("Не вдалося отримати дані з API. Статус-код:", my_response.status_code)

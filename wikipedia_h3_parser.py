import requests
from bs4 import BeautifulSoup

# URL страницы Wikipedia о Python
url = 'https://ru.wikipedia.org/wiki/Python'

# Заголовки для имитации браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # GET-запрос к странице
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Проверяем, что запрос успешен

    # Парсинг HTML-контент с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Поиск всех заголовков h3
    h3_headings = soup.find_all('h3')

    # Сохранение заголовков в текстовый файл
    with open('h3_headings.txt', 'w', encoding='utf-8') as file:
        for heading in h3_headings:
            # Запись текста каждого заголовка в файл
            file.write(heading.get_text() + '\n')

    print("Заголовки успешно сохранены в файл 'h3_headings.txt'")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе к странице: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
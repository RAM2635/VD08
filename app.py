from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://api.quotable.io/random"

@app.route('/')
def home():
    try:
        # Запрос к API
        response = requests.get(API_URL, verify=False)
        response.raise_for_status()
        quote_data = response.json()
        quote = quote_data.get("content", "Цитата недоступна")
        author = quote_data.get("author", "Неизвестный автор")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        quote = "Не удалось загрузить цитату."
        author = "Ошибка"
    except ValueError as e:
        print(f"Ошибка обработки JSON: {e}")
        quote = "Цитата недоступна."
        author = "Ошибка"

    return render_template("index.html", quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)

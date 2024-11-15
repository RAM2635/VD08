
# Flask Quotes App

Это простое веб-приложение на Flask, которое отображает случайные цитаты, полученные из API [Quotable](https://api.quotable.io).

## Описание

Приложение запрашивает случайные цитаты через публичный API и отображает их на веб-странице. При обновлении страницы загружается новая цитата.

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <URL_репозитория>
cd <папка_проекта>
```

### 2. Установка виртуального окружения (рекомендуется)

```bash
python -m venv .venv
```

Активируйте окружение:

- **Windows:**

  ```bash
  .venv\Scripts\activate
  ```

- **Linux/Mac:**

  ```bash
  source .venv/bin/activate
  ```

### 3. Установка зависимостей

Убедитесь, что у вас установлен `pip`. Установите необходимые библиотеки:

```bash
pip install flask requests
```

### 4. Запуск приложения

Запустите приложение:

```bash
python app.py
```

Откройте в браузере: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Решение возможных проблем

### Ошибка `certificate verify failed`

Если сертификат API устарел, можно временно отключить проверку SSL, добавив `verify=False` в запросы `requests.get()`.

## Структура проекта

```bash
project/
│
├── app.py                 # Основной файл приложения Flask
├── requirements.txt       # Зависимости проекта
└── templates/             # HTML-шаблоны
    └── index.html         # Главная страница приложения
```

## Используемые технологии

- **Flask**: Веб-фреймворк для Python.
- **Requests**: Библиотека для выполнения HTTP-запросов.

## Планы на будущее

- Добавить возможность выбора категорий цитат.
- Поддержка других API для получения цитат.
- Улучшить дизайн страницы.

## Благодарности

Большое спасибо API Quotable за предоставление данных.
```

GitHub (https://api.quotable.io/)
GitHub - lukePeavey/quotable: Random Quotes API
Random Quotes API. Contribute to lukePeavey/quotable development by creating an account on GitHub.
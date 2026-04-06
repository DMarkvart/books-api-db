# Books API DB

REST API для управления коллекцией книг с использованием реальной базы данных.

## Стек
- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Установка
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск
```bash
uvicorn main:app --reload
```

## Документация

После запуска: http://127.0.0.1:8000/docs

## Эндпоинты

| Метод | Адрес | Описание | Статус |
|-------|-------|----------|--------|
| GET | /books | Все книги | 200 |
| GET | /books/{id} | Книга по ID | 200 |
| POST | /books | Создать книгу | 201 |
| PUT | /books/{id} | Обновить книгу | 200 |
| DELETE | /books/{id} | Удалить книгу | 204 |

## Структура проекта
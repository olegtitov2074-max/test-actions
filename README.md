# Server Time API

Простой бэкенд на FastAPI, возвращающий текущее время сервера.

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn main:app --reload
```

Сервер запустится по адресу: [http://localhost:8000](http://localhost:8000)

## API

### GET `/time`

Возвращает текущее время сервера.

**Ответ:**

```json
{
  "utc": "2026-08-14T12:30:45+0000",
  "timestamp": 1755169845.0
}
```

## Документация

Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

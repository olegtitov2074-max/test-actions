# Server Time API

FastAPI-сервис для получения текущего времени сервера.

## Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| GET | `/time` | Текущее время UTC в формате ISO 8601 |
| GET | `/date` | Текущая дата и день недели |
| GET | `/datetime` | Полная дата и время + день недели |

### Примеры ответов

**GET /time**
```json
{
  "utc": "2025-01-15T12:30:45+0000",
  "timestamp": 1736939445.0
}
```

**GET /date**
```json
{
  "date": "2025-01-15",
  "day_of_week": "Wednesday",
  "timestamp": 1736939445.0
}
```

**GET /datetime**
```json
{
  "datetime": "2025-01-15T12:30:45+0000",
  "date": "2025-01-15",
  "time": "12:30:45",
  "day_of_week": "Wednesday",
  "timestamp": 1736939445.0
}
```

## Локальный запуск

```powershell
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Docker

```powershell
docker build -t server-time-api .
docker run -p 8080:8000 server-time-api
```

## CI/CD

Автоматическая сборка и деплой при push в `main`:

1. GitHub Actions собирает Docker-образ
2. Публикует образ в GitHub Container Registry (GHCR)
3. Разворачивает контейнер на сервере через SSH

## Стек

- Python 3.11
- FastAPI
- Uvicorn
- Docker
- GitHub Actions
# Server Time API

FastAPI-сервис для получения текущего времени, даты и дня недели сервера.

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141.1-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-supported-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Описание

API предоставляет три эндпоинта для получения информации о времени сервера:

| Эндпоинт | Описание |
|----------|----------|
| `GET /time` | Текущее время UTC в формате ISO 8601 |
| `GET /date` | Текущая дата и день недели |
| `GET /datetime` | Полная дата и время с днём недели |

## 🚀 Быстрый старт

### Локальный запуск

```powershell
# 1. Создаём виртуальное окружение
python -m venv .venv
.venv\Scripts\Activate.ps1

# 2. Устанавливаем зависимости
pip install -r requirements.txt

# 3. Запускаем сервер
uvicorn main:app --host 0.0.0.0 --port 8000
```

Откройте браузер: http://localhost:8000

### Docker

```powershell
# 1. Собираем образ
docker build -t server-time-api .

# 2. Запускаем контейнер
docker run -d --name server-time -p 8002:8000 server-time-api

# 3. Проверяем
curl http://localhost:8002/time
```

## 📡 API Документация

### GET /time

Возвращает текущее время UTC.

**Пример запроса:**
```
GET http://89.104.74.189:8002/time
```

**Пример ответа:**
```json
{
  "utc": "2026-08-19T09:20:30+0000",
  "timestamp": 1787131230.969728
}
```

### GET /date

Возвращает текущую дату и день недели.

**Пример запроса:**
```
GET http://89.104.74.189:8002/date
```

**Пример ответа:**
```json
{
  "date": "2026-08-19",
  "day_of_week": "Wednesday",
  "timestamp": 1787131230.969728
}
```

### GET /datetime

Возвращает полную дату, время и день недели.

**Пример запроса:**
```
GET http://89.104.74.189:8002/datetime
```

**Пример ответа:**
```json
{
  "datetime": "2026-08-19T09:20:30+0000",
  "date": "2026-08-19",
  "time": "09:20:30",
  "day_of_week": "Wednesday",
  "timestamp": 1787131230.969728
}
```

## 📚 Интерактивная документация

FastAPI автоматически генерирует документацию:

- **Swagger UI:** http://89.104.74.189:8002/docs
- **ReDoc:** http://89.104.74.189:8002/redoc

## 🏗️ Структура проекта

```
.
├── .github/workflows/
│   └── deploy.yml          # CI/CD пайплайн
├── .dockerignore           # Исключения для Docker
├── Dockerfile              # Сборка Docker-образа
├── main.py                 # FastAPI приложение
├── requirements.txt        # Зависимости Python
└── README.md               # Документация
```

## 🔄 CI/CD

Проект использует GitHub Actions для автоматической сборки и деплоя:

1. **Push в main** → запуск Workflow
2. **Сборка Docker-образа** → публикация в GHCR
3. **Деплой на сервер** → запуск контейнера через SSH

### Настройка Secrets

Для работы CI/CD добавьте в Settings → Secrets:

- `SSH_HOST` — адрес сервера (89.104.74.189)
- `SSH_USER` — пользователь (root)
- `SSH_PRIVATE_KEY` — SSH-ключ для доступа к серверу
- `SSH_PORT` — порт SSH (22, опционально)

## 🛠️ Технологии

- **Python 3.11** — язык программирования
- **FastAPI** — веб-фреймворк
- **Uvicorn** — ASGI сервер
- **Docker** — контейнеризация
- **GitHub Actions** — CI/CD
- **GHCR** — GitHub Container Registry

## 📝 Лицензия

MIT
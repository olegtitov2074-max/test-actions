"""
Server Time API — FastAPI-сервис для получения текущего времени сервера.

Эндпоинты:
    GET /time  — текущее время UTC
    GET /date  — текущая дата и день недели
    GET /datetime — полная дата и время
"""

from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="Server Time API",
    description="API для получения текущего времени, даты и дня недели сервера",
    version="1.0.0",
)


@app.get("/time")
def get_server_time():
    """
    Возвращает текущее время сервера в формате ISO 8601.

    Returns:
        dict: Текущее UTC время и timestamp
    """
    now = datetime.now(timezone.utc)
    return {
        "utc": now.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "timestamp": now.timestamp(),
    }


@app.get("/date")
def get_server_date():
    """
    Возвращает текущую дату сервера и день недели.

    Returns:
        dict: Дата, день недели и timestamp
    """
    now = datetime.now(timezone.utc)
    return {
        "date": now.strftime("%Y-%m-%d"),
        "day_of_week": now.strftime("%A"),
        "timestamp": now.timestamp(),
    }


@app.get("/datetime")
def get_server_datetime():
    """
    Возвращает полную дату и время сервера.

    Returns:
        dict: Дата, время, день недели и timestamp
    """
    now = datetime.now(timezone.utc)
    return {
        "datetime": now.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "day_of_week": now.strftime("%A"),
        "timestamp": now.timestamp(),
    }
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="Server Time API")


@app.get("/time")
def get_server_time():
    """Возвращает текущее время сервера."""
    now = datetime.now(timezone.utc)
    return {
        "utc": now.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "timestamp": now.timestamp(),
    }


@app.get("/date")
def get_server_date():
    """Возвращает текущую дату сервера."""
    now = datetime.now(timezone.utc)
    return {
        "date": now.strftime("%Y-%m-%d"),
        "day_of_week": now.strftime("%A"),
        "timestamp": now.timestamp(),
    }


@app.get("/datetime")
def get_server_datetime():
    """Возвращает текущие дату и время сервера."""
    now = datetime.now(timezone.utc)
    return {
        "datetime": now.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "day_of_week": now.strftime("%A"),
        "timestamp": now.timestamp(),
    }

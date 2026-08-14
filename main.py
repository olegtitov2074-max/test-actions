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

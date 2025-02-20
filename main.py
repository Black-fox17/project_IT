from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import httpx
import asyncio
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model for website monitoring settings
class Setting(BaseModel):
    label: str
    type: str
    required: bool
    default: str

# Payload structure for monitoring request
class MonitorPayload(BaseModel):
    channel_id: str
    return_url: str
    settings: List[Setting]

async def fetch_dau_data(site: str) -> dict:
    """
    Fetches the daily active user (DAU) count from a given website's API.
    Modify the endpoint based on the actual analytics API being used.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{site}/api/dau", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return {"site": site, "dau": data.get("daily_active_users", 0)}
            else:
                return {"site": site, "error": f"Failed to fetch DAU (status {response.status_code})"}
    except Exception as e:
        return {"site": site, "error": str(e)}

async def monitor_dau_task(payload: MonitorPayload):
    sites = [s.default for s in payload.settings if s.label.startswith("site")]
    results = await asyncio.gather(*(fetch_dau_data(site) for site in sites))

    message = "\n".join(
        [
            f"{result['site']}: {result['dau']} active users"
            if "dau" in result
            else f"{result['site']}: {result['error']}"
            for result in results
        ]
    )

    data = {
        "message": message,
        "username": "DAU Monitor",
        "event_name": "Daily Active Users Report",
        "status": "success" if all("dau" in r for r in results) else "error"
    }

    async with httpx.AsyncClient() as client:
        await client.post(payload.return_url, json=data)

@app.get("/integration.json")
def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "data": {
            "author": "Blackfox",
            "date": {
                "created_at": "2025-02-13",
                "updated_at": "2025-02-13"
            },
            "descriptions": {
                "app_description": "A bot that monitors the number of daily active users (DAU) on a platform.",
                "app_logo": "https://img.icons8.com/?size=100&id=37410&format=png&color=000000",
                "app_name": "Telex DAU Monitor",
                "app_url": "",
                "background_color": "#ffffff"
            },
            "integration_category": "Analytics & Monitoring",
            "integration_type": "output",
            "is_active": True,
            "key_features": [
                "Receive messages from Telex channels.",
                "Fetch daily active users (DAU) from website analytics.",
                "Format messages based on predefined templates or logic.",
                "Send DAU reports back to the Telex channel.",
                "Log DAU tracking activity for auditing purposes."
            ],
            "permissions": {
                "events": [
                    "Receive messages from Telex channels.",
                    "Fetch DAU metrics from website analytics API.",
                    "Format DAU reports.",
                    "Send DAU updates back to the channel.",
                    "Log DAU tracking activity for auditing purposes."
                ]
            },
            "settings": [
                {"label": "site-1", "type": "text", "required": True, "default": ""}
            ],
            "tick_url": f"{base_url}/tick"
        }
    }

@app.post("/tick", status_code=202)
def monitor(payload: MonitorPayload, background_tasks: BackgroundTasks):
    background_tasks.add_task(monitor_dau_task, payload)
    return {"status": "accepted"}

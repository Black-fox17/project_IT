from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime,timezone,timedelta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
NIGERIA_TZ = timezone(timedelta(hours=1))
@app.get("/info")
@app.get("/info")
def get_info():
    return {
        "email": "ayeleru1234@gmail.com",
        "current_datetime": datetime.now(NIGERIA_TZ).isoformat(),
        "github_url": "https://github.com/Black-fox17/project_IT"
    }
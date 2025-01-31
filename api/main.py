from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime, timezone

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/info")
def get_info():
    response_data = {
        "email": "ayeleru1234@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "github_url": "https://github.com/Black-fox17/project_IT"
    }
    return JSONResponse(content=response_data)

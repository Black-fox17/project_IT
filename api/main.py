from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Allow all origins for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins instead of ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/info")
def get_info():
    return {
        "email": "ayeleru1234@gmail.com",
        "current_datetime": datetime.now().isoformat(),
        "github_url": "https://github.com/Black-fox17"
    }
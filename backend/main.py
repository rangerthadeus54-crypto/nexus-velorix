
from fastapi import FastAPI  # pyright: ignore[reportMissingImports]

app = FastAPI(
    title="NEXUS VELORIX API",
    description="Global Gaming Community Backend",
    version="1.0.0"
)


# HOME ENDPOINT
@app.get("/")
def home():
    return {
        "message": "Welcome to NEXUS VELORIX!",
        "status": "Online",
        "platform": "Gaming Community"
    }


# HEALTH CHECK ENDPOINT
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "backend": "FastAPI",
        "website": "NEXUS VELORIX"
    }


# API STATUS ENDPOINT
@app.get("/api/status")
def api_status():
    return {
        "success": True,
        "website": "NEXUS VELORIX",
        "backend": "FastAPI",
        "message": "Backend connection successful!"
    }

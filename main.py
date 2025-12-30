from fastapi import FastAPI
from app.api.v1.routes import payload_routes
app = FastAPI()

app.include_router(payload_routes.route, prefix="/api/v1")
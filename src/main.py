import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.http.routers import root_router as http_router

app = FastAPI(
    title="Example API",
    docs_url="/api/docs",
    openapi_url="/api/docs/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(http_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

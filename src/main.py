import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.http.routers import root_router as http_router
from api.midleware.db_sessions import DBSessionMiddleware

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

app.add_middleware(DBSessionMiddleware)

app.include_router(http_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

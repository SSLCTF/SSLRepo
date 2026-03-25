from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from core.api import api

app = FastAPI(
    title="SSL CTF API",
    description="API for SSL CTF",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.add_middleware(CORSMiddleware, allow_origins=[])
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")

app.include_router(api.router)
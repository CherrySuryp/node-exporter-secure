from typing import Annotated

from fastapi import Depends, FastAPI, status
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse

from app.auth import Auth
from app.config import Config
from app.dependiencies import RequestMetrics

config = Config()

auth = Auth(config.API_BEARER_TOKEN.get_secret_value())
metrics_dep = RequestMetrics(config.NODE_EXPORTER_METRICS_PATH.unicode_string())

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
if config.is_dev_env:
    app = FastAPI(title="Node-Exporter Secure")


app.add_middleware(GZipMiddleware, minimum_size=1024)  # noqa


@app.get(f"{config.METRICS_ROUTE}", dependencies=[Depends(auth)])
async def fetch_metrics(metrics: Annotated[metrics_dep, Depends()]) -> PlainTextResponse:
    return metrics


@app.get("/debug/healthcheck", tags=["Debug"])
async def health():
    return JSONResponse({"status": "OK"}, status_code=status.HTTP_200_OK)


@app.get("/debug/auth", dependencies=[Depends(auth)], tags=["Debug"])
async def auth():
    return {"status": "OK"}

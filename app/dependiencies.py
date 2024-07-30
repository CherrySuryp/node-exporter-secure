from typing import Optional

import aiohttp
from aiohttp.client_exceptions import ClientConnectorError
from fastapi import status
from fastapi.responses import PlainTextResponse


class RequestMetrics:
    def __init__(self, node_exporter_url: str):
        self._node_exporter_url = node_exporter_url

    async def _fetch_metrics(self) -> Optional[str]:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self._node_exporter_url) as resp:
                    if resp.status == 200:
                        return await resp.text("utf-8")
            except ClientConnectorError:
                pass

    async def __call__(self) -> PlainTextResponse:
        metrics = await self._fetch_metrics()
        if not metrics:
            return PlainTextResponse(
                content="COULDN'T COLLECT METRICS. CHECK IF NODE-EXPORTER WORKS AND CONFIGURED PROPERLY",
                status_code=status.HTTP_409_CONFLICT,
            )
        return PlainTextResponse(
            metrics, status_code=status.HTTP_200_OK, headers={"Cache-Control": "no-store, max-age=0, private"}
        )

"""Portfolio excerpt: generic asynchronous repository pattern.

The production database schema and queries are deliberately not included.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Protocol

from .snapshot_model import ServerSnapshot


class AsyncConnection(Protocol):
    async def execute(self, query: str, params: tuple = ()) -> object: ...
    async def commit(self) -> None: ...


class SnapshotRepository:
    """Demonstrates separation between domain objects and persistence."""

    def __init__(self, connection: AsyncConnection):
        self.connection = connection

    async def save(self, snapshot: ServerSnapshot) -> None:
        # SQL and production schema intentionally omitted from public showcase.
        payload = asdict(snapshot)
        await self._write_private(payload)

    async def _write_private(self, payload: dict) -> None:
        raise NotImplementedError("Production persistence implementation is private")

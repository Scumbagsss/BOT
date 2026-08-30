"""Portfolio excerpt: reduced immutable-style data model.

Field set is intentionally smaller than the production model.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class ServerSnapshot:
    status: str
    players: int | None
    max_players: int | None
    queue: int | None
    updated_at: datetime

    @property
    def is_online(self) -> bool:
        return self.status.upper() == "ONLINE"

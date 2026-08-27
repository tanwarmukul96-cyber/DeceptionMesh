from datetime import datetime, timezone
from pydantic import BaseModel, Field
from typing import Optional


class SecurityEvent(BaseModel):
    event_id: str
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    source_ip: str
    decoy: str
    action: str

    tool: Optional[str] = None
    command: Optional[str] = None
    target: Optional[str] = None

    interaction_depth: int = 1
    success: bool = False
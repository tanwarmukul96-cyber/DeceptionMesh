from datetime import datetime, timezone
from models.events import SecurityEvent


def collect_event(
    source_ip: str,
    decoy: str,
    action: str,
    tool: str | None = None,
    command: str | None = None,
    target: str | None = None,
    interaction_depth: int = 1,
    success: bool = False,
) -> SecurityEvent:

    event = SecurityEvent(
        event_id=f"evt-{int(datetime.now().timestamp() * 1000)}",
        timestamp=datetime.now(timezone.utc),
        source_ip=source_ip,
        decoy=decoy,
        action=action,
        tool=tool,
        command=command,
        target=target,
        interaction_depth=interaction_depth,
        success=success,
    )

    print(
        f"[EVENT] {event.event_id} | "
        f"{event.source_ip} | "
        f"{event.decoy} | "
        f"{event.action}"
    )

    return event
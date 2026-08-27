from collections import Counter
from models.events import SecurityEvent


def analyze_behaviour(events: list[SecurityEvent]) -> dict:
    if not events:
        return {
            "event_count": 0,
            "actions": [],
            "decoys_touched": [],
            "interaction_depth": 0,
            "behaviour": "unknown",
        }

    actions = Counter(event.action for event in events)
    decoys = sorted(set(event.decoy for event in events))
    max_depth = max(event.interaction_depth for event in events)

    if max_depth >= 4:
        behaviour = "deep_interaction"

    elif len(actions) >= 3:
        behaviour = "multi_stage_activity"

    elif len(events) >= 2:
        behaviour = "repeated_interaction"

    else:
        behaviour = "initial_probe"

    return {
        "event_count": len(events),
        "actions": dict(actions),
        "decoys_touched": decoys,
        "interaction_depth": max_depth,
        "behaviour": behaviour,
    }
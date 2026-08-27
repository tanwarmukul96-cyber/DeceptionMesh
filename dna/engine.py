from collections import Counter
from models.events import SecurityEvent
from dna.scoring import calculate_scores


class DeceptionDNA:
    def __init__(self):
        self.total_events = 0
        self.actions = Counter()
        self.decoys = Counter()
        self.tools = Counter()
        self.max_interaction_depth = 0

    def update(self, events: list[SecurityEvent]) -> dict:
        for event in events:
            self.total_events += 1
            self.actions[event.action] += 1
            self.decoys[event.decoy] += 1

            if event.tool:
                self.tools[event.tool] += 1

            self.max_interaction_depth = max(
                self.max_interaction_depth,
                event.interaction_depth,
            )

        snapshot = self.snapshot()

        scores = calculate_scores(
            event_count=self.total_events,
            interaction_depth=self.max_interaction_depth,
            unique_actions=len(self.actions),
            unique_decoys=len(self.decoys),
        )

        snapshot["risk"] = scores

        return snapshot

    def snapshot(self) -> dict:
        return {
            "total_events": self.total_events,
            "action_pattern": dict(self.actions),
            "decoys_interacted": dict(self.decoys),
            "tools_observed": dict(self.tools),
            "max_interaction_depth": self.max_interaction_depth,
        }
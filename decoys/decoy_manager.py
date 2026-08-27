from dataclasses import dataclass


@dataclass
class DecoyEnvironment:
    name: str
    services: list[str]
    interaction_level: int


DECOYS = {
    "fake-ssh": DecoyEnvironment(
        name="fake-ssh",
        services=["ssh"],
        interaction_level=1,
    ),

    "credential-decoy": DecoyEnvironment(
        name="credential-decoy",
        services=["ssh", "login"],
        interaction_level=2,
    ),

    "advanced-decoy": DecoyEnvironment(
        name="advanced-decoy",
        services=["ssh", "web-admin", "fake-files"],
        interaction_level=3,
    ),
}


class DecoyManager:

    def __init__(self):
        self.active_decoy = DECOYS["fake-ssh"]

    def activate(self, target: str) -> DecoyEnvironment:
        if target in DECOYS:
            self.active_decoy = DECOYS[target]

        return self.active_decoy

    def status(self) -> dict:
        return {
            "active_decoy": self.active_decoy.name,
            "services": self.active_decoy.services,
            "interaction_level": self.active_decoy.interaction_level,
        }
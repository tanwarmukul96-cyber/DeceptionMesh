TECHNIQUE_MAP = {
    "connection_attempt": {
        "id": "T1021",
        "name": "Remote Services",
    },
    "identification_received": {
        "id": "T1021",
        "name": "Remote Services",
    },
    "credential_probe": {
        "id": "T1110",
        "name": "Brute Force",
    },
    "resource_access": {
        "id": "T1083",
        "name": "File and Directory Discovery",
    },
}


def map_mitre_techniques(events: list) -> list:
    techniques = {}

    for event in events:
        mapping = TECHNIQUE_MAP.get(event.action)

        if mapping:
            key = mapping["id"]

            techniques[key] = {
                "id": mapping["id"],
                "name": mapping["name"],
                "observed_actions": [],
            }

            if event.action not in techniques[key]["observed_actions"]:
                techniques[key]["observed_actions"].append(event.action)

    return list(techniques.values())
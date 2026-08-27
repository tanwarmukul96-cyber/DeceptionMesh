from models.events import SecurityEvent
from core.deception_loop import DeceptionLoop


def main():
    loop = DeceptionLoop()

    print("\n=== ROUND 1: INITIAL ACTIVITY ===")

    events_round_1 = [
        SecurityEvent(
            event_id="evt-101",
            source_ip="127.0.0.1",
            decoy="fake-ssh",
            action="connection_attempt",
            tool="ssh",
            interaction_depth=1,
            success=True,
        ),
        SecurityEvent(
            event_id="evt-102",
            source_ip="127.0.0.1",
            decoy="fake-ssh",
            action="identification_received",
            tool="ssh",
            interaction_depth=2,
            success=True,
        ),
    ]

    result_1 = loop.process_events(events_round_1)

    print("Behaviour:", result_1["behaviour"])
    print("Risk:", result_1["dna"]["risk"]["risk_score"])
    print("Confidence:", result_1["dna"]["risk"]["confidence_score"])
    print("Adaptation:", result_1["adaptation"])
    print("Active Decoy:", result_1["active_decoy"])

    print("\n=== ROUND 2: DEEPER ACTIVITY ===")

    events_round_2 = [
        SecurityEvent(
            event_id="evt-103",
            source_ip="127.0.0.1",
            decoy="fake-admin",
            action="credential_probe",
            tool="ssh",
            interaction_depth=3,
            success=False,
        ),
        SecurityEvent(
            event_id="evt-104",
            source_ip="127.0.0.1",
            decoy="fake-backup",
            action="resource_access",
            tool="ssh",
            interaction_depth=4,
            success=True,
        ),
    ]

    result_2 = loop.process_events(events_round_2)

    print("Behaviour:", result_2["behaviour"])
    print("Risk:", result_2["dna"]["risk"]["risk_score"])
    print("Confidence:", result_2["dna"]["risk"]["confidence_score"])
    print("Adaptation:", result_2["adaptation"])
    print("Active Decoy:", result_2["active_decoy"])

    print("\n=== DNA EVOLUTION ===")
    print("Total Events:", result_2["dna"]["total_events"])
    print("Actions:", result_2["dna"]["action_pattern"])
    print("Decoys:", result_2["dna"]["decoys_interacted"])
    print("Max Interaction Depth:",
          result_2["dna"]["max_interaction_depth"])


if __name__ == "__main__":
    main()
from models.events import SecurityEvent
from services.behaviour_analyzer import analyze_behaviour
from dna.engine import DeceptionDNA
from adaptation.engine import adapt_environment
from reports.attacker_report import generate_report, save_report


def main():

    events = [
        SecurityEvent(
            event_id="evt-001",
            source_ip="127.0.0.1",
            decoy="fake-ssh",
            action="connection_attempt",
            tool="ssh",
            interaction_depth=1,
            success=True,
        ),

        SecurityEvent(
            event_id="evt-002",
            source_ip="127.0.0.1",
            decoy="fake-ssh",
            action="identification_received",
            tool="ssh",
            interaction_depth=2,
            success=True,
        ),

        SecurityEvent(
            event_id="evt-003",
            source_ip="127.0.0.1",
            decoy="fake-admin",
            action="credential_probe",
            tool="ssh",
            interaction_depth=3,
            success=False,
        ),

        SecurityEvent(
            event_id="evt-004",
            source_ip="127.0.0.1",
            decoy="fake-backup",
            action="resource_access",
            tool="ssh",
            interaction_depth=4,
            success=True,
        ),
    ]

    print("\n=== BEHAVIOUR ANALYSIS ===")

    behaviour = analyze_behaviour(events)

    for key, value in behaviour.items():
        print(f"{key}: {value}")

    print("\n=== DECEPTION DNA ===")

    dna = DeceptionDNA()

    dna_snapshot = dna.update(events)

    for key, value in dna_snapshot.items():
        print(f"{key}: {value}")

    print("\n=== DECEPTION ADAPTATION ===")

    decision = adapt_environment(
        behaviour=behaviour["behaviour"],
        risk_score=dna_snapshot["risk"]["risk_score"],
        interaction_depth=dna_snapshot["max_interaction_depth"],
    )

    print(f"Action: {decision.action}")
    print(f"Reason: {decision.reason}")
    print(f"Target: {decision.target}")

    print("\n=== ATTACKER INTELLIGENCE REPORT ===")

    report = generate_report(
        behaviour=behaviour,
        dna=dna_snapshot,
        adaptation=decision,
        events=events,
    )

    report_path = save_report(report)

    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()
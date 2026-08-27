from reports.mitre_mapper import map_mitre_techniques

from datetime import datetime
import json
from pathlib import Path


def generate_report(
    behaviour: dict,
    dna: dict,
    adaptation: dict,
    events: list,
) -> str:

    report = {
        "report_type": "DeceptionMesh Attacker Intelligence Report",
        "generated_at": datetime.now().isoformat(),

        "attacker_profile": {
            "behaviour": behaviour.get("behaviour", "unknown"),
            "event_count": dna.get("total_events", 0),
            "interaction_depth": dna.get("max_interaction_depth", 0),
            "tools_observed": dna.get("tools_observed", {}),
        },

        "deception_dna": dna,

        "risk_assessment": dna.get("risk", {}),

        "attack_timeline": [
            {
                "event_id": event.event_id,
                "source_ip": event.source_ip,
                "decoy": event.decoy,
                "action": event.action,
                "tool": event.tool,
                "interaction_depth": event.interaction_depth,
                "success": event.success,
            }
            for event in events
        ],

        "adaptation": {
            "action": adaptation.action,
            "reason": adaptation.reason,
            "target": adaptation.target,
        },

        "investigation_summary": (
            "Observed activity indicates potentially malicious interaction "
            "with the deception environment. Behavioural evidence and "
            "interaction depth should be investigated further."
        ),

        "mitre_attack_mapping": map_mitre_techniques(events),
    }

    return json.dumps(report, indent=4)


def save_report(report: str) -> str:

    output_dir = Path("reports/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = (
        output_dir /
        f"attacker_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    filename.write_text(report, encoding="utf-8")

    return str(filename)
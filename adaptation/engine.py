from dataclasses import dataclass


@dataclass
class AdaptationDecision:
    action: str
    reason: str
    target: str


def adapt_environment(
    behaviour: str,
    risk_score: int,
    interaction_depth: int,
) -> AdaptationDecision:

    if risk_score >= 75 or interaction_depth >= 4:
        return AdaptationDecision(
            action="increase_decoy_depth",
            reason="High-risk deep interaction detected",
            target="advanced-decoy",
        )

    if behaviour == "multi_stage_activity":
        return AdaptationDecision(
            action="expose_additional_service",
            reason="Multi-stage attacker behaviour detected",
            target="web-admin-decoy",
        )

    if behaviour == "repeated_interaction":
        return AdaptationDecision(
            action="increase_interaction_surface",
            reason="Repeated interaction indicates continued interest",
            target="credential-decoy",
        )

    return AdaptationDecision(
        action="maintain_decoy",
        reason="Insufficient behavioural evidence for mutation",
        target="current-decoy",
    )
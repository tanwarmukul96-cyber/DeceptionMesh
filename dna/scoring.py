def calculate_scores(
    event_count: int,
    interaction_depth: int,
    unique_actions: int,
    unique_decoys: int,
) -> dict:

    risk = (
        event_count * 5
        + interaction_depth * 10
        + unique_actions * 8
        + unique_decoys * 5
    )

    risk_score = min(risk, 100)

    confidence = (
        event_count * 8
        + interaction_depth * 12
        + unique_actions * 5
    )

    confidence_score = min(confidence, 100)

    if risk_score >= 75:
        risk_level = "CRITICAL"
    elif risk_score >= 50:
        risk_level = "HIGH"
    elif risk_score >= 25:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "confidence_score": confidence_score,
    }
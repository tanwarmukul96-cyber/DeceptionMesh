from dna.engine import DeceptionDNA
from adaptation.engine import adapt_environment
from decoys.decoy_manager import DecoyManager
from decoys.mutation_logger import MutationLogger

class DeceptionLoop:

    def __init__(self):
        self.dna = DeceptionDNA()
        self.mutation_logger = MutationLogger()
        self.decoy_manager = DecoyManager()

    def process_events(self, events):

        # 1. Continuously update Deception DNA
        dna_snapshot = self.dna.update(events)

        risk = dna_snapshot["risk"]["risk_score"]
        depth = dna_snapshot["max_interaction_depth"]

        # 2. Determine current attacker behaviour
        if depth >= 4:
            behaviour = "deep_interaction"

        elif len(dna_snapshot["action_pattern"]) >= 3:
            behaviour = "multi_stage_activity"

        elif len(events) >= 2:
            behaviour = "repeated_interaction"

        else:
            behaviour = "normal_interaction"

        # 3. Ask adaptation engine for a decision
        decision = adapt_environment(
            behaviour=behaviour,
            risk_score=risk,
            interaction_depth=depth,
        )

        # 4. Activate the selected decoy
        previous_decoy = self.decoy_manager.active_decoy.name
        active_decoy = self.decoy_manager.activate(
            decision.target
        )
        mutation = self.mutation_logger.record(
    previous_decoy=previous_decoy,
    new_decoy=active_decoy.name,
    action=decision.action,
    reason=decision.reason,
)

        # 5. Return complete adaptive state
        return {
            "dna": dna_snapshot,
            "mutation": mutation,
            "mutation_history": self.mutation_logger.get_history(),
            "behaviour": behaviour,

            "adaptation": {
                "action": decision.action,
                "reason": decision.reason,
                "target": decision.target,
            },

            "active_decoy": active_decoy.name,

            "decoy_status": self.decoy_manager.status(),
        }
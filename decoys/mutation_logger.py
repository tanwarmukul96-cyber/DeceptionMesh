from datetime import datetime


class MutationLogger:

    def __init__(self):
        self.history = []

    def record(self, previous_decoy, new_decoy, action, reason):
        mutation = {
            "timestamp": datetime.now().isoformat(),
            "previous_decoy": previous_decoy,
            "new_decoy": new_decoy,
            "action": action,
            "reason": reason,
        }

        self.history.append(mutation)

        return mutation

    def get_history(self):
        return self.history
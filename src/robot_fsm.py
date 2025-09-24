from transitions import Machine

class Robot:
    # Define states
    states = ["idle", "moving", "charging", "error"]

    def __init__(self, name="Robo1"):
        self.name = name
        self.machine = Machine(
            model=self,
            states=Robot.states,
            initial="idle"
        )

        # Define transitions
        self.machine.add_transition(trigger="start_moving", source="idle", dest="moving")
        self.machine.add_transition(trigger="stop", source="moving", dest="idle")
        self.machine.add_transition(trigger="low_battery", source="moving", dest="charging")
        self.machine.add_transition(trigger="charged", source="charging", dest="idle")
        self.machine.add_transition(trigger="fault", source="*", dest="error")
        self.machine.add_transition(trigger="reset", source="error", dest="idle")

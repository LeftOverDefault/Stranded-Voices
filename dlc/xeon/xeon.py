from dlc.dlc import DLC

class Xeon(DLC):
    def __init__(self) -> None:
        self.name = "Xeon"
        self.description = "description"
        self.initialized = False
        super().__init__(self.name, self.description, self.initialized)
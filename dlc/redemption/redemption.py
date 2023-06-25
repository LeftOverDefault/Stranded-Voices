from dlc.dlc import DLC

class Redemption(DLC):
    def __init__(self) -> None:
        self.name = "Redemption"
        self.description = "description"
        self.initialized = False
        super().__init__(self.name, self.description, self.initialized)
from dlc.dlc import DLC

class WorldBuilder(DLC):
    def __init__(self) -> None:
        self.name = "World Builder"
        self.description = "description"
        self.initialized = False
        super().__init__(self.name, self.description, self.initialized)
from dlc.dlc import DLC

class EnglishLover(DLC):
    def __init__(self) -> None:
        self.name = "English Lover"
        self.description = "description"
        self.initialized = False
        super().__init__(self.name, self.description, self.initialized)
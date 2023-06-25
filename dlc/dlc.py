class DLC:
    def __init__(self, name, description, initialized) -> None:
        self.name = name
        self.description = description
        self.initialized = initialized
    
    def Active(self) -> str:
        if self.initialized == True:
            return "O"
        else:
            return "X"
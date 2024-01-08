from abc import abstractmethod
import uuid 

class Task:

    def __init__(self, window=None, name=uuid.uuid4(), repeat=False) -> None:
        self.window = window
        self.name = name
        self.repeat=repeat

    @abstractmethod
    def run(self) -> None:
        ...

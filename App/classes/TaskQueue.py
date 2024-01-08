from Task import Task


class TaskQueue:

    def __init__(self) -> None:
        self.queue = []

    def addTask(self, task:Task, repeat=False):
        self.queue.append(task)
        return self

    def removeTask(self, task_name:str) -> Task | None:
        if len(self.queue) < 0:
            return None

        return self.queue.pop()

    def run(self) -> None: 
        while True:
            ...

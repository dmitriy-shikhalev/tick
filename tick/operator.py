from abc import ABC, abstractmethod


class Operator(ABC):
    @property
    def name(self):
        return self.__class__.__name__

    def __init__(self, data: list[tuple[str, str]]):
        self.data = data

    @abstractmethod
    async def apply(self):
        raise NotImplementedError

    @abstractmethod
    async def reverse(self):
        raise NotImplementedError

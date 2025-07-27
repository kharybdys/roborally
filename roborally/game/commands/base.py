from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseCommand(ABC, BaseModel):
    @abstractmethod
    def process(self):
        pass

from abc import ABC, abstractmethod
from typing import Dict


class PetListerControllerInterface(ABC):
    @abstractmethod
    def list_pets(self) -> Dict:
        pass
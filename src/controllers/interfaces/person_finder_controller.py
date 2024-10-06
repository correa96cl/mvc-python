from abc import ABC, abstractmethod
from typing import Dict


class PersonFinderControllerInterface(ABC):
    @abstractmethod
    def find(self, person_id: int) -> Dict:
        raise NotImplementedError
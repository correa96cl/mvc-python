from abc import ABC, abstractmethod
from typing import Dict


class PersonCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self, person_info: Dict) -> Dict:
        raise NotImplementedError
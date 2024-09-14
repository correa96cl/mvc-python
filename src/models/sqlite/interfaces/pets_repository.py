from abc import ABC, abstractmethod
from typing import List

from src.models.sqlite.entities.pets import PetsTable


class PetsRepositoryInterface(ABC):
    @abstractmethod
    def get_all_pets(self) -> List[PetsTable]:
        raise NotImplementedError

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        raise NotImplementedError
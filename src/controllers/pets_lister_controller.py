

from typing import Dict, List
from src.controllers.interfaces.pet_lister_controller import PetListerControllerInterface
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetsListerController(PetListerControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def list_pets(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pets_repository.get_all_pets()
        return pets
    
    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({
                "name": pet.name,
                "type": pet.type,
                "id": pet.id
            })
        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }

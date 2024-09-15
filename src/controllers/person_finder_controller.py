

from typing import Dict
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonFinderController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
       self.__people_repository = people_repository
    
    def find(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)
        response = self.__format_response(person)
        return response
    
    def __find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise Exception("Person not found")
        return person
    
    def __format_response(self, person: PeopleTable) -> Dict:
        return {
            "infos": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "Pet_type": person.pet_type, 
                    "age": person.age, 
                    "pet_id": person.pet_id
                }
            }
        }
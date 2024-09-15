import pytest
from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass

def test_create():
    person_infor = {
        "first_name": "belinha",
        "last_name": "belinha",
        "age": 77,
        "pet_id": 2
    }
    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_infor)
    assert response["infos"]["type"] == "Person"
    assert response["infos"]["count"] == 1
    assert response["infos"]["attributes"] == person_infor

def test_create_error():
    person_infor = {
        "first_name": "belinha2",
        "last_name": "belinha",
        "age": 77,
        "pet_id": 2
    }
    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception):
        controller.create(person_infor)

from src.controllers.person_finder_controller import PersonFinderController

class MockPerson():
    def __init__(self, first_name, last_name, age, pet_id) -> None:
        self.first_name = first_name,
        self.last_name = last_name,
        self.age = age,
        self.pet_id = pet_id
       

class MockPeopleRepository:
    def get_person(self, person_id: int):
        return MockPerson(
            first_name="belinha",
            last_name="belinha",
            age=77,
            pet_id=2
           )


def test_find():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(77)
    expected_response = {
        "infos": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "belinha",
                "last_name": "belinha",
                 "age": 77,
                "pet_id": 2,
               
               
            }
        }
        
    }
    
    print(response)
    print(expected_response)

    assert response == expected_response
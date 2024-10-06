from src.controllers.pets_lister_controller import PetsListerController
from src.models.sqlite.entities.pets import PetsTable


class MockPetsRepository:
        def list_pets(self):
            return [
                PetsTable(name="Fluffy", type="Cat", id=4),
                PetsTable(name="Spot", type="Dog", id=5),
            ]
    
        def test_list_pets():
            controller = PetsListerController(MockPetsRepository())
            response = controller.list_pets()

            expected_response = {
                "data": {
                    "type": "Pets",
                    "count": 2,
                    "attributes": [
                        {
                            "name": "Fluffy",
                            "type": "Cat",
                            "id": 4
                        },
                        {
                            "name": "Spot",
                            "type": "Dog",
                            "id": 5
                        }
                    ]
                }
            }

            print(response)
            print(expected_response)

            assert response == expected_response
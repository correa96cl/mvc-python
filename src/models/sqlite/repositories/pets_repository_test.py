from unittest import mock
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository
from mock_alchemy.mocking import UnifiedAlchemyMagicMock


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                     PetsTable(name="dog", type="dog"), 
                     PetsTable(name="cat", type="cat")
                    ],
                )
            ]
        )
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass


def test_get_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.get_all_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()
    assert response[0].name == "dog"
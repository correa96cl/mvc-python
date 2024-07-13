from unittest import mock
import pytest
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound


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

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_result_found
    
    def __raise_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")
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

def test_delete_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    name = "dog"
    repo.delete_pets(name)

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name==name)
    mock_connection.session.delete.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_get_pets_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    response = repo.get_all_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()
    assert response == []

def test_delete_pets_error():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    with pytest.raises(Exception):
        repo.delete_pets("name")
    mock_connection.session.rollback.assert_called_once()
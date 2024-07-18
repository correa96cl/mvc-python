
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable
from sqlalchemy.orm.exc import NoResultFound

class PeopleRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_person(
        self,
        first_name: str,
        last_name: str,
        age: int,
        pet_id: int
    ) -> None:
        with self.__db_connection as database:
            try:
                person_data = PeopleTable(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    pet_id=pet_id
                )
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def get_person(self, person_id: int) -> PeopleTable:
        with self.__db_connection as database:
            try:
                person = (
                    database.session.query(PeopleTable)
                    .outerjoin(PetsTable, PetsTable.id == PeopleTable.pet_id)
                    .filter(PeopleTable.id == person_id)
                    .with_entities(
                        PeopleTable.id,
                        PeopleTable.first_name,
                        PeopleTable.last_name,
                        PeopleTable.age,
                        PeopleTable.pet_id,
                        PetsTable.name.label("pet_name"),
                        PetsTable.name.label("pet_type")
                    ).all()
                )
                return person
            except NoResultFound:
                return None

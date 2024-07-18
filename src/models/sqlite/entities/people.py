from sqlalchemy import Column, ForeignKey, String, BIGINT
from src.models.sqlite.settings.base import Base

class PeopleTable(Base):
    __tablename__ = "people"
    id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, ForeignKey("pets.id"))

    def __repr__(self):
        return f"Person(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, age={self.age!r})"
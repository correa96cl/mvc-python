from sqlalchemy import Column, Integer, String, BIGINT
from src.models.sqlite.settings.base import Base

class PetsTable(Base):
    __tablename__ = "pets"

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f"Pets(id={self.id!r}, name={self.name!r}, type={self.type!r})"
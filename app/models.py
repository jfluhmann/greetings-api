from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.database import Base


class Greeting(Base):
    __tablename__ = "greeting"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(255), index=True)
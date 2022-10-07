from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship

from config.database import Base


class User(Base):
    """
        SQLAlchemy model for a User
    """

    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    birth_date = Column(Date)
    hashed_password = Column(String)

    tweets = relationship("Tweet", back_populates="user",
                          cascade="all, delete-orphan")

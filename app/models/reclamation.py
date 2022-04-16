import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.models.Enums.reclamationStatus import ReclamationStatus
from ..database import Base


class Reclamation(Base):
    __tablename__ = "reclamations"

    id = Column(Integer, primary_key=True, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    reclamation_status = Column(String, default=ReclamationStatus.pending)
    photo_url = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow())
    description = Column(String)

    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

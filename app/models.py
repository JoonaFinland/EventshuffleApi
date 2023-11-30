from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, index=True)
    possible_dates = Column(String)

    votes = relationship("Vote", back_populates="event")

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    voter_name = Column(String)
    date = Column(Date)
    event_id = Column(Integer, ForeignKey("events.id"))

    event = relationship("Event", back_populates="votes")

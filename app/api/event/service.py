from sqlalchemy import insert, select, delete
from app.models import Event, Vote
from app.core.database import execute, fetch_one, fetch_all

async def create_event(event_name: str, event_dates: list[str]):
    insert_query = (
        insert(Event)
        .values(event_name=event_name, possible_dates=event_dates)
        .returning(Event)
    )
    return await fetch_one(insert_query)

async def get_event(event_id: int):
    select_query = select(Event).where(Event.id == event_id)
    return await fetch_one(select_query)

async def get_all_events():
    select_query = select(Event)
    return await fetch_all(select_query)

async def delete_event(event_id: int):
    delete_query = delete(Event).where(Event.id == event_id)
    await execute(delete_query)

async def create_vote(event_id: int, voter_name: str, vote_dates: list[str]):
    insert_query = (
        insert(Vote)
        .values(event_id = event_id, voter_name=voter_name, date=vote_dates)
        .returning(Vote)
    )
    return await fetch_one(insert_query)

async def get_votes(event_id: int):
    select_query = select(Vote).where(Vote.event_id == event_id)
    return await fetch_all(select_query)
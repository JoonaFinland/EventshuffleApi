from fastapi import APIRouter, HTTPException
from .schema import Event, Vote
from .service import (
    create_event,
    get_event,
    get_all_events,
    delete_event,
    create_vote,
    get_votes
)
from .utils import (
    transform_votes,
    get_suitable_dates
)
router = APIRouter()

@router.get("/list")
async def event_list():
    events = await get_all_events()
    return {"events": [{"id": e.get("id"), "name": e.get('event_name')} for e in events]}

@router.post("/")
async def create_event_handler(event_data: Event):
    event = await create_event(event_data.name, event_data.dates)
    if event is not None:
        return {"id": event.get("id")}
    else:
        return {"error": "Event creation failed"}

@router.get("/{event_id}")
async def get_event_handler(event_id: int):
    event = await get_event(event_id)
    votes = await get_votes(event_id)
    if event:
        return {"id": event.get("id"),
                "name": event.get("event_name"),
                "dates": event.get("possible_dates"),
                "votes": transform_votes(votes)}
    else:
        raise HTTPException(status_code=404, detail="Could not find event")

@router.post("/{event_id}/vote")
async def create_vote_handler(event_id: int, vote_data: Vote):
    event = await get_event(event_id)
    if event:
        vote = await create_vote(event_id, vote_data.name, vote_data.dates)
        votes = await get_votes(event_id)
        return {"id": event.get("id"),
                "name": event.get("event_name"),
                "dates": event.get("possible_dates"),
                "votes": transform_votes(votes)}
    else:
        raise HTTPException(status_code=404, detail="Could not find event")

@router.get("/{event_id}/results")
async def vote_event(event_id: int):
    event = await get_event(event_id)
    if event:

        votes = await get_votes(event_id)
        votes = transform_votes(votes)
        suitable_dates = get_suitable_dates(votes)
        return {"id": event.get("id"),
                "name": event.get("event_name"),
                "suitableDates": suitable_dates}
    else:
        raise HTTPException(status_code=404, detail="Could not find event")

### TODO !!!!! ####
# Add validation support, i.e check if event exists when checking results
# Add support for actual datetime string format (simple iso)
# Get vote results should do some magic to get date will all votes
# When casting vote, check that the days are valid entries in the Event
####################
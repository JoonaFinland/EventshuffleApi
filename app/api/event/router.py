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
router = APIRouter()

@router.get("/list")
async def event_list():
    events = await get_all_events()
    return events

@router.post("/")
async def create_event_handler(event: Event):
    event = await create_event(event.name, event.dates)
    return {"event_id": event.get("id"), "event_name": event.get("event_name")}

@router.get("/{event_id}")
async def get_event_handler(event_id: int):
    event = await get_event(event_id)
    if event:
        return {"event_id": event.get("id"), "event_name": event.get("event_name")}
    else:
        raise HTTPException(status_code=404, detail="Could not find event")

@router.post("/{event_id}/vote")
async def create_vote_handler(event_id: int, vote: Vote):
    vote = await create_vote(event_id, vote.name, vote.dates)
    return {"vote_id": vote.get("id"), "voter_name": vote.get("voter_name")}

@router.get("/{event_id}/results")
async def vote_event(event_id: int):
    votes = await get_votes(event_id)
    return votes

### TODO !!!!! ####
# Add validation support, i.e check if event exists when checking results
# Add support for actual datetime string format (simple iso)
# Get vote results should do some magic to get date will all votes
# Get Event, should also get a list of all the votes for that event :)
# Adding vote needs to return the whole Event, just like get Event with votes
# Maybe some functionality if no date is found, some cool magic to get optimal
####################
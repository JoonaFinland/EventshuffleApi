from fastapi import APIRouter
from .models import Event, Vote
router = APIRouter()

@router.get("/list")
def event_list():
    return "event list"

@router.post("/")
def create_event(event: Event):
    return f"made new event {event.name}"

@router.get("/{event_id}")
def get_event(event_id: int):
    return f"getting event {event_id}"

@router.post("/{event_id}/vote")
def vote_event(event_id: int, vote: Vote):
    return f"voting event {event_id} by {vote.name}"

@router.get("/{event_id}/results")
def vote_event(event_id: int):
    return f"results for event {event_id}"
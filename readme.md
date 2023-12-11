# EventShuffle - Event Scheduling Simplified

EventShuffle is an application designed to simplify event scheduling with friends, providing a user-friendly alternative to tools like http://doodle.com. With VentShuffle, users can effortlessly create events, query available dates, and allow participants to submit their suitable dates.

## Features

- **Event Creation**: Easily create events by posting a name and suitable dates to the backend.
- **Event Querying**: Retrieve information about created events from the backend.
- **Participant Date Submission**: Participants can submit dates that are suitable for them.

## Requirements

- Docker
- Docker Compose

## Getting Started

Follow these steps to set up and run EventShuffle locally.

### 1. First-Time Setup

```bash
docker volume create --name=psql-dev
```
### 2. Start the Backend
```bash
docker-compose -f docker-compose.yaml up --build
```
### 3. Run Tests
```bash
docker-compose -f docker-compose-test.yaml up --build --exit-code-from test
```

## Usage
Once the backend is up and running, interact with the API to create and query events.

Example API Requests
### Create an Event:

```http
POST http://localhost:8000/events
Content-Type: application/json

{
  "name": "Birthday Party",
  "dates": ["2023-12-15", "2023-12-16"]
}
```
### Query Events:

```http
GET http://localhost:8000/events
```

### Submit Dates as a Participant:

```http
POST http://localhost:8000/events/1/participants
Content-Type: application/json

{
  "name": "John Doe",
  "dates": ["2023-12-15"]
}
```
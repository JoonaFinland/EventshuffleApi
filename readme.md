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

### 1. Copy sample.env to .env 

### 2. First-Time Setup
```bash
docker volume create --name=psql-dev
```
### 3. Start the Backend
```bash
docker-compose -f docker-compose.yaml up --build
```
### 4. Run Tests
```bash
docker-compose -f docker-compose-test.yaml up --build --exit-code-from test
```

## Usage
Once the backend is up and running, interact with the API to create and query events.

Docs: http://localhost:8000/docs

Example API Requests
### Create an Event:

```http
POST http://localhost:8000/api/v1/event
Content-Type: application/json

{
  "name": "Birthday Party",
  "dates": ["2023-12-15", "2023-12-16"]
}
```
### Query Events:

```http
GET http://localhost:8000/api/v1/event/list
```

### Query Single Event by Id:

```http
GET http://localhost:8000/api/v1/event/1
```

### Submit Dates as a Participant:

```http
POST http://localhost:8000/api/v1/event/1/vote
Content-Type: application/json

{
  "name": "John Doe",
  "dates": ["2023-12-15"]
}
```

### Get Suitable Dates:

```http
GET http://localhost:8000/api/v1/event/1/results
```
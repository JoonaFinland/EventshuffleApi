# from fastapi.testclient import TestClient
# import sys
# sys.path.insert(0, '/src') 
# import subprocess
# import pytest
# from src.main import app

# client = TestClient(app)

# def test_main():
#     response = client.get('/api/v1')
#     assert response.status_code == 200


# def test_events():
#     response = client.get('/api/v1/event/list')
#     assert response.status_code == 200

# def test_event_add():
#     response = client.post('/api/v1/event/', json={
#         "name": "Test Event",
#         "dates": ["Fri", "Mon"]
#     })
#     assert response.status_code == 200
import pytest
from async_asgi_testclient import TestClient
from fastapi import status

@pytest.mark.asyncio
async def test_index(client: TestClient) -> None:
    response = await client.get('/api/v1')
    assert response.status_code == 200

#### LIST EVENTS ####
@pytest.mark.asyncio
async def test_get_events(client: TestClient) -> None:
    response = await client.get('/api/v1/event/list')
    assert response.status_code == 200

#### CREATE EVENTS ####
@pytest.mark.asyncio
async def test_create_event_validation_error(client: TestClient) -> None:
    invalid_event_data = {"name": "", "dates": ["invalid-date"]}
    response = await client.post('/api/v1/event/', json=invalid_event_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_create_event(client: TestClient) -> None:
    event_data = {"name": "New Event", "dates": ["2023-12-31"]}
    response = await client.post('/api/v1/event/', json=event_data)
    print(response.text)
    assert response.status_code == 200

#### GET EVENT ####
@pytest.mark.asyncio
async def test_get_event_by_id(client: TestClient) -> None:
    event_id = 1
    response = await client.get(f'/api/v1/event/{event_id}')
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_event_by_id_not_found(client: TestClient) -> None:
    nonexistent_event_id = 99
    response = await client.get(f'/api/v1/event/{nonexistent_event_id}')
    assert response.status_code == 404

#### VOTE TESTS ####
@pytest.mark.asyncio
async def test_create_vote(client: TestClient) -> None:
    event_id = 1
    vote_data = {"name": "John Doe", "dates": ["2023-12-31"]}
    response = await client.post(f'/api/v1/event/{event_id}/vote', json=vote_data)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_create_vote_id_not_found(client: TestClient) -> None:
    event_id = 99
    vote_data = {"name": "John Doe", "dates": ["2023-12-31"]}
    response = await client.post(f'/api/v1/event/{event_id}/vote', json=vote_data)
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_create_vote_id_invalid_date(client: TestClient) -> None:
    event_id = 1
    vote_data = {"name": "John Doe", "choice": ["invalid-date"]}
    response = await client.post(f'/api/v1/event/{event_id}/vote', json=vote_data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_create_vote_id_bad_date(client: TestClient) -> None:
    event_id = 1
    vote_data = {"name": "John Doe", "choice": ["2020-01-01"]}
    response = await client.post(f'/api/v1/event/{event_id}/vote', json=vote_data)
    assert response.status_code == 422

#### EVENT RESULTS ####
@pytest.mark.asyncio
async def test_get_event_results(client: TestClient) -> None:
    event_id = 1
    response = await client.get(f'/api/v1/event/{event_id}/results')
    assert response.status_code == 200


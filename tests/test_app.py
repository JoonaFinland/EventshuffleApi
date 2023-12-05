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
    # resp = await client.post(
    #     "/auth/users",
    #     json={
    #         "email": "email@fake.com",
    #         "password": "123Aa!",
    #     },
    # )
    response = await client.get('/api/v1')
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_events(client: TestClient) -> None:
    response = await client.get('/api/v1/event/list')
    assert response.status_code == 200
from typing import Any, Generator, AsyncGenerator
import sys
sys.path.insert(0, '/src')
import pytest_asyncio
import pytest
from async_asgi_testclient import TestClient
from src.main import app
import asyncio

@pytest.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture()
async def client() -> AsyncGenerator[TestClient, None]:
    host, port = "127.0.0.1", "9000"
    scope = {"client": (host, port)}

    async with TestClient(app, scope=scope) as client:
        yield client
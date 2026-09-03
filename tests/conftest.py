import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def restore_activities():
    original_participants = {
        name: details["participants"].copy()
        for name, details in activities.items()
    }

    yield

    for name, participants in original_participants.items():
        activities[name]["participants"][:] = participants

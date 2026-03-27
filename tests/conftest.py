import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities before each test for isolation."""
    # Arrange
    original_activities = copy.deepcopy(app_module.activities)

    # Act
    app_module.activities = copy.deepcopy(original_activities)

    # Assert
    # Fixture setup complete; tests can now run against clean state.
    yield

    app_module.activities = copy.deepcopy(original_activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)

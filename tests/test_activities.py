def test_get_activities_returns_dictionary_payload(client):
    # Arrange
    expected_count = 9

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) == expected_count


def test_get_activities_contains_expected_activity_fields(client):
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    payload = response.json()
    first_activity = next(iter(payload.values()))
    assert required_keys.issubset(first_activity.keys())
    assert isinstance(first_activity["participants"], list)

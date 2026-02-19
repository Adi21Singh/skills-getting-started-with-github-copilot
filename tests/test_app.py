import pytest
from httpx import AsyncClient
from src.app import app

@pytest.mark.asyncio
def test_get_activities():
    # Arrange: (no setup needed for in-memory activities)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Act
        response = await ac.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

@pytest.mark.asyncio
def test_signup_activity():
    # Arrange
    test_email = "testuser@mergington.edu"
    activity_name = next(iter(app.activities)) if hasattr(app, 'activities') else list(app.state.activities.keys())[0]
    # Act
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(f"/activities/{activity_name}/signup?email={test_email}")
    # Assert
    assert response.status_code in (200, 400)  # 400 if already signed up

import uuid
from api.project_api import create_project

def test_create_project():
    project_name = f"Automation-{uuid.uuid4()}"

    response = create_project(project_name)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == project_name
    assert data["status"] == "active"
    assert data["id"]

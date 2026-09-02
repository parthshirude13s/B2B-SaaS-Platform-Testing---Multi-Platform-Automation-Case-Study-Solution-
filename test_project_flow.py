import os
import uuid
import requests
from playwright.sync_api import expect
from api.project_api import create_project, delete_project

BASE_URL = os.getenv("BASE_URL", "https://qa.workflowpro.com")
API_URL = os.getenv("API_URL")
COMPANY2_TOKEN = os.getenv("COMPANY2_TOKEN")

def test_project_creation_and_tenant_isolation(page):
    project_name = f"Automation-{uuid.uuid4()}"

    response = create_project(project_name)
    assert response.status_code == 201

    project = response.json()
    project_id = project["id"]

    try:
        page.goto(
            f"{BASE_URL}/projects/{project_id}",
            wait_until="domcontentloaded"
        )
        expect(page.get_by_text(project_name)).to_be_visible()

        other_tenant_response = requests.get(
            f"{API_URL}/api/v1/projects/{project_id}",
            headers={
                "Authorization": f"Bearer {COMPANY2_TOKEN}",
                "X-Tenant-ID": "company2"
            },
            timeout=10
        )

        assert other_tenant_response.status_code in [403, 404]

    finally:
        delete_project(project_id)

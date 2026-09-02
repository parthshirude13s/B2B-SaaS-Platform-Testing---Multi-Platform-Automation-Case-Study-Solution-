import os
import requests

API_URL = os.getenv("API_URL")
COMPANY1_TOKEN = os.getenv("COMPANY1_TOKEN")

def create_project(project_name):
    response = requests.post(
        f"{API_URL}/api/v1/projects",
        headers={
            "Authorization": f"Bearer {COMPANY1_TOKEN}",
            "X-Tenant-ID": "company1"
        },
        json={
            "name": project_name,
            "description": "Created by automation",
            "team_members": []
        },
        timeout=10
    )
    return response

def delete_project(project_id):
    response = requests.delete(
        f"{API_URL}/api/v1/projects/{project_id}",
        headers={
            "Authorization": f"Bearer {COMPANY1_TOKEN}",
            "X-Tenant-ID": "company1"
        },
        timeout=10
    )
    return response

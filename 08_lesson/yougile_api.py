import requests


class YougileApi:

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str):
        payload = {"title": title}
        response = requests.post(
            f"{self.base_url}/api-v2/projects",
            headers=self.headers,
            json=payload
        )
        return response

    def get_project_by_id(self, project_id: str):
        response = requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers
        )
        return response

    def update_project(self, project_id: str, new_title: str):
        payload = {"title": new_title}
        response = requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers,
            json=payload
        )
        return response

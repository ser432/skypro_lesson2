import os
import pytest
import requests
from yougile_api import YougileApi

LOGIN = os.getenv("YOUGILE_LOGIN", "YOUR_LOGIN_HERE")
PASSWORD = os.getenv("YOUGILE_PASSWORD", "YOUR_PASSWORD_HERE")
BASE_URL = "https://ru.yougile.com"


@pytest.fixture(scope="module")
def api():
    # 1. Получаем список компаний пользователя
    comp_creds = {
        'login': LOGIN,
        'password': PASSWORD
    }
    resp_comp = requests.post(
        f"{BASE_URL}/api-v2/auth/companies", json=comp_creds
    )
    assert resp_comp.status_code == 200, "Ошибка получения списка компаний"
    companies = resp_comp.json().get('content', [])
    assert len(companies) > 0, "Список компаний пуст"
    company_id = companies[0]['id']

    # 2. Получаем токен по companyId
    key_creds = {
        'login': LOGIN,
        'password': PASSWORD,
        'companyId': company_id
    }
    resp_key = requests.post(f"{BASE_URL}/api-v2/auth/keys", json=key_creds)
    assert resp_key.status_code == 201, "Ошибка получения токена"
    token = resp_key.json()['key']

    # 3. Возвращаем настроенный экземпляр класса
    return YougileApi(BASE_URL, token)


# --- Авторизационные тесты ---
def test_auth():
    creds = {'login': LOGIN, 'password': PASSWORD}
    resp = requests.post(f"{BASE_URL}/api-v2/auth/companies", json=creds)
    assert resp.status_code == 200


def test_get_token():
    comp_resp = requests.post(
        f"{BASE_URL}/api-v2/auth/companies",
        json={'login': LOGIN, 'password': PASSWORD}
    )
    companies = comp_resp.json().get('content', [])
    assert len(companies) > 0
    company_id = companies[0]['id']

    key_resp = requests.post(
        f"{BASE_URL}/api-v2/auth/keys",
        json={'login': LOGIN, 'password': PASSWORD, 'companyId': company_id}
    )
    assert key_resp.status_code == 201
    assert "key" in key_resp.json()


# --- CRUD тесты над проектами ---
def test_create_project_positive(api):
    response = api.create_project("Test Project Auto")
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_project_by_id_positive(api):
    create_res = api.create_project("Project for Get Test")
    project_id = create_res.json()["id"]

    response = api.get_project_by_id(project_id)
    assert response.status_code == 200
    assert response.json()["title"] == "Project for Get Test"


def test_update_project_positive(api):
    create_res = api.create_project("Old Title Project")
    project_id = create_res.json()["id"]

    response = api.update_project(project_id, "Updated Title Project")
    assert response.status_code == 200

    get_res = api.get_project_by_id(project_id)
    assert get_res.json()["title"] == "Updated Title Project"


def test_create_project_negative_empty_title(api):
    response = api.create_project("")
    assert response.status_code == 400


def test_get_project_by_id_negative_invalid_id(api):
    response = api.get_project_by_id("non_existent_id_12345")
    assert response.status_code in [400, 404, 440]


def test_update_project_negative_invalid_id(api):
    response = api.update_project("non_existent_id_12345", "New Title")
    assert response.status_code in [400, 404, 440]

# -*- coding: utf-8 -*-
import unittest
import secrets
from starlette.testclient import TestClient

from app.com_lib.file_functions import save_json
from app.main import app

client = TestClient(app)
directory_to__files: str = "data"

# api/v1/groups/list?delay=1&qty=10&offset=1&active=true&groupType=approval
class Test(unittest.TestCase):
    def test_groups_get_list_error_delay(self):
        url = f"/api/v1/groups/list?delay=122"

        response = client.get(url)
        assert response.status_code == 422

    def test_groups_get_list_error_qty(self):
        url = f"/api/v1/groups/list?qty=501"

        response = client.get(url)
        assert response.status_code == 422

    def test_groups_get_list_error_type(self):
        url = f"/api/v1/groups/list?groupType=bob"

        response = client.get(url)
        assert response.status_code == 422

    def test_groups_get_list_all_options(self):

        url = f"/api/v1/groups/list?delay=1&qty=10&offset=1&active=true&groupType=approval"

        response = client.get(url)
        assert response.status_code == 200

    def test_groups_get_list(self):

        url = f"/api/v1/groups/list"

        response = client.get(url)
        assert response.status_code == 200
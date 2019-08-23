# -*- coding: utf-8 -*-
import datetime
import os
import json
from pathlib import Path
import sys
import time
import unittest
from unittest import mock
import requests
from requests.exceptions import Timeout
import requests_mock
from loguru import logger
import pytest
from app.main import app
from app.com_lib.file_functions import open_json, save_json

# from starlette.responses import HTMLResponse
from starlette.testclient import TestClient

# from starlette.exceptions import HTTPException

client = TestClient(app)

directory_to__files: str = "data"


class test_default_endpoints(unittest.TestCase):
    def test_todos_post_exception(self):
        test_data = {
            # "title": "Test",
            "userId": "123",
            "description": "test",
            "dateDue": "2019-08-22T23:51:28.873Z",
        }
        url = f"/api/v1/todo/create/"
        client = TestClient(app)
        response = client.post(url, json=test_data)
        # result = response.json()
        assert response.status_code == 422
        # data = response.json()
        # save_json("test_data_todos.json", data)

    def test_todos_post(self):
        test_data = {
            "title": "Test",
            "userId": "123",
            "description": "test",
            "dateDue": "2019-08-22T23:51:28.873Z",
        }
        url = f"/api/v1/todo/create/?delay=1"
        client = TestClient(app)
        response = client.post(url, json=test_data)
        assert response.status_code == 200
        data = response.json()
        save_json("test_data_todos.json", data)

    def test_todos_count(self):
        client = TestClient(app)
        response = client.get(f"api/v1/todo/list/count")
        assert response.status_code == 200

    def test_todos_count_complete_delay(self):
        client = TestClient(app)
        response = client.get(f"/api/v1/todo/list/count?delay=1&complete=true")
        assert response.status_code == 200

    def test_todos_list(self):
        client = TestClient(app)
        response = client.get(f"/api/v1/todo/list")
        assert response.status_code == 200

    def test_todos_list_options(self):
        client = TestClient(app)
        response = client.get(f"/api/v1/todo/list?delay=1&complete=true")
        assert response.status_code == 200

    def test_todos_error_delay(self):
        client = TestClient(app)
        response = client.get(f"/api/v1/todo/list?delay=122")
        assert response.status_code == 422

    def test_todos_id(self):
        todo_id = open_json("test_data_todos.json")
        client = TestClient(app)
        response = client.get(f"/api/v1/todo/{todo_id['todoId']}")
        assert response.status_code == 200

    def test_todos_id_delay(self):
        todo_id = open_json("test_data_todos.json")
        client = TestClient(app)
        response = client.get(f"/api/v1/todo/{todo_id['todoId']}?delay=1")
        assert response.status_code == 200

    def test_todos_put_complete_delay(self):
        todo_id = open_json("test_data_todos.json")
        client = TestClient(app)
        response = client.put(f"/api/v1/todo/complete/{todo_id['todoId']}?delay=1")
        assert response.status_code == 200

    def test_todos_delete_delay(self):
        todo_id = open_json("test_data_todos.json")
        client = TestClient(app)
        response = client.delete(f"/api/v1/todo/{todo_id['todoId']}?delay=1")
        assert response.status_code == 200

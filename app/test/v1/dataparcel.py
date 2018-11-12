from ...app import app
import unittest
import json


class TestDataParcel(unittest.TestCase):
    def setUp(self):
        create_app().testing = True
        self.app = app.test_client
        self.data = {
            "sender_name": "stephler"
        }

    def test_post(self):
        response = self.app.post("api/v1/parcel")
        result = json.load(response.data)
        self.assertEqual(response.status_code, 201)

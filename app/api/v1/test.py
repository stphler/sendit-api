import unittest
import os
import json
from app import create_app


class TestDataParcel(unittest.TestCase):

    def setUp(self):
        app = create_app()
        self.client = app.test_client()
        self.data = {
        "id": 1,
        "sender_name": "Muthoni",
        "user_id": 10,
        "recipient": "Auma",
        "destination": "Nyeri",
        "weight": "50",
        "pickup": "Nairobi CBD",
        "location": "Nairobi",
        "status": "pending"
        }

    def test_post_parcel(self):
        res = self.client.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(res.data)
        self.assertEqual(result['Message'], "Parcel Created")
        self.assertEqual(res.status_code, 201)

    def test_get_all_parcels(self):
        res = self.client.get('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(res.data)
        self.assertEqual(result['Message'], "Success")
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()

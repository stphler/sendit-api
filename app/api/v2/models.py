parcles = []


class DataParcel(object):
    """docstring for  DataParcel"""

    def __init__(self):
        self.db = init__db()

    def save(self, sende_name, adddress):
        payload = {
            "id": len(self.db) + 1,
            "sender_name": sender_name
        }
query="""

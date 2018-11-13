from flask_restful import Resource
from .models import DataParcel


class OrderParcel(Resource, DataParcel):
    """This class contains data parcels without
    any specificity."""

    def __init__(self):
        self.parcel = DataParcel()

    def get(self):
        parcel = self.parcel.get_all()
        return parcel


class OneParcel(Resource, DataParcel):
    """This class contains methods for manipulating a specific parcel"""

    def __init__(self):
        self.parcel = DataParcel()

    def get(self, id):

        parcel = self.parcel.get_parcel(id)
        return parcel

    def post(self):
        add = self.parcel.add_parcel()
        return add

    def put(self, id):

        new = self.parcel.change_location(id)
        return new

    def delete(self, id):

        self.parcel.delete_parcel(id)
        return {"Success": "Delivery {} was successfully deleted".format(id)}


class User(Resource, DataParcel):

    def __init__(self):
        self.parcel = DataParcel()

    def get(self, sender):

        package = self.parcel.get_theirs(sender_name)
        if package['sender_name'] == sender_name:
            return {"parcels": package}
        else:
            return "No Parcel by {}".format(sender_name)

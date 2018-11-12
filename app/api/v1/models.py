from flask import request

# this is where all our parcels delivery orders will be posted
parcels = [
{
        "id": 1,
        "sender_name": "Muthoni",
        "user_id": 10,
        "recipient": "Auma",
        "destination": "Nyeri",
        "weight": "50",
        "pickup": "Nairobi CBD",
        "location": "Nairobi",
        "status": "pending"
    }, {
        "id": 2,
        "sender_name": "Steve",
        "user_id": 11,
        "recipient": "JAMES",
        "destination": "Kiambu",
        "weight": "20",
        "pickup": "Nakuru",
        "location": "Nakuru",
        "status": "pending"
    },

]


class DataParcel(object):
    """This is the Dataparcel class with its attributes"""

    def __init__(self, sender_name, recipient, destination, weight, pickup, status):
        self.db = parcels
        self.sender = sender
        self.recipient = recipient
        self.destination = destination
        self.weight = weight
        self.pickup = pickup

    def add_parcel(self):
        """The method to create a delivery order and adding
            it to our list"""

        # to validate whether the user has enough information
        if not request.json():
            return {"Error": "Bad request"}, 400
        if not request.json['sender']:
            return {"Error": "Please include your sender_name"}, 400
        if not request.json["recipient"]:
            return {"Error": "Please include the recipient of the package"}, 400
        if not request.json["destination"]:
            return {"Error": "You must specify a destination for the parcel delivery"}, 400
        if not request.json["weight"]:
            return {"Error": "You must specify the weight of the parcel"}, 400
        if not request.json["pickup"]:
            return {"Error": "What is the pickup location?"}, 400

        payload = {
            'id': len(parcels) + 1,
            'sender': request.json['sender'],
            'recipient': request.json['recipient'],
            'destination': request.json['destination'],
            'weight': request.json['weight'],
            'pickup': request.json['pickup'],
            'status': request.json['Success']
        }

        self.db.append(payload)
        return {"Success": "Added Parcel" + payload}, 201

    def get_all(self):
        """Defines the method to get all parcel deliveries in the dataset"""
        return {"parcels": self.db}, 200

    def get_parcel(self, id):
        """Defines method to get a specific delivery with it's key/id"""
        for parcel in self.db:
            if parcel['id'] == id:
                return parcel, 200
            else:
                return {"Error": "No delivery exists with that parcel id."}, 404

    def get_theirs(self, sender):
        """"method for getting all deliveries from a specific
        sender_name"""
        if not request.json("sender_name"):
            return {"Error": "Please include your sender"}
        for parcel in parcels:
            if parcel["sender_name"] == sender_name:
                return {"Parcels by {}".format(sender_name), parcel}, 200
        else:
            return "No delivery by {}".format(sender_name), 404

    def delete_parcel(self, id):
        """Describes the method for deleting a specific delivery from the
        dataset"""
        for parcel in self.db:
            if len(parcel) == 0:
                return {"message": "Delivery not found."}, 400
            elif parcel['id'] == id:
                self.db.remove(parcel)
                return {"Success": "Delivery successfully deleted."}, 200
            else:
                return {"Error": "No delivery exists with that id."}, 404

    def change_location(self, id):
        """Defines the method for changing the
        current location of a delivery"""
        for parcel in parcels:
            if parcel["id"] == id:
                if not request.json["location"]:
                    return {"Error": "You must add a location"}, 400
                else:
                    location = request.json["location"]
                    parcel["location"] = location
                    return parcel, 201
            else:
                return "Parcel not found", 404

    def change_destination(self, id):
        if not request.json["destination"]:
            return {"Error": "Please enter your new destination"}, 400
        new = request.json["destination"]
        for parcel in parcels:
            if parcel["id"] == id:
                parcel["destination"] = new
                return {"Success": "Destination successfully changed" + parcel}, 200
class CancelOrder(Resource, Dataparcel):
    def put(self, parcelId):
        '''
        Cancel an order
        '''
        parcel = DataOrder().get_parcel(parcelId)
        if not parcel:
            return {'message': 'parcel missing'}, 404
        parcel.status = 'cancelled'
        return {
            "message":"parcel cancellationed successfully",
            "parcel cancelled":parcel.__dict__
            }, 200
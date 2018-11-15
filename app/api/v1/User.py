from flask_restful import Resource
class SignUp(Resource, ParcelModel):

    """docstring for SignUp"""

    def post(self):
        data = request.get_json()
        user_id = len(users) + 1
        self.name = data["name"]
        self.email = data["email"]
        self.password = data["password"]
        self.repeatpassword = data["repeatpassword"]

        user = {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "repeatpassword": self.repeatpassword
        }

        users.append(user)

        return make_response(jsonify({
            "status": "Ok",
            "message": "Account created succefully",
            "user": "users"
        }, 201

        ))

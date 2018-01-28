from werkzeug.security import safe_str_cmp
from resources.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user # Everything is alright. So generate a JWT token

def identity(payload):
    user_id = payload['identity'] # Check the JWT token to make sure its correct
    return UserModel.find_by_id(user_id)

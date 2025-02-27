from jwt import DecodeError
import jwt
from mysite.settings import JWT_KEY


class JwtToken:

    @classmethod
    def generate(cls, user):
        token = jwt.encode(
            payload={
                "user_id": user.id,
            },
            algorithm="HS256",
            key=JWT_KEY,
        )
        return token

    @classmethod
    def decode(cls, token):
        jwt_token = jwt.decode(
            jwt=token,
            algorithms="HS256",
            key=JWT_KEY,
        )
        return jwt_token

    @classmethod
    def validate(cls, token):
        try:
            cls.decode(token=token)
            return True
        except DecodeError:
            return False

    @classmethod
    def get_user_id(cls, token):
        jwt_token = cls.decode(token=token)
        return jwt_token["user_id"]

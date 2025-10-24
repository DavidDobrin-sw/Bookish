from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from bookish.services.auth_service import create_user, verify_user

bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@bp.post("/register")
def register():
    if not request.is_json:
        return {"error": "JSON required"}, 415
    data = request.get_json()

    try:
        user = create_user(data.get("email"), data.get("password"))
    except ValueError as e:
        return {"error": str(e)}, 409
    token = create_access_token(identity=user.id)

    return {"access_token": token}, 201

@bp.post("/login")
def login():
    if not request.is_json:
        return {"error": "JSON required"}, 415

    data = request.get_json()
    user = verify_user(data.get("email"), data.get("password"))

    if not user:
        return {"error": "Invalid credentials"}, 401

    token = create_access_token(identity=user.id)
    return {"access_token": token}, 200

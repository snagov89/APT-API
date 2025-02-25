from flask import request, Blueprint
import logging

from app import limiter
from app.services.encoding import EncodeApt
from app.services.token_handling import TokenHandling

encode_api_blueprint = Blueprint("encode_api", __name__)

@encode_api_blueprint.route("/encode", methods=["POST"])
@limiter.limit("1 per 2 seconds", per_method=True)
def encode():
    """encode route
    Requires:
        image file
        token
    Returns:
        file: wav audio file
    """
    try:

        image_file = request.files.get("image")
        if not image_file:
            return {"status":'error',"msg": "No image file provided."}

        token = request.form.get("token")
        if not token:
            return {"status":'error',"msg": "No token provided."}

        if not TokenHandling().verifyToken(token):
            return {"status":'error',"msg": "Invalid token."}
        
        return encode_audio(image_file)
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"message": "An error occurred."}, 500

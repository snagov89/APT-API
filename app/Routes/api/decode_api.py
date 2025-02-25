from flask import request, Blueprint
import logging

from app import limiter
from app.services.decoding import decode_audio
decode_api_blueprint = Blueprint("decode_api", __name__)

@decode_api_blueprint.route("/decode", methods=["POST"])
@limiter.limit("1 per 2 seconds", per_method=True)
def decode():
    """Decode route
    Requires:
        audio file
        token
    Returns:
        file: image
    """
    try:

        audio_file = request.files.get("audio")
        if not audio_file:
            return {"status":"error","message": "No audio file provided."}

        token = request.form.get("token")
        if not token:
            return {"status":"error","message": "No token provided"}

        
        image = decode_audio(audio_file, token)

        return image
    except Exception as e:
        logging.error(f"Error: {e}")
        return {'status':'error','msg':'An error occurred.'}

from flask import request, Blueprint,send_file
import logging
import io

from app import limiter
from app.services.decoding import DecodeApt
from app.services.token_handling import TokenHandling
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

        TokenHandling().track_requests(token,"encode")
        image_data = DecodeApt().decode_audio(audio_file)
        img_io = io.BytesIO(image_data)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        logging.error(f"Error: {e}")
        return {'status':'error','msg':'An error occurred.'}

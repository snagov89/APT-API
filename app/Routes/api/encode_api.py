from flask import request, Blueprint,send_file,jsonify
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
        image_file_1 = request.files.get("image_1")
        image_file_2 = request.files.get("image_2")
        if not image_file_1:
            return {"status":'error',"msg": "No image file provided."}

        token = request.form.get("token")
        if not token:
            return {"status":'error',"msg": "No token provided."}
        if not TokenHandling().verify_token(token):
            return {"status":'error',"msg": "Invalid token."}
        status = EncodeApt().encode_apt(image_file_1,image_file_2=image_file_2)
        if 'file' in status:
            wav_file_path = status['file']
            del status['file']
        TokenHandling().track_requests(token,"encode")
        return send_file(
            wav_file_path,
            as_attachment=True,
            download_name="encoded_audio_data.wav"
        )

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"status":'error',"message": "Backend error"})

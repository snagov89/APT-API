from pydub import AudioSegment
from io import BytesIO

class Validator:
    def is_valid_audio_file(self, audio_file: bytes) -> bool:
        """Function that checks if the file is a valid audio file
        """
        try:
            audio = AudioSegment.from_file(BytesIO(audio_file))
            return True
        except Exception:
            return False


import logging

class DecodeApt:

    def decode_audio(self,audio:bytes) -> str:
        """Decode audio function

        Args:
            audio (bytes): Audio file

        Returns:
            str: _description_
        """
        try:
            return "Decoded audio file"
        except Exception as err:
            logging.error(f"Error: {err}")
            return {"status":'error',"msg": "An error occurred."}
    
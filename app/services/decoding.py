import os
import logging

from app.models.salt import GenSalt

class DecodeApt:
    def decode_audio(self, audio:bytearray) -> str:
        """
        This decode API route uses noaa-apt to decode the audio file.
        The implemention i made from scratch does not compare to the noaa-apt results.
        
        Args:
            audio (bytearray): The audio file to decode.

        returns:
            str: path of the image file
        """
        try:
            saved_temp_audio_file = os.path.join(os.getcwd(),"app","data","encoded_data", f"temp_{GenSalt().gen_salt()}.wav")
            saved_temp_image_file = os.path.join(os.getcwd(),"app","data","encoded_data", f"temp_{GenSalt().gen_salt()}.png")
            with open(saved_temp_audio_file, "wb") as f:
                f.write(audio.read())
            print({os.path.join(os.getcwd(),"app","bin","noaa-apt")})
            os.system(f"{os.path.join(os.getcwd(),"app","bin","noaa-apt")} {saved_temp_audio_file} -o {saved_temp_image_file}")            

            with open(saved_temp_image_file, "rb") as f:
                image_data = f.read()
            return image_data
        except Exception as err:
            logging.error(f"Decoding error: {err}")
            return None
        finally:
            if os.path.exists(saved_temp_audio_file):
                os.remove(saved_temp_audio_file)
            if os.path.exists(saved_temp_image_file):
                os.remove(saved_temp_image_file)
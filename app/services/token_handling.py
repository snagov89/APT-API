
import logging
from app.models.salt import GenSalt
from app.repository.token_handling import TokenHandling

token_repo = TokenHandling()
class TokenHandling:

    def generate_token(self) -> dict[str,str]:
        try:
            token = GenSalt().gen_salt(20)
            token_repo.insert_new_token(token)
            return {"status":'success',"token": token}
        except Exception as err:
            logging.error(f"Error: {err}")
            return {"status":'error',"msg": "An error occurred."}


    def verifyToken(self,token:str) -> bool:
        try:
            token_validity = token_repo.check_token(token)
            return token_validity
        except Exception as err:
            logging.error(f"Error: {err}")
            return {"status":'error',"msg": "An error occurred."}
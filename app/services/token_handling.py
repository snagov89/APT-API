
import logging
from app.models.salt import GenSalt
from app.repository.token_handling import TokenHandleDb

token_repo = TokenHandleDb()
class TokenHandling:

    def generate_token(self) -> dict[str,str]:
        try:
            token = GenSalt().gen_salt(20)
            token_repo.insert_new_token(token)
            return {"status":'success',"token": token}
        except Exception as err:
            logging.error(f"Error: {err}")
            return {"status":'error',"msg": "An error occurred."}

    def track_requests(self,token:str,action:str) -> dict[str,str]:
        try:
            token_repo.track_requests(token,action)
            return {"status":'success',"msg": "success"}
        except Exception as err:
            logging.error(f"Error: {err}")
            return {"status":'error',"msg": "An error occurred."}

    def verify_token(self,token:str) -> bool:
        try:
            token_validity = token_repo.check_token(token)
            if token_validity['status'] == 'ok':
                return True
            return False
        except Exception as err:
            logging.error(f"Error: {err}")
            return {"status":'error',"msg": "An error occurred."}
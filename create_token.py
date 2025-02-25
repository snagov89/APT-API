from app.repository.token_handling import TokenHandleDb
from app.models.salt import GenSalt

salt = GenSalt().gen_salt(20)
token = TokenHandleDb().insert_new_token(salt)
if token['status'] == 'ok':
    print(f"Token: {salt}")
else:
    print('Failed !')
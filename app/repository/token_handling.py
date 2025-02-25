from datetime import datetime

class TokenHandling(BaseMongo):
    def __init__(self) -> None:
        super().__init__()
        self.tokens = self.db['tokens']
    
    def insert_new_token(self,token:str) -> dict[str,str]:
        self.tokens.insert_one({"token":token,"created_at":datetime.now()})
        return {"status":'ok','msg':'success'}

    def check_token(self,token:str) -> dict[str,str]:
        token = self.tokens.find_one({"token":token})
        if token:
            return {"status":'ok','msg':'success'}
        return {"status":'error','msg':'Token not found'}
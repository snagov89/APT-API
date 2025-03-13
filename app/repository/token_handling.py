from datetime import datetime
from app.repository.base_mongo import BaseMongo

class TokenHandleDb(BaseMongo):
    def __init__(self) -> None:
        super().__init__()
        self.tokens = self.db['tokens']
        self.actions = self.db['actions']
    def insert_new_token(self,token:str) -> dict[str,str]:
        self.tokens.insert_one({"token":token,"created_at":datetime.now()})
        return {"status":'ok','msg':'success'}

    def check_token(self,token:str) -> dict[str,str]:
        # self.insert_new_token('123')
        token = self.tokens.find_one({"token":token})
        if token:
            return {"status":'ok','msg':'success'}
        return {"status":'error','msg':'Token not found'}
    
    def track_requests(self,token:str,action:str) -> dict[str,str]:
        self.actions.insert_one({"token":token,"action":action,"created_at":datetime.now()})
        return {"status":'ok','msg':'success'}

    def delete_token(self,token:str) -> dict[str,str]:
        self.tokens.delete_one({"token":token})
        return {"status":'ok','msg':'success'}
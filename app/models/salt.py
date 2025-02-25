from werzeug.security import gen_salt

class GenSalt:
    def gen_salt(self, length: int=20) -> str:
        return gen_salt(length)
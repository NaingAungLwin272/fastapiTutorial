from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    
    def hashing_password(self, password: str):
        return pwd_context.hash(password)

  
    def verify(self, hashed_password: str, plain_password: str):
        return pwd_context.verify(plain_password, hashed_password)

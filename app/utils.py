from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str):
    print("Recived: ", password)
    print(f"Type being hashed: {type(password)}")
    print(f"Length being hashed: {len(password)}")
    return pwd_context.hash(password)
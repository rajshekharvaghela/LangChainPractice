from pydantic import BaseModel, ValidationError
from datetime import datetime

class User(BaseModel):
    id: int
    name: str   # Field with a default value
    signup_ts: datetime | None = None  # Optional datetime field

# Validating data
user_data = {
    "id": 123,
    "signup_ts": "2024-04-03T10:30:00"
}

try:
    user = User(**user_data)
    print(user)
except ValidationError as e:
    print(e)

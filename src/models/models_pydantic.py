from pydantic import BaseModel, Field, ConfigDict
from datetime import date

class UserCreatePayload(BaseModel):
    first_name: str = Field(min_length=1, max_length=50, frozen=True)
    last_name: str = Field(min_length=1, max_length=50, frozen=True)
    dob: date = Field(frozen=True)

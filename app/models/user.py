from pydantic import BaseModel, ValidationError, EmailStr, validator, Field
from uuid import UUID, uuid4
from enum import Enum, IntEnum
from datetime import  datetime
from app.core.utils import JSONEncoder
import json

from  app import DB

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Account(BaseModel):
    id: UUID
    username: str
    password1: str
    password2: str
    created_at: datetime = Field(default_factory=datetime.now)

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('password do not match')
        return v

class User(BaseModel):
    _id: UUID = Field(default=uuid4(), alias='_id')
    name: str = None
    gender: Gender
    email: EmailStr
    account: Account
    created_at: datetime = Field(default_factory=datetime.now)

    @staticmethod
    def get():
        table_name = __name__.split('.')[-1].lower()
        results = DB.find(table_name)
        list_data = [
            json.loads(JSONEncoder().encode(result))
            for result in results
        ]
        return list_data

    def save(self):
        table_name = type(self).__name__.lower()
        print(self.json())
        DB.insert(table_name,self.dict())
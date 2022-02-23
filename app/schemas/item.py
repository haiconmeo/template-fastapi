from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class ItemBase(BaseModel):
    id: Optional[int]=None
    name :Optional[str]=None

class ItemCreate(ItemBase):
    id:int
    name:str 
    
class ItemUpdate(ItemBase):
    pass

class ItemInDBBase(ItemBase):
    id: int
    name: str

    class Config:
        orm_mode = True

class Item(ItemInDBBase):
    pass

class ItemInDB(ItemInDBBase):
    pass 

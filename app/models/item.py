from typing import TYPE_CHECKING

from sqlalchemy import Column,  Integer, String

class Item():
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,index=True)
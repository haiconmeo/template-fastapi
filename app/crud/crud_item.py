from typing import Any, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.Item import Item
from app.schemas.Item import ItemCreate, ItemUpdate
from app.db.query_builder import query_builder,get_count

class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    def create_with_owner(
        self, db: Session, *, obj = ItemCreate
    ) -> Item:
        obj_in_data = jsonable_encoder(obj)

        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return db_obj
    def get_multi_by_owner(
        self, db: Session, *,  skip: int = 0, limit: int = 100,filter: str = '{}'
    ) -> Any:
        query =  query_builder(db=db, model=self.model, filter=filter)

        return {
            "total": get_count(query),
            "results": query.offset(skip)
            .offset(skip)
            .limit(limit)
            .all()
        }


item = CRUDItem(Item)
from pydantic import BaseModel

class Item(BaseModel):
    """ Item schema model"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

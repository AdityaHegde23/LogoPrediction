from pydantic import BaseModel

class LogoInfo(BaseModel):
    """ Item schema model"""
    logo_name: str
    # description: str | None = None
    # price: float
    # tax: float | None = None

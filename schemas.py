from pydantic import BaseModel

class SandwichBase(BaseModel):
    name: str
    ingredients: str

class SandwichCreate(SandwichBase):
    pass

class Sandwich(SandwichBase):
    id: int

    class Config:
        orm_mode = True

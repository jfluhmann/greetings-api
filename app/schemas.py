from pydantic import BaseModel

class GreetingBase(BaseModel):
    message: str


class GreetingCreate(GreetingBase):
    pass

class Greeting(GreetingBase):
    id: int

    class Config: # this might not be needed (there's not relationships between tables)
        orm_mode = True
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    active: bool

data = {
    "id": 1,
    "name": "Pedro",
    "active": "No" ## Dato curioso pydantic puede entender si yes/no son True o False
}

user = User(**data)


print(user)

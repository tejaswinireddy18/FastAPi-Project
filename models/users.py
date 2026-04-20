from dataclasses import dataclass


@dataclass
class UserModel:
    id: int
    name: str
    email: str

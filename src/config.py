from typing import List


class Config:
    address: str = "localhost:50051"
    clients: List[str] = ["Rohith", "Deepak"]


config = Config()

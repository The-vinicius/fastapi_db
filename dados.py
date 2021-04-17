from typing import Optional, List

from pydantic import BaseModel

class Play(BaseModel):
    level: int
    caracter: str
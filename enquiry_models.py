from typing import Literal
from pydantic import BaseModel, Field


class Enquiry(BaseModel):
    name: str | None = None
    phone: str | None = Field(default=None, pattern=r"^\d{10}$")
    intent: str
    urgency: Literal["high", "medium", "low"]
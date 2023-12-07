from typing import Optional

from pydantic import BaseModel, HttpUrl


class OpenAPIContact(BaseModel):
    name: str
    url: HttpUrl
    email: str


class OpenAPILicense(BaseModel):
    name: str
    url: HttpUrl

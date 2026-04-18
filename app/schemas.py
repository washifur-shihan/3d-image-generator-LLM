from pydantic import BaseModel

class ImageRequest(BaseModel):
    prompt: str
    style: str = "3d cartoon"
    width: int = 1024
    height: int = 1024
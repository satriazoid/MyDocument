from pydantic import BaseModel, Field

class DocumentRequest(BaseModel):
    title: str = Field(..., min_length=5)
    author: str = Field(..., min_length=3)
    institution: str = Field(..., min_length=3)
    chapters: int = Field(..., ge=1, le=10)

class DocumentResponse(BaseModel):
    status: str
    file: str

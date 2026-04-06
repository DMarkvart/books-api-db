from pydantic import BaseModel, Field, field_validator


class BookCreate(BaseModel):
    title: str = Field(min_length=2, max_length=120, description="Book title")
    author: str = Field(min_length=2, max_length=60, description="Book author")
    year: int = Field(ge=1910, le=2026, description="Book year")

    @field_validator("title", "author")
    @classmethod
    def validate_str_data(cls, value)->str:
        if not value.strip():
            raise ValueError("Строка не может быть пустой")
        return value.strip()


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: int

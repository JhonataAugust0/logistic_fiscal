from fastapi import HTTPException
from pydantic import BaseModel, field_validator


class TagRouteValidator(BaseModel):
    product_code: str

    @field_validator("product_code")
    def validate_product_code(cls, product_code: str):
        if not isinstance(product_code, str):
            raise ValueError("O código do produto deve ser uma string")
        return product_code

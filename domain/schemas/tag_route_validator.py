from fastapi import HTTPException
from starlette import status
from typing import Any
from pydantic import BaseModel, field_validator, root_validator

class TagRouteValidator(BaseModel):
    product_code: Any

    @root_validator(pre=True)
    def validate_parameter_name(cls, values):
        if not values.get("product_code"):
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "O código do produto é obrigatório")
        return values
    
    @field_validator("product_code")
    def validate_product_code(cls, product_code: str):
        if not isinstance(product_code, str):
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "O código do produto deve ser uma string")
        return product_code
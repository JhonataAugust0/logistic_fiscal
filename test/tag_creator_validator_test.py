import os
import sys
from fastapi import HTTPException
import pytest
from starlette import status
from domain.schemas.tag_route_validator import TagRouteValidator


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class MockRequest:
    def __init__(self, json) -> None:
      self.json = json


def test_validate_valid_key_and_value():
    request = MockRequest(json={"product_code": "123456"})
    response = TagRouteValidator.validate_parameter_name(request.json) 
    assert response == request.json


def test_validate_invalid_key_name():
    with pytest.raises(HTTPException) as exc_info:
        request = MockRequest(json={"invalid_parameter_name": "123456"})
        TagRouteValidator.validate_parameter_name(request.json)
    
    assert exc_info.value.status_code == 422
    assert exc_info.value.detail == "O código do produto é obrigatório"


def test_validate_invalid_value_type():
    with pytest.raises(HTTPException) as exec_info: 
        request = MockRequest(json={"product_code": 79.4})
        TagRouteValidator.validate_product_code(request.json) 
    assert exec_info.value.status_code == 422
    assert exec_info.value.detail == "O código do produto deve ser uma string"

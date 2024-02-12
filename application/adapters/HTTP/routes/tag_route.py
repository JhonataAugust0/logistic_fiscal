from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from application.views.tag_creator_view import TagCreatorView
from domain.schemas.tag_route_validator import TagRouteValidator
from errors.error_handler import handle_errors


class TagRoute:
    def __init__(self, tags: str = ["TagRoute"]):
        self.router = APIRouter(tags=tags)
        self.router.add_api_route(
            name="Criar código de barras",
            path="/create_tag",
            endpoint=self.create_tag,
            methods=["POST"],
            include_in_schema=True,
            responses={
                200: {"content": {"application/json": {"examples": {
                    "examples": {"summary": "examples", "value": {
                        "data": {
                            "type": "Tag Image",
                            "count": 'number',
                            "path": f'path_from_tag.png'
                        }}}}}}},
                422: {"content": {"application/json": {"examples": {
                    "examples": {"summary": "examples", "value": {
                        "data": {
                            "detail": "O código do produto deve ser uma string"
                        }}}}}}},
            }
        )

    async def create_tag(self, tag_data: TagRouteValidator) -> Dict[str, Any]:
        response = None
        try:
            product_code = tag_data.product_code
            tag_creator_view = TagCreatorView()

            response = await tag_creator_view.validate_and_create(product_code)
            return response
        except Exception as error:
           response = handle_errors(error)
           return response 
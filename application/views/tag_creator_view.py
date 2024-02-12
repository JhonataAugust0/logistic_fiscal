from application.controllers.tag_creator_controller import TagCreatorController
from typing import Dict, Any

from application.views.http_types.http_response import HttpResponse
from application.views.http_types.http_request import HttpRequest


class TagCreatorView:
    def __init__(self):
        self.tag_creator_controller = TagCreatorController()

    async def validate_and_create(self, product_code: HttpRequest) -> HttpResponse:
        formatted_response = await self.tag_creator_controller.create(product_code)
        return formatted_response
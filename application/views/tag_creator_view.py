from application.controllers.tag_creator_controller import TagCreatorController
from typing import Dict, Any


class TagCreatorView:
    def __init__(self):
        self.tag_creator_controller = TagCreatorController()

    async def validate_and_create(self, product_code: str) -> Dict[str, Any]:
        formatted_response = await self.tag_creator_controller.create(product_code)
        return formatted_response
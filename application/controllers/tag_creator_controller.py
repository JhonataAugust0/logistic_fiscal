from typing import Dict, Any
from application.drivers.barcode_handler import BarcodeHandler


class TagCreatorController:
    def __init__(self):
        self.barcode_handler = BarcodeHandler()

    async def create(self, product_code: str) -> Dict[str, Any]:
        path_from_tag = await self.__create_tag(product_code)
        formatted_response = await self.__format_response(path_from_tag)
        return formatted_response

    async def __create_tag(self, product_code: str) -> str:
        path_from_tag = await self.barcode_handler.create_barcode(product_code)
        return path_from_tag

    async def __format_response(self, path_from_tag: str) -> Dict[str, Any]:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }

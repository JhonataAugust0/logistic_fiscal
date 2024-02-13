from unittest.mock import patch

import pytest
from application.controllers.tag_creator_controller import TagCreatorController
from application.drivers.barcode_handler import BarcodeHandler


@pytest.mark.asyncio
@patch.object(BarcodeHandler, "create_barcode")
async def test_create(mock_create_barcode):
    mock_value = "image_path"
    mock_create_barcode.return_value = mock_value
    tag_creator_controller = TagCreatorController()

    result = await tag_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert "data" in result and "type" in result["data"] and "count" in result["data"] and "path" in result["data"]
    assert result["data"]["type"] == "Tag Image" and result["data"]["count"] == 1 and result["data"]["path"] == f"{mock_value}.png"


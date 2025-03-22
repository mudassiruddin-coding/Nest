# # -*- coding: utf-8 -*-
# import os

# import pytest
# from PIL import Image

# os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


# @pytest.fixture(autouse=True, scope="module")
# def image():
#     os.makedirs("media", exist_ok=True)
#     with open(os.path.join("media", "testing.jpeg"), "w") as f:
#         Image.new("RGB", (100, 100), (150, 0, 0)).save(f)

# -*- coding: utf-8 -*-
import os

import pytest
from PIL import Image

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


@pytest.fixture(autouse=True, scope="module")
def image():
    os.makedirs("media", exist_ok=True)
    image_path = os.path.join("media", "testing.jpeg")

    # Create an RGB image (not RGBA) to avoid issues
    img = Image.new("RGB", (100, 100), (150, 0, 0))
    img.save(image_path, format="JPEG")

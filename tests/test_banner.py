import os
from PIL import Image


def test_banner_generates_file():
    from banner import generate_banner
    output = "assets/test_banner.png"
    generate_banner(output)
    assert os.path.exists(output)
    os.remove(output)


def test_banner_correct_dimensions():
    from banner import generate_banner
    output = "assets/test_banner.png"
    generate_banner(output)
    with Image.open(output) as img:
        size = img.size
    assert size == (1500, 500)
    os.remove(output)

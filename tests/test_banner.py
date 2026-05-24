import os
from PIL import Image


def test_banner_generates_file(tmp_path):
    from banner import generate_banner
    output = str(tmp_path / "banner.png")
    generate_banner(output)
    assert os.path.exists(output)


def test_banner_correct_dimensions(tmp_path):
    from banner import generate_banner
    output = str(tmp_path / "banner.png")
    generate_banner(output)
    with Image.open(output) as img:
        assert img.size == (1500, 500)

from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1500, 500
FONT_PATH = "assets/fonts/Roboto-Bold.ttf"
START_COLOR = (224, 64, 251)   # #E040FB pink
END_COLOR = (124, 58, 237)     # #7C3AED purple


def _gradient(width, height, start, end):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    r1, g1, b1 = start
    r2, g2, b2 = end
    for x in range(width):
        r = int(r1 + (r2 - r1) * x / width)
        g = int(g1 + (g2 - g1) * x / width)
        b = int(b1 + (b2 - b1) * x / width)
        draw.line([(x, 0), (x, height)], fill=(r, g, b))
    return img


def generate_banner(output_path="assets/banner.png"):
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    img = _gradient(WIDTH, HEIGHT, START_COLOR, END_COLOR)
    draw = ImageDraw.Draw(img)

    try:
        title_font = ImageFont.truetype(FONT_PATH, 130)
        tagline_font = ImageFont.truetype(FONT_PATH, 48)
    except OSError:
        print(f"Warning: font not found at {FONT_PATH}, falling back to default (text will look small)")
        title_font = ImageFont.load_default()
        tagline_font = ImageFont.load_default()

    title = "Verse"
    tb = draw.textbbox((0, 0), title, font=title_font)
    title_w, title_h = tb[2] - tb[0], tb[3] - tb[1]
    draw.text(
        ((WIDTH - title_w) / 2, HEIGHT / 2 - title_h - 10),
        title, font=title_font, fill=(255, 255, 255),
    )

    tagline = "AI Employees, No Code Required"
    sb = draw.textbbox((0, 0), tagline, font=tagline_font)
    tagline_w = sb[2] - sb[0]
    draw.text(
        ((WIDTH - tagline_w) / 2, HEIGHT / 2 + 20),
        tagline, font=tagline_font, fill=(230, 210, 255),
    )

    img.save(output_path)


if __name__ == "__main__":
    generate_banner()
    print("Banner saved to assets/banner.png")

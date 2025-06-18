from PIL import Image
from pathlib import Path

def crop(img):
    width, height = img.size
    if width > height:
        left = (width - height) // 2
        right = left + height
        img = img.crop((left, 0, right, height))
    elif height > width:
        top = (height - width) // 2
        bottom = top + width
        img = img.crop((0, top, width, bottom))
    return img

def resize(img, width=800, height=800):
    return img.resize((width, height), Image.LANCZOS)

for file in Path('').glob('*.png'):
    input_path = str(file)
    output_path = str(file.parent / (file.stem + ".out.png"))

    with Image.open(input_path) as img:
        processed_img = resize(crop(img))
        processed_img.save(output_path, format="PNG")
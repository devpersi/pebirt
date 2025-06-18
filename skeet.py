# this version can fit in a bluesky post if you don't include the imports
from PIL import Image
from pathlib import Path

for f in Path('').glob('*.png'):
    with Image.open(f) as img:
        s = min(img.size)
        img = img.crop(((img.width-s)//2, (img.height-s)//2, (img.width+s)//2, (img.height+s)//2)).resize((800, 800), Image.LANCZOS)
        img.save(f.with_suffix('.out.png'))
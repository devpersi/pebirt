# this version can fit in a bluesky post
from PIL import Image
from pathlib import Path

for f in Path('').glob('*.png'):
    with Image.open(f) as img:
        s=min(img.size)
        img.crop(((img.width-s)//2,(img.height-s)//2,(img.width+s)//2,(img.height+s)//2)).resize((800, 800), Image.LANCZOS).save(f.with_suffix('.out.png'))
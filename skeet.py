# this version can fit in a bluesky post
from PIL import Image; from pathlib import Path
for f in Path().glob('*.png'):
    with Image.open(f) as i:
        i.crop(((w:=i.width-(s:=min(i.size)))//2, (h:=i.height-s)//2, w//2+s, h//2+s)).resize((800,800), Image.LANCZOS).save(f.with_suffix('.out.png'))

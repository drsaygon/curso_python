from pathlib import Path
from PIL import Image

ROOT_FOOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOOLDER / 'original.jpg'
NEW_IMAGE = ROOT_FOOLDER / 'new.jpg'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
exif = pil_image.info['exif']

new_width = 640
new_height = round(height * new_width / width)

print(new_width, new_height)

new_image = pil_image.resize((new_width, new_height))

new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=100
)
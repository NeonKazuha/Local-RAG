import os
import pytesseract as tess
from PIL import Image
from pdf2image import convert_from_path

def read(file):
    pages = []

    try:
        # Converting PDF pages into individual images
        images = convert_from_path(file)

        for i, image in enumerate(images):
            file_name = 'page_' + str(i) + '_' + os.path.basename(file) + '.jpeg'
            image.save(file_name, 'JPEG')
            text = tess.image_to_string(Image.open(file_name))
            pages.append(text)

    except Exception as e:
        print(str(e))

    with open( 'extraction.txt', 'w' ) as f:
        f.write('\n'.join(pages))
import sys
import os
from PIL import Image
from PIL import ImageOps

def main():


    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")



    input = sys.argv[1].lower()
    output = sys.argv[2].lower()

    if input.endswith(".png") or input.endswith(".jpg") or input.endswith(".jpeg"):
        pass
    else:
        sys.exit("Not an image file")

    if output.endswith(".png") or output.endswith(".jpg") or output.endswith(".jpeg"):
        pass
    else:
        sys.exit("Output not an image file")

    name_1, ext_1 = os.path.splitext(input)
    name_2, ext_2 = os.path.splitext(output)
    

    if ext_2 != ext_1:
        sys.exit("File extensions do not match")


    with Image.open("shirt.png") as shirt:
        size = shirt.size

    with Image.open(sys.argv[1]) as image_1, Image.open("shirt.png") as shirt:
        image_1 = ImageOps.fit(image_1, size)
        image_1.paste(shirt, shirt)
        image_1.save(sys.argv[2])






if __name__ == "__main__":
    main()
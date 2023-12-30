import argparse
from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions

def display_image(image_path):
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.chain_length = 2
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'  

    matrix = RGBMatrix(options=options)

    image = Image.open(image_path)
    image.thumbnail((options.cols * options.chain_length, options.rows), Image.ANTIALIAS)
    matrix.SetImage(image.convert('RGB'))

    try:
        print("Image displayed. Press CTRL-C to stop.")
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        matrix.Clear()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', help='Path to the image to display', required=True)
    args = parser.parse_args()

    display_image(args.image)

import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import argparse
import sys

def run_text(text, font_name, speed, rows, cols):
    options = RGBMatrixOptions()
    options.rows = rows
    options.cols = cols
    options.chain_length = 1  # Adjust if different
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'

    matrix = RGBMatrix(options=options)

    # Set the correct font path
    font_path = '/home/fonts/' + font_name + '.bdf'

    # Load font
    font = graphics.Font()
    font.LoadFont(font_path)

    # Colors and position setup
    color = graphics.Color(255, 255, 255)
    xpos = cols * options.chain_length
    ypos = rows // 2

    # Check if text is provided
    if not text:
        print("No text provided. Exiting.")
        sys.exit(1)

    # Display text
    while True:
        matrix.Clear()
        len = graphics.DrawText(matrix, font, xpos, ypos, color, text)
        xpos -= speed
        if xpos + len < 0:
            xpos = cols * options.chain_length
        time.sleep(0.05)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', help='The text to scroll on the matrix', default='Hello')
    parser.add_argument('--font', help='Name of the font (without .bdf extension)', default='6x9')
    parser.add_argument('--speed', help='Speed of the text scroll', type=int, default=1)
    args = parser.parse_args()

    run_text(args.text, args.font, args.speed, 32, 64)  # Assuming 32 rows and 64 columns per panel

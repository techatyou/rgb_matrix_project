import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import argparse
import sys

def run_text(text, font_name, speed, rows, cols, color):
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

    # Parse the color argument and ensure it's a valid option
    if color not in ('red', 'green', 'blue'):
        print("Invalid color option. Use 'red', 'green', or 'blue'.")
        sys.exit(1)

    # Set the color based on the argument
    if color == 'red':
        text_color = graphics.Color(255, 0, 0)
    elif color == 'green':
        text_color = graphics.Color(0, 255, 0)
    else:  # color == 'blue'
        text_color = graphics.Color(0, 0, 255)

    # Colors and position setup
    xpos = cols
    ypos = rows // 2 - font.baseline - 1

    # Check if text is provided
    if not text:
        print("No text provided. Exiting.")
        sys.exit(1)

    # Display text
    while True:
        matrix.Clear()
        for char in text:
            char_width = font.CharacterWidth(ord(char))  # Get the width of the character
            graphics.DrawText(matrix, font, xpos - char_width, ypos, text_color, char)
            xpos -= char_width + 1  # Add 1-pixel space between characters
            if xpos + char_width < 0:
                xpos = cols
            time.sleep(0.05)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', help='The text to scroll on the matrix', default='Hello')
    parser.add_argument('--font', help='Name of the font (without .bdf extension)', default='6x9')
    parser.add_argument('--speed', help='Speed of the text scroll', type=int, default=1)
    parser.add_argument('--color', help='Text color: red, green, or blue', default='red')
    args = parser.parse_args()

    run_text(args.text, args.font, args.speed, 32, 64, args.color)  # Assuming 32 rows and 64 columns per panel

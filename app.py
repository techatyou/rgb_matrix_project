from flask import Flask, render_template, request
from samplebase import SampleBase
from rgbmatrix import graphics
import time

app = Flask(__name__)

# Initialize the text color to white (255, 255, 255)
text_color = graphics.Color(255, 255, 255)

class RunText(SampleBase):
    # ... (no changes to the RunText class)

@app.route("/", methods=["GET", "POST"])
def index():
    global text_color
    if request.method == "POST":
        text = request.form["text"]
        font = request.form["font"]
        speed = int(request.form["speed"])
        color = request.form["color"]

        # Set the text color based on the selected color
        if color == "red":
            text_color = graphics.Color(255, 0, 0)  # Red
        elif color == "green":
            text_color = graphics.Color(0, 255, 0)  # Green
        elif color == "blue":
            text_color = graphics.Color(0, 0, 255)  # Blue

        # Call the RunText function with the selected parameters
        run_text(text, font, speed, 32, 64)  # Adjust rows and columns as needed

    return render_template("index.html", text_color=text_color)

if __name__ == "__main__":
    app.run(debug=True)

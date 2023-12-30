from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

# Directory where uploaded files will be stored
UPLOAD_FOLDER = 'uploaded_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# List of available fonts
AVAILABLE_FONTS = ['6x9', '6x12', '7x13', '8x13', '9x15', '10x20']

# Store the subprocess object for controlling the display
display_process = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global display_process
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Upload':
            file = request.files['graphic']
            if file and file.filename != '':
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
                display_graphic_on_matrix(filepath)
        elif action == 'Start Text':
            text = request.form.get('text')
            font = request.form.get('font')
            speed = request.form.get('speed')
            stop_display()
            start_display_text(text, font, speed)
        elif action == 'Stop Text':
            stop_display()
    return render_template('index.html', fonts=AVAILABLE_FONTS, display_running=is_display_running())

def display_graphic_on_matrix(image_path):
    graphic_display_script = '/root/rgb_matrix_project/led_matrix/graphic_display_script.py'
    cmd = ['python3', graphic_display_script, '--image', image_path]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while displaying the graphic on the matrix: {e}")

def start_display_text(text, font, speed):
    global display_process
    matrix_script_path = '/root/rgb_matrix_project/led_matrix/runtext.py'
    cmd = ['python3', matrix_script_path, '--text', text, '--font', font, '--speed', speed]
    try:
        display_process = subprocess.Popen(cmd)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while starting the matrix display: {e}")

def stop_display():
    global display_process
    if display_process:
        try:
            display_process.terminate()
            display_process.wait()
        except Exception as e:
            print(f"An error occurred while stopping the matrix display: {e}")
        display_process = None

def is_display_running():
    return display_process is not None

if __name__ == '__main__':
    app.run(debug=True)

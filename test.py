import tkinter as tk
import subprocess

def start_scroll_text():
    text = "Hello, World!"  # Replace this with your desired text
    font = "6x9"  # Replace this with your desired font
    speed = "1"  # Replace this with your desired speed

    matrix_script_path = '/root/rgb_matrix_project/led_matrix/runtext.py'
    cmd = ['python3', matrix_script_path, '--text', text, '--font', font, '--speed', speed]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the matrix display command: {e}")

# Create the main window
root = tk.Tk()
root.title("RGB Matrix Controller")

# Create a button to start scrolling text
start_button = tk.Button(root, text="Start Scrolling Text", command=start_scroll_text)
start_button.pack(pady=20)

# Start the GUI main loop
root.mainloop()

# This program retrieves the PC screen size and displays the mouse cursor coordinates.
# After using this program, please close the Tkinter window.
# If you leave it open, you won't be able to run other programs.

import tkinter as tk

# Check the screen resolution and scaling settings in your PC's display settings.
# For a screen resolution of 1920x1080
screen_width = 1920
screen_height = 1080
# Set the screen scaling rate in Windows.
scale_factor = 1.25  # For example, if the screen scaling is set to 125%


def get_window_position():
    root.update_idletasks()  # Update the window information
    x = root.winfo_rootx()  # X-coordinate of the top-left corner of the window (including the frame)
    y = root.winfo_rooty()  # Y-coordinate of the top-left corner of the window (including the frame)
    return x, y

def update_coordinates(event, screen_width, screen_height, scale_factor):
    # Get the current position of the window
    window_x, window_y = get_window_position()

    # Convert coordinates within the window to screen-wide coordinates
    screen_x = window_x + event.x
    screen_y = window_y + event.y

    # Apply the scaling factor to the actual coordinates
    actual_x = int(screen_x * scale_factor)
    actual_y = int(screen_y * scale_factor)

    # Display the coordinates
    label.config(text=f"X: {actual_x}, Y: {actual_y}\n"
                      f"Screen Width: {screen_width}, Screen Height: {screen_height}")

def on_motion(event):
    update_coordinates(event, screen_width, screen_height, scale_factor)

root = tk.Tk()

# Open the window at 250x50 pixels
root.geometry("250x50")

# Create and place the label
label = tk.Label(root, text="")
label.pack(padx=10, pady=10)

# Monitor mouse movement
root.bind("<Motion>", on_motion)

root.mainloop()

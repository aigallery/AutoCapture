import tkinter as tk
import pyautogui

class MousePositionDisplay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mouse Position Display")

        # Set the window style to "toolwindow" and remove minimize and maximize buttons
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)

        # Create a frame to hold the contents
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.mouse_pos_label = tk.Label(self.frame, text="Mouse Position: (0, 0)")
        self.mouse_pos_label.pack()

        # Create a close button
        self.close_button = tk.Button(self.frame, text="Close", command=self.root.destroy)
        self.close_button.pack()

        self.root.after(100, self.update_info)  # Update every 100 milliseconds

        self.root.mainloop()

    def update_info(self):
        mouse_x, mouse_y = pyautogui.position()
        self.mouse_pos_label.config(text=f"Mouse Position: ({mouse_x}, {mouse_y})")

        self.root.after(100, self.update_info)  # Schedule the next update

MousePositionDisplay()

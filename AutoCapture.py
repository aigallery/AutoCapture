import pyautogui
import time
import tkinter as tk
from tkinter import filedialog
import os

capture_in_progress = False

def capture_screenshot(left, top, right, bottom, save_path):
    # Capture the screenshot of the specified region
    screenshot = pyautogui.screenshot(region=(left, top, right-left, bottom-top))

    # Generate a unique filename to prevent overwriting existing files
    index = 1
    filename = f"{index}.png"
    while os.path.exists(os.path.join(save_path, filename)):
        index += 1
        filename = f"{index}.png"

    # Save the screenshot with the generated filename
    screenshot.save(os.path.join(save_path, filename))

def capture_button_click():
    global capture_in_progress

    if not capture_in_progress:
        # Get the user input from the text entry fields
        left = int(left_entry.get())
        top = int(top_entry.get())
        width = int(width_entry.get())
        height = int(height_entry.get())
        save_path = filedialog.askdirectory()
        click_count = int(click_count_entry.get())
        button = 'left' if button_var.get() == 1 else 'right'
        click_x = int(click_x_entry.get())
        click_y = int(click_y_entry.get())

        # Perform the specified number of clicks at the specified position
        while True:
            pyautogui.moveTo(click_x, click_y)
            current_count = 0  # 当前点击计数
            while current_count < click_count:
                try:
                    current_pos = pyautogui.position()
                    if current_pos.x != click_x or current_pos.y != click_y:
                        pyautogui.moveTo(click_x, click_y)
                    pyautogui.click(button=button)
                    current_count += 1
                    # time.sleep(0.2)
                except pyautogui.FailSafeException:
                    # 处理鼠标移动到屏幕边缘的情况
                    print("鼠标移动失败")
                except pyautogui.FailSafeException:
                    # 处理其他鼠标操作异常
                    print("鼠标点击失败")

            # Capture and save the screenshot
            capture_screenshot(left, top, width, height, save_path)

            # Check if there is any change after the left click
            if button == 'left':
                previous_screen = pyautogui.screenshot(region=(left, top, width, height))
                pyautogui.click(button='left')
                time.sleep(1)  # Wait for potential page changes
                current_screen = pyautogui.screenshot(region=(left, top, width, height))

                if previous_screen == current_screen:
                    break

        capture_in_progress = True
        # Capture process is complete
        tk.messagebox.showinfo("Capture Completed", "Capture process has been completed.")

def end_button_click():
    global capture_in_progress
    capture_in_progress = False


# Create the GUI window
window = tk.Tk()
window.title("Screenshot Capture")
window.geometry("350x250")

# Create and position the input fields and labels
left_label = tk.Label(window, text="Area Left:")
left_label.grid(row=0, column=0, sticky="w")
left_entry = tk.Entry(window)
left_entry.grid(row=0, column=1, sticky="w")

top_label = tk.Label(window, text="Area Top:")
top_label.grid(row=1, column=0, sticky="w")
top_entry = tk.Entry(window)
top_entry.grid(row=1, column=1, sticky="w")

width_label = tk.Label(window, text="Area Right:")
width_label.grid(row=2, column=0, sticky="w")
width_entry = tk.Entry(window)
width_entry.grid(row=2, column=1, sticky="w")

height_label = tk.Label(window, text="Area Bottom:")
height_label.grid(row=3, column=0, sticky="w")
height_entry = tk.Entry(window)
height_entry.grid(row=3, column=1, sticky="w")

click_count_label = tk.Label(window, text="Click Count:")
click_count_label.grid(row=5, column=0, sticky="w")
click_count_entry = tk.Entry(window)
click_count_entry.grid(row=5, column=1, sticky="w")

button_label = tk.Label(window, text="Button:")
button_label.grid(row=6, column=0, sticky="w")
button_var = tk.IntVar()
left_button = tk.Radiobutton(window, text="Left", variable=button_var, value=1)
left_button.grid(row=6, column=1, sticky="w")
right_button = tk.Radiobutton(window, text="Right", variable=button_var, value=2)
right_button.grid(row=6, column=2, sticky="w")

click_x_label = tk.Label(window, text="Click X Position:")
click_x_label.grid(row=7, column=0, sticky="w")
click_x_entry = tk.Entry(window)
click_x_entry.grid(row=7, column=1, sticky="w")

click_y_label = tk.Label(window, text="Click Y Position:")
click_y_label.grid(row=8, column=0, sticky="w")
click_y_entry = tk.Entry(window)
click_y_entry.grid(row=8, column=1, sticky="w")

button_frame = tk.Frame(window)
button_frame.grid(row=9, column=0, columnspan=2, pady=10)
capture_button = tk.Button(button_frame, text="Capture", command=capture_button_click)
capture_button.pack(side="left", padx=10)

end_button = tk.Button(button_frame, text="End", command=end_button_click)
end_button.pack(side="left", padx=10)

# Start the GUI event loop
window.mainloop()

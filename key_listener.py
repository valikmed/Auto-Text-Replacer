import time
import os
import pyperclip

FILE_PATH = r"C:\\Users\\Valentyn\\Documents\\Python\\data.txt"  # Update this path

def get_value_from_file(key: str, file_path: str) -> str | None:
    """Searches for a key in the file and returns its corresponding value."""
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                if k == key:
                    return v  # Return the value if key matches
    return None  # Key not found

def monitor_clipboard():
    """Continuously checks clipboard content and replaces recognized keys automatically."""
    last_clipboard = ""

    print("🔄 Monitoring clipboard... Copy a key, and it will be replaced automatically!")

    while True:
        time.sleep(1)  # Check every second to reduce CPU usage
        clipboard_content = pyperclip.paste()

        if clipboard_content != last_clipboard:  # Check if clipboard has changed
            last_clipboard = clipboard_content
            value = get_value_from_file(clipboard_content, FILE_PATH)

            if value:
                pyperclip.copy(value)  # Replace clipboard content with the found value
                print(f"✅ Replaced '{clipboard_content}' with '{value}' (Copied to clipboard)")

if __name__ == "__main__":
    monitor_clipboard()

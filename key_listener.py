import os
import keyboard
import datetime

FILE_PATH = r"C:\\Users\\Valentyn\\Documents\\Python\\data.txt"  # Update this path

typed_word = ""

def get_value_from_file(key: str, file_path: str) -> str | None:
    """Searches for a key in the file and returns its corresponding value."""
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                if k == key:
                    # Special case: Convert date format
                    if k == "data":
                        try:
                            date_obj = datetime.datetime.strptime(v, "%d/%m/%Y")
                            return date_obj.strftime("%Y-%m-%d")  # Convert to YYYY-MM-DD
                        except ValueError:
                            return None
                    return v  # Return the value if key matches
    return None  # Key not found

def on_key_press(event):
    global typed_word

    if event.event_type == "down":  # Only process keypress events
        if event.name == "space":  
            value = get_value_from_file(typed_word, FILE_PATH)  # Get replacement value
            if value:
                for _ in range(len(typed_word) + 1):  # Remove typed key + space
                    keyboard.send("backspace")
                keyboard.write(value + " ")  # Replace with correct value and space
                print(f"✅ Replaced '{typed_word}' with '{value}'")
            typed_word = ""  # Reset after replacement
        
        elif event.name == "backspace":  
            typed_word = typed_word[:-1]  # Remove last character
        
        elif len(event.name) == 1:  # Only add normal characters (not special keys)
            typed_word += event.name  

# Start listening for keyboard input
keyboard.on_press(on_key_press)

print("🔄 Listening for typed words... Type a key and press space to replace it.")
keyboard.wait()  # Keep the script running

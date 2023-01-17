import pyautogui

# Open WhatsApp
# assumes WhatsApp is in the first position on the taskbar
pyautogui.hotkey('win', '1')

# Wait for WhatsApp to load
pyautogui.sleep(1)

# Focus on the input field
pyautogui.hotkey('ctrl', 't')
for i in range(20):
    # Type "I love you"
    pyautogui.typewrite("I am Sorry", interval=0.10)

    # Press enter to send the message
    pyautogui.press('enter')

    # Repeat 100 times

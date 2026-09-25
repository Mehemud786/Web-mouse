import time
import requests
import pyautogui

# Replace with your actual deployed Vercel URL
SERVER_URL = "https://your-app-name.vercel.app/api/get"

print("Listening for mouse signals from Mobile A via Vercel...")

# Safety fail-safe for PyAutoGUI
pyautogui.FAILSAFE = True

while True:
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            data = response.json()
            dx = data.get("x", 0)
            dy = data.get("y", 0)
            action = data.get("action", "idle")

            if action == 'move' and (dx != 0 or dy != 0):
                # Scale movement multiplier as necessary
                pyautogui.moveRel(dx * 1.5, dy * 1.5)
            elif action == 'left_click':
                pyautogui.click()
            elif action == 'right_click':
                pyautogui.rightClick()
                
    except Exception as e:
        print("Polling error:", e)
    
    time.sleep(0.05) # Poll interval (~20 times per second)
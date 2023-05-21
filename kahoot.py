import pyautogui, time, random, webbrowser
webbrowser.open('https://kahoot.it/')
time.sleep(10)
nums = "1234567890"
for i in range(int(input("how many times to spam? "))):
    for i in range(6):
        pyautogui.write(random.choice(nums))
    pyautogui.press('enter')
    time.sleep(1.5)

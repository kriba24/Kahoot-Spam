import pyautogui as pg, time, random, webbrowser as wb
wb.open('https://kahoot.it/')
time.sleep(10)
nums = "1234567890"
for i in range(50):
    for i in range(6):
        pg.write(random.choice(nums))
    pg.press('enter')
    time.sleep(1.5)

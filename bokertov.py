
import pyautogui
import time
import datetime
import keyboard

def schedule():
    now = datetime.datetime.now()
    day = now.strftime("%A")
    if (day == "Thursday" or day == "Friday") and now.hour >= 8 and now.hour <= 11:
        return True
    else:
        return False

flag = True
while True:
    while schedule():
        if flag:
            today_pic = r'C:\Users\liran\PycharmProjects\pythonProject1\today3.png'
            pyautogui.click(1919, 1048)
            time.sleep(0.3)
            pyautogui.press("win")
            time.sleep(0.7)
            keyboard.write("google chrome")
            time.sleep(0.8)
            t = pyautogui.locateOnScreen(r'C:\Users\liran\PycharmProjects\pythonProject1\google.png')
            if t != None:
                pyautogui.click(pyautogui.center(t))
            pyautogui.click(240, 513)
            time.sleep(1.5)
            pyautogui.click(413, 51)
            keyboard.write("https://web.whatsapp.com/")
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.click(435, 170)
            keyboard.write("deep learning")
            time.sleep(1.2)
            pyautogui.click(472, 297)
            time.sleep(1)
            p = pyautogui.locateOnScreen(today_pic)
            time.sleep(0.6)
            pyautogui.click(984, 990)
            while flag and schedule():
                time.sleep(1)
                if p == None:
                    pyautogui.moveTo(950, 500)
                    pyautogui.scroll(5)
                    pyautogui.scroll(-5)
                    time.sleep(0.5)
                    p = pyautogui.locateOnScreen(today_pic)
                if p != None:
                    r = pyautogui.locateOnScreen(r'C:\Users\liran\PycharmProjects\pythonProject1\bokertov.png')
                    max1 = 0
                    max2 = 0
                    if r != None:
                        time.sleep(1)
                        r = list(pyautogui.locateAllOnScreen(r'C:\Users\liran\PycharmProjects\pythonProject1\bokertov.png'))
                        if len(r) >= 2:
                            max1 = pyautogui.center(r[-1])[0]
                            max2 = pyautogui.center(r[-1])[1]
                        else:
                            r = pyautogui.locateOnScreen(r'C:\Users\liran\PycharmProjects\pythonProject1\bokertov.png')
                            r = pyautogui.center(r)
                            max1 = r[0]
                            max2 = r[1]
                        if max1 < p[0] and max2 > p[1] and max1 > 680:
                            keyboard.write("בוקר טוב")
                            pyautogui.press("enter")
                            flag = False
                            pyautogui.click(1900,9)
                time.sleep(60 * 3)
    flag = True
    time.sleep(60*5)

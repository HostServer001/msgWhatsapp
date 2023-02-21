try:
  import pyautogui as gui
  import webbrowser as web
  import datetime
  import time
except:
  import os
  print("[Note]: Setting up")
  os.system("pip install pyautogui")
  os.system("pip install PyPi-Browser")
  os.system("pip install time")
  os.system("pip install datetime")
  import pyautogui as gui
  import webbrowser as web
  import datetime
def send(message,number,h,m):
  if h:
    if m:
      if datetime.datetime.now().hour == h:
        if datetime.datetime.now().minutes == m:
          web.open(f"https://web.whatsapp.com/send/?phone={number}&text={message}&type=phone_number&app_absent=0")
          time.sleep(15)
          gui.click(1340,700)

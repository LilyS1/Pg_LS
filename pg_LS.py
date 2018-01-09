import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')

pg.typewrite('gmail.com\n',0.5)
time.sleep(3)

pg.moveTo(850,282,2)
pg.click(850,282)

pg.moveTo(609,380,2)
pg.click(609,380)
time.sleep(2)

pg.typewrite('lschweinfurth@gcds.net')
pg.hotkey('Enter\n')

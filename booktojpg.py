import pyautogui as pag

pag.moveTo(2103 ,-220,duration=2)
pag.leftClick()

for i in range(140):
    pag.moveTo(2103 ,-220, duration=1)
    pag.hotkey('ctrl', 's',)
    pag.moveTo(2103 ,-220, duration=2)
    pag.dragTo(x=3238, y=1348, duration=2)

    pag.moveTo(3307, 565, duration=2)
    pag.leftClick()

    pag.moveTo(2101, -224, duration=1)
    pag.hotkey('ctrl', 's')
    pag.moveTo(2101 ,-224, duration=2)
    pag.dragTo(x=3234, y=1349, duration=2)

    pag.moveTo(3307, 565,duration=2)
    pag.leftClick()
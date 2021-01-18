import pyautogui as pag
import time
pag.moveTo(1985,-266,duration=1) # 캡처할 프로그램 클릭
pag.leftClick()

for i in range(145): # 페이지 반.
    ########
    pag.moveTo(1985,-266, duration=0.5) #캡처 시작지점으로 이동
    pag.hotkey('ctrl', 'e',) # 지정 캡처 버튼
    time.sleep(2) # 지정 캡처 후 기다리는 시간
    pag.dragTo(x=3290  , y=1422, duration=2) # 천천히 캡처.
    #pag.moveTo(3353  ,579, duration=1) # 다음페이지
    time.sleep(1)
    pag.doubleClick()
    pag.scroll(-1)
    #####################################################################
    '''
    pag.moveTo(2101, -224, duration=0.5)
    pag.hotkey('ctrl', 'e')
    pag.moveTo(2101 ,-224, duration=2)
    pag.dragTo(x=3234, y=1349, duration=2)
    pag.moveTo(3307, 565,duration=2)
    pag.leftClick()
    '''
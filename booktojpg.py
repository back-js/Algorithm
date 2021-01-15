import pyautogui as pag

pag.moveTo(2103 ,-220,duration=1) # 캡처할 프로그램 클릭
pag.leftClick()

for i in range(140): # 페이지 반.
    ########
    pag.moveTo(2103 ,-220, duration=0.5) #캡처 시작지점으로 이동
    pag.hotkey('ctrl', 'e',) # 지정 캡처 버튼
    pag.moveTo(2103 ,-220, duration=2) # 지정 캡처 후 기다리는 시간
    pag.dragTo(x=3238, y=1348, duration=2) # 천천히 캡처.
    pag.moveTo(3307, 565, duration=2) # 다음페이지
    pag.leftClick()
    #####################################################################
    pag.moveTo(2101, -224, duration=0.5)
    pag.hotkey('ctrl', 'e')
    pag.moveTo(2101 ,-224, duration=2)
    pag.dragTo(x=3234, y=1349, duration=2)
    pag.moveTo(3307, 565,duration=2)
    pag.leftClick()
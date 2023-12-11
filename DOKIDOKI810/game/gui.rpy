
init offset = -2

init python:
    gui.init(1920, 1080)


define config.check_conflicting_properties = True

## GUI 

## 색상 

define gui.accent_color = '#cc0066'

define gui.idle_color = '#707070'

define gui.idle_small_color = '#606060'

define gui.hover_color = '#cc0066'

define gui.selected_color = '#555555'

define gui.insensitive_color = '#7070707f'

define gui.muted_color = '#e066a3'
define gui.hover_muted_color = '#ea99c1'

define gui.text_color = '#000000'
define gui.interface_text_color = '#000000'


## 글자

## 글자
define gui.text_font = "Cafe24Supermagic.ttf"

## 캐릭터
define gui.name_text_font = "Cafe24Supermagic.ttf"

## 인터페이스
define gui.interface_text_font = "Cafe24Supermagic.ttf"

## 대사
define gui.text_size = 40

## 이름
define gui.name_text_size = 55

## 유저 인터페이스
define gui.interface_text_size = 50

## 유저 인터페이스에서 레이블
define gui.label_text_size = 36

## 통지
define gui.notify_text_size = 24

## 타이틀
define gui.title_text_size = 75


## 메인

define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## 대사 

## 대사 높이
define gui.textbox_height = 278

## 텍스트 박스 배치
define gui.textbox_yalign = 1.0

## 이름 배치
define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False


## 대사 위치
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## 픽셀값 대사 최대 너비
define gui.dialogue_width = 1116

## 대사 글자 수평 정렬
define gui.dialogue_text_xalign = 0.0


## 버튼
define gui.button_width = None
define gui.button_height = None

## 좌측, 상단, 우측, 하단 버튼 테두리 값
define gui.button_borders = Borders(6, 6, 6, 6)

define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#707070'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#7070707f'

## 위치와 간격 

## 네비게이션 버튼
define gui.navigation_xpos = 110

define gui.skip_ypos = 15

define gui.notify_ypos = 68

define gui.choice_spacing = 33

## 메인 버튼 간격
define gui.navigation_spacing = 30

## 환경 설정 간격
define gui.pref_spacing = 15

## 환경 설정 버튼 사이 간격
define gui.pref_button_spacing = 0

## 파일 페이지 버튼 간격
define gui.page_spacing = 0

## 파일 슬롯 간격
define gui.slot_spacing = 15

## 메인 메뉴 글자의 위치입니다.
define gui.main_menu_text_xalign = 1.0


## 프레임들 

define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)
define gui.frame_tile = False

## 수평 막대, 스크롤바, 슬라이더의 높이. 수직 막대, 스크롤바, 슬라이더 너비
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## 수평 테두리
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## 수직 테두리
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)
define gui.unscrollable = "hide"


## 대사록

## 대사록 보관
define config.history_length = 250

## 대사록 높이
define gui.history_height = 210

## 캐릭터 이름 GUI
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## 대사 GUI
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL모드 
## 배경 테두리
define gui.nvl_borders = Borders(0, 15, 0, 30)

## 렌파이가 표시할 NVL-mode 항목의 최대 수
define gui.nvl_list_length = 6


define gui.nvl_height = 173

## nvl 간격
define gui.nvl_spacing = 15

## 캐릭터 이름
define gui.nvl_name_xpos = 845
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## 대사 
define gui.nvl_text_xpos = 875
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0


define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


define gui.language = "unicode"

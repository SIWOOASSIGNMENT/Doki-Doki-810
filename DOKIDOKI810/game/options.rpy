define config.name = _("DOKI DOKI 810")

define gui.show_name = False

## 버전
define config.version = "1.0"

define gui.about = _p("""
""")

define build.name = "DOKIDOKI810"


## 음악

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


define config.main_menu_music = "background/background.mp3"


#
define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.intra_transition = dissolve

define config.after_load_transition = None

define config.end_game_transition = None


define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## 글자
default preferences.text_cps = 15

default preferences.afm_time = 15


define config.save_directory = "DOKIDOKI810-1702054942"



define config.window_icon = "gui/window_icon.png"


init python:


    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')

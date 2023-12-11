define none = Character('???')
define hapro = Character('하둥한 교수님')
define me = Character('나')

#image 613 = "schoolclass/613.png"
#image dormitory = "dormitory/dormitory.png"
image happy_end = "schoolclass/happy_end.png"

image hapro1 = im.FactorScale("professor/hapro.png",0.2)
image hapro2 = im.FactorScale("professor/hapro2.png",1.0)

image hat = im.FactorScale("hat/hat.png",1.0)
image F = im.FactorScale("F/F.png",1.0)

define hatCharacter = Position(xalign = 0.1, yalign = 0.5)
define rightCharacter = Position(xalign = 0.85, yalign = 1.0)

## 시작
label start:
    play music "audio/ingame/start1.mp3"

    $ name = renpy.call_screen("set_name",title="학생 이름은? (3글자 이상)", init_name="이름")
    $ na = Character( name , color="#ffffff")

    while len(name) <3:
        if len(name) <3:
            "3글자 이상 입력하세요" with vpunch
            $ name = renpy.call_screen("set_name",title="학생 이름은? (3글자 이상)", init_name="이름")
            $ na = Character( name , color="#ffffff")

    none "....." with dissolve
    none "..군...ㅇ..." with dissolve
    none "...[name[1]][name[2]]......." with dissolve
    none "...일어나..." with dissolve
    none "...[name[1]][name[2]]군 일어나......"with dissolve

    #scene 613
    show hapro at rightCharacter
    play music "audio/ingame/start2.mp3" loop

    none "[name]군 일어나게!!!!!!!!!" with vpunch
    none "수업 도중에 자면 어떡하나!!!!!!" with vpunch 
    
    menu:
        me "(누구더라...)"

        "에밀리아...?":
            me "에밀리아...?"
            none "에ㅁ..에밀리아? 너는 예의가 없군!!!!!!" with vpunch
        
        "선생님...?":
            me "선생님...?"
            none "비슷하지만 아직 정신을 덜 차렸나보군"

        "교수님...?":
            me "교수님...?"
            none "그래 정신을 차렸나"

    me "(그래 기억났다. 이분은 하둥한 교수님.)"
    me "(진지해 보이시지만 알고 보면 상냥한 분일지도...)" 

    hapro "어찌 됐든 곧 과제에 대해서 설명할거니 집중하도록"

    scene black with dissolve
    "([name]은(는) 과제를 받고 기숙사로 갔다)"

    #scene dormitory with dissolve
    me "하... 이놈의 학과는 무슨 매일 과제만 해야 해..."
    me "졸린데... 잘까"
    me "아니야... 아직 1학년인데 벌써 포기하면 안되지"
    me "근데 할 게 너무 많네..."

    ## 게임 선택지

    menu: 
        me "무슨 과제 할까?"

        "툴 공부해서 하둥한 교수님한테 과제 제출하기" :
            scene black with dissolve
            play music "audio/ingame/minigame.mp3"
            "([name]은(는) 노트북을 펼치고 과제를 시작한다)"
            call play_minigame from _call_play_minigame

            if _return < 3500:
                scene black with dissolve
                call bad_end from _call_bad_end
            elif _return >= 3500:
                scene black with dissolve
                call happy_end from _call_happy_end

        "교양 과제해서 일단 A+ 늘리기" :
            scene black with dissolve
            play music "audio/ingame/minigame.mp3"
            "([name]은(는) 노트북을 펼치고 과제를 시작한다)"
            "한 번도 실패하지 않고 10번 성공하세요"

            call begin_hunt from _call_begin_hunt

            if targets_hit <= 9:
                scene black with dissolve
                call bad_end from _call_bad_end_1
            if targets_hit > 9:
                scene black with dissolve
                call happy_end from _call_happy_end_1

    return


## 게임

init python:
    import pygame
    import time
    import random
    from os import path

    class gameDisplayable(renpy.Displayable):

        #이미지, 오브젝트, 변수 정의
        def __init__(self):

            renpy.Displayable.__init__(self)

            #사이즈
            self.DISPLAY_X = 1920
            self.DISPLAY_Y = 1080    
            self.COURT_LEFT = 0
            self.COURT_RIGHT = 1920
            self.PADDLE_WIDTH = 100
            self.PADDLE_HEIGHT = 100
            self.PADDLE_Y = self.DISPLAY_Y - 200
            self.PROFESSOR_Y = 50

            #과제스피드
            self.bx = []
            for i in range(6):
                self.bx.append(random.randrange(self.COURT_LEFT,self.COURT_RIGHT-100))
            self.by = []
            for i in range(6):
                self.by.append(100)
            self.bdy = .5
            self.bspeed = []
            for i in range(6):
                self.bspeed.append(random.randrange(1300,2300))
            
            #변수
            self.gameover = None
            self.submitstate = 0
            self.energynum = 0
            self.score = 0
            self.submity = self.PADDLE_Y
            self.Start_Time = time.time()

            #오브젝트
            self.player = Solid("#ffffff", xsize=80, ysize=80)
            self.professor = Image("minigame/professor.png")
            self.energyoutline = Solid("#ffffff", xsize=210, ysize=40)

            self.ball = Image("minigame/Blender.png")
            self.ball2 = Image("minigame/Ai.png")
            self.ball3 = Image("minigame/Ae.png")
            self.ball4 = Image("minigame/Python.png")
            self.ball5 = Image("minigame/Maya.png")
            self.ball6 = Image("minigame/cpp.png")

            self.submit = Image("minigame/submit.png")

            #커서 위치
            self.playery = (self.COURT_RIGHT - self.COURT_LEFT) / 2

            # The speed of the computer.
            self.computerspeed = 380.0

            # The time of the past render-frame.
            self.oldst = None

        def visit(self):
            return [self.player, self.ball]

        def render(self, width, height, st, at):
            r=renpy.Render(width, height)
                        
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            speed = []
            for i in range(6):
                speed.append (dtime * self.bspeed[i])

            for i in range(6):            
                self.by[i] += self.bdy * speed[i]

            #플레이어
            player = renpy.render(self.player, width, height, st, at)
            r.blit(player, (int(self.playery)-self.PADDLE_WIDTH / 2, int(self.PADDLE_Y)))

            #교수님
            professor = renpy.render(self.professor, width, height, st, at)
            r.blit(professor, (self.DISPLAY_X / 2 - 100, self.PROFESSOR_Y))

            #점수
            self.scoretext = Text("Score: "+str(self.score), size=50)
            score = renpy.render(self.scoretext, width, height, st, at)
            r.blit(score, (self.DISPLAY_X -400, 100))

            #체력
            energyoutline = renpy.render(self.energyoutline, width, height, st, at)
            r.blit(energyoutline, (self.DISPLAY_X / 2 - 105, self.DISPLAY_Y - 100))   

            self.energy = Solid("#39bf35", xsize=self.energynum, ysize=30)
            energy = renpy.render(self.energy, width, height, st, at)
            r.blit(energy, (self.DISPLAY_X / 2 - 100, self.DISPLAY_Y - 95))

            #과제
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx[0]), int(self.by[0])))
            ball2 = renpy.render(self.ball2, width, height, st, at)
            r.blit(ball2, (int(self.bx[1]), int(self.by[1])))
            ball3 = renpy.render(self.ball3, width, height, st, at)
            r.blit(ball3, (int(self.bx[2]), int(self.by[2])))
            ball4 = renpy.render(self.ball4, width, height, st, at)
            r.blit(ball4, (int(self.bx[3]), int(self.by[3])))
            ball5 = renpy.render(self.ball5, width, height, st, at)
            r.blit(ball5, (int(self.bx[4]), int(self.by[4])))
            ball6 = renpy.render(self.ball6, width, height, st, at)
            r.blit(ball6, (int(self.bx[5]), int(self.by[5])))
            
            for i in range(6):
                if self.PADDLE_Y < self.by[i]+50 < self.DISPLAY_Y:
                    self.bx[i] = random.randrange(self.COURT_LEFT,self.COURT_RIGHT-100)
                    self.by[i] = 100 
                    self.bspeed[i] = random.randrange(1300,2300)
                elif self.by[i]+50 > self.PADDLE_Y - self.PADDLE_HEIGHT:
                    if self.playery - self.PADDLE_WIDTH / 2 <= self.bx[i]+50 <= self.playery + self.PADDLE_WIDTH / 2:
                        self.bx[i] = random.randrange(self.COURT_LEFT,self.COURT_RIGHT-100)
                        self.by[i] = 100 
                        self.bspeed[i] = random.randrange(1300,2300)
                        self.score += 30
                        if self.energynum < 200:
                            self.energynum += 20 

            #과제 제출
            if self.energynum >= 200:
                submitText = Text("SPACE BAR를 눌러 제출!", size = 70)
                stt = renpy.render(submitText, 800, 100, st, at)
                r.blit(stt, (self.DISPLAY_X / 2 - 350, self.PADDLE_Y - 200))

            if self.submitstate == 1:
                submit = renpy.render(self.submit, width, height, st, at)
                r.blit(submit, (self.DISPLAY_X / 2 - 125, self.submity))
                self.submity -= self.bdy * dtime * 1300

            if self.submity <= self.PROFESSOR_Y + 100:
                self.score += 500
                self.submity = self.PADDLE_Y
                self.submitstate = 0

            if time.time()-self.Start_Time >= 30.:
                self.gameover = "gameover"
                renpy.timeout(0)

            #화면 계속 렌더링
            renpy.redraw(self, 0)

            return r

        def event(self, ev, x, y, st):
            #마우스 위치에 따라 x축 업데이트
            x = max(x, self.COURT_LEFT)
            x = min(x, self.COURT_RIGHT)
            self.playery = x

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    if self.energynum >= 200:
                        self.submitstate = 1
                        self.energynum = 0

            if self.gameover:
                return self.score
            else:
                raise renpy.IgnoreEvent()

screen game():

    default minigame = gameDisplayable()

    add minigame

label play_minigame:

    window hide  # Hide the window and quick menu while in pong
    $ quick_menu = False

    call screen game

    $ quick_menu = True
    window show
    
    return _return



## 엔딩 ##

image happy = "end/happy_end.png"
image bad = "end/bad_end.png"

## 해피 엔딩
label happy_end:

    scene happy_end with dissolve
    play music "audio/ingame/ending.mp3"

    me "하암...... 과제 제출하고 바로 잠들어버렸네..."
    me "우여곡절이 있었지만, 잘 마무리한 것 같다"
    me "어라...? 여긴 어디지...?"
    
    show hapro2 with dissolve

    hapro "허허 일어났나?"
    me "교수님..?"
    me "여긴 어디죠...?"
    hapro "허허허 자네 농담이 많이 늘었군"
    hapro "당연히 대학원이지 않나"
    hapro "이거 받게"

    show hat at hatCharacter with dissolve 

    hapro "대학원생이 된 걸 진심으로 축하하네"
    hapro "앞으로 열심히 해서 좋은 성과 내보자고"
    me "아...네...!"

    scene happy with dissolve
    "클릭해서 메인 메뉴로"

    return
    
## 배드 엔딩

label bad_end:
    
    #scene dormitory with dissolve
    play music "audio/ingame/ending.mp3"

    me "하암...... "
    me "으악!!! 과제 제출 못하고 자버렸다!!!" with vpunch

    scene black with dissolve
    "([name]은(는) 황급히 강의실로 달려갔다)"

    #scene 613 with dissolve

    me "허억...허억..."

    show hapro2 with dissolve

    hapro "자네 왔는가"
    hapro "과제가 형편없더군"
    me "죄송합니다..."
    hapro "허허허 죄송할 건 없지"
    hapro "아 이거 받게나"

    show F at hatCharacter with dissolve      
    hapro "자네 성적일세"

    scene bad with dissolve
    "클릭해서 메인 메뉴로"

    return

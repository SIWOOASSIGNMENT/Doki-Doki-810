image target:
    "hunt/target.png"
    zoom 0.5
image A:
    "A/A.png"

transform moving_target:
    ypos 275
    linear 3.0 xpos 2000
    xpos -300
    repeat

label begin_hunt:
    $ shots_fired = 0
    $ targets_hit = 0
    call hunting from _call_hunting
    return
    
label hunting:
    
    scene A
    show target at moving_target
    $ position = At(ImageReference("target"), moving_target)
    show expression position

    $ ui.imagebutton("hunt/crosshair.png", "hunt/crosshair_focused.png", clicked = ui.returns("fired"), xpos= 996, ypos = 163)
    $ fired_gun = ui.interact()
    
    show expression position
    if position.xpos > 950:
        if position.xpos < 1100:
            with vpunch
            "성공!"
            $ targets_hit = targets_hit + 1
            if targets_hit >= 10:
                return
            else:
                call hunting from _call_hunting_1
        else :
                return
            
    
    return

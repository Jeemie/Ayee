# Declare images below this line, using the image statement.



image mainmenu:

    "images/bg1.png"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 1.0
    linear 0.5 alpha 0.0
    pause 1.0
    "images/bg2.png"
    linear 1.0 alpha 1.0
    pause 1.0
    linear 0.5 alpha 0.0
    pause 1.0
    "images/bg4.png"
    linear 1.0 alpha 1.0
    pause 1.0
    linear 0.5 alpha 0.0
    "images/white.jpg"
    linear 0.50 alpha 1.0
    linear 0.25 alpha 0.0
    "images/bg3.png"
    linear 0.5 alpha 1.0
        
image mainmenu2:
    time 8.5
    block:
        "images/heart.png"
        linear 1.0 alpha 0.0
        pause 0.5
        linear 1.0 alpha 1.0
        pause 0.5
        repeat
    
image eileen happy = "eileen_happy.png"
image tree = "images/tree.jpg"
image black = "images/black.jpg"
image olin = "images/olin.jpg"
image goddard = "images/goddardentrance.jpg"
image labroom = "images/goddard_lab.jpg"
image dorm = "images/dorm.jpg"
image dininghall = "images/daka.jpg"
image quad = "images/quad.jpg"

image fsassy = "images/female_sassy.png"
image fhappy = "images/female_happy.png"
image fangry = "images/female_angry.png"
image fsad = "images/female_sad.png"
image flaughing = "images/female_laughing.png"

image mhappy = "images/male_happy.png"
image msad = "images/male_sad.png"
image mangry = "images/male_angry.png"
image mshocked = "images/male_shocked.png"

image nhappy = "images/twin_happy.png"
image nsad = "images/twin_sad.png"
image nangry = "images/twin_angry.png"
image nshocked = "images/twin_shocked.png"

image logo = "images/logo.png"

image bg1 = "images/bg1.png"
image bg2 = "images/bg2.png"
image bg3 = "images/bg3.png"
image bg4 = "images/bg4.png"
image heart = "images/heart.png"

image placeholder animated:
    im.Scale("images/tryagain.png", 400, 800)
    pause 1
    im.Scale("images/tryagain2.png", 400, 800)
    pause 1
    repeat


# Declare characters used by this game.
define f = persistent.f
define m = persistent.m
define p = Character('Professor', color="#c8ffc8")
define male = Character('Male', color="#c8ffc8")
define female = Character('Female', color="#c8ffc8")
define n = Character('Nick', color="#c8ffc8")


#Animation("images/tree.jpg", 2.0, "images/bg1.png", 2.0, "images/bg2.png", 2.0)
transform basicfade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 0.5 alpha 0.0    
           

transform dim:
    alpha 1.0
    linear 1.0 alpha 0.5

transform mmenu:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 1.0
    linear 0.5 alpha 0.0
    pause 1.0
    
transform mmenu2:
    linear 1.0 alpha 1.0
    pause 1.0
    linear 0.5 alpha 0.0

transform mmenu3:
    
    linear 0.50 alpha 1.0
    linear 0.25 alpha 0.0
    
transform mmenu4:
    linear 0.5 alpha 1.0
    
transform mmenu5:
    linear 1.0 alpha 0.0
    pause 0.5
    linear 1.0 alpha 1.0
    pause 0.5
    repeat
        
transform undim:
    linear 1.0 alpha 1.0
    
transform fastfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0
    
#some labels

label splashscreen:
    scene white
    show logo at basicfade,truecenter
    with Pause(4)
    hide logo at basicfade
    scene black with dissolve
    with Pause(1)

    show text "Spell Shaded presents to you..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return
    
    
#show text "" at basicfade,truecenter with Pause(2.5)
#pause 1
#hide text at basicfade
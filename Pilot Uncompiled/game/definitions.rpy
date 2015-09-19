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
    "images/white.jpg"
    linear 0.50 alpha 1.0
    linear 0.25 alpha 0.0
    "images/bg3.png"
    linear 0.5 alpha 1.0
        
image mainmenu2:
    time 7.0
    block:
        "images/heart.png"
        linear 1.0 alpha 0.0
        pause 0.5
        linear 1.0 alpha 1.0
        pause 0.5
        repeat
    
image eileen happy = "eileen_happy.png"
image bg tree = "images/big_tree"
image bg black = "images/black.jpg"
image fsassy = "images/female_sassy.png"
image fhappy = "images/female_happy.png"
image fangry = "images/female_angry.png"
image placeholder animated:
    im.Scale("images/tryagain.png", 400, 800)
    pause 1
    im.Scale("images/tryagain2.png", 400, 800)
    pause 1
    repeat
image bg olin = "images/olin.jpg"
image bg goddardlab = "images/goddard_lab.jpg"

# Declare characters used by this game.
define p = Character('Professor', color="#c8ffc8")
define male = Character('Male', color="#c8ffc8")
define female = Character('Female', color="#c8ffc8")


#Animation("images/tree.jpg", 2.0, "images/bg1.png", 2.0, "images/bg2.png", 2.0)
transform basicfade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 0.5 alpha 0.0    
           
           
transform dim:
    linear 1.0 alpha 0.5
    
    
transform undim:
    linear 1.0 alpha 1.0
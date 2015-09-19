# Declare images below this line, using the image statement.


image eileen happy = "eileen_happy.png"
image bg tree = "big_tree"
image bg black = "black.jpg"
image fsassy = "female_sassy.png"
image fhappy = "female_happy.png"
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


transform basicfade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 0.5 alpha 0.0    
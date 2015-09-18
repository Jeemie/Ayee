image eileen happy = "eileen_happy.png"
image bg tree = "big_tree"
image girl school = im.Scale("images/schoolgirl.jpeg", 400, 800)
image girl angry = im.Scale("images/schoolgirla.jpeg", 400, 800)
image white blank = im.Scale("images/blank1.png", 500, 375)
image placeholder = im.Scale("images/placeholder.png", 400, 800)
image placeholder animated:
    im.Scale("images/tryagain.png", 400, 800)
    pause 1
    im.Scale("images/tryagain2.png", 400, 800)
    pause 1
    repeat
image olin = im.Scale("images/olin.jpg", 1280, 1080)
image goddard lab = im.Scale("images/wpi_top.jpg", 1280, 1080)
# Declare characters used by this game.
define f = Character('Professor', color="#c8ffc8")
define m = Character('Male', color="c8ffc8")

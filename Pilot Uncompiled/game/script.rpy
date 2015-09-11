# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image eileen happy = "eileen_happy.png"
image bg tree = "big_tree"
image girl school = "images/schoolgirl.jpeg"
image white blank = im.Scale("images/blank1.png", 500, 300)
image placeholder = im.Scale("images/placeholder.png", 250, 500)
image placeholder animated:
    im.Scale("images/tryagain.png", 250, 500)
    pause 0.1
    im.Scale("images/tryagain2.png", 250, 500)
    pause 0.1
    repeat
    
# Declare characters used by this game.
define f = Character('Female', color="#c8ffc8")
define m = Character('Male', color="c8ffc8")

# The game starts here.
label start:

scene bg tree
#show placeholder at Position(xpos = 0, xanchor= 0, ypos= 0.25, yanchor = 1)
show placeholder animated at Position(xpos = 0, xanchor= 0, ypos= 0.25, yanchor = 1)

#show white blank

m "Do you really think I'd do that? I just... I wouldn't want to hurt you. That's because... I..."
    
return

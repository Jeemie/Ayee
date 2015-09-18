# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image eileen happy = "eileen_happy.png"
image bg tree = "big_tree"
image girl school = im.Scale("images/schoolgirl.jpeg", 250, 500)
image girl angry = im.Scale("images/schoolgirla.jpeg", 250, 500)
image white blank = im.Scale("images/blank1.png", 500, 300)
image placeholder = im.Scale("images/placeholder.png", 250, 500)
image placeholder animated:
    im.Scale("images/tryagain.png", 250, 500)
    pause 0.1
    im.Scale("images/tryagain2.png", 250, 500)
    pause 0.1
    repeat
image olin = im.Scale("images/olin.jpg", 800, 600)
image goddard lab = im.Scale("images/wpi_top.jpg", 800, 600)
# Declare characters used by this game.
define f = Character('Professor', color="#c8ffc8")
define m = Character('Male', color="c8ffc8")

# The game starts here.
label start:
scene olin
show placeholder animated at Position(xpos = 0, xanchor= 0, ypos= 0.25, yanchor = 1)

f "What's your name?"
$ male = renpy.input("This is it! I will call myself..")

$ male = male.strip()
$ blank = "%(male)s"
if male == "":
    $ male="Blank"
    $ blank="a"
male "My name is %(male)s !"
if blank == "a":
    f "Woah, you're not trying to copy NGNL, are you?!"
#scene bg tree
#show placeholder at Position(xpos = 0, xanchor= 0, ypos= 0.25, yanchor = 1)


#show white blank

#f "Do you really think I'd do that? I just... I wouldn't want to hurt you. That's because... I..."
hide placeholder animated
show girl school at Position(xpos = 0, xanchor= 0, ypos= 0.25, yanchor = 1)
"Cute Girl" "Nice to meet you, %(male)s !"
$ female = renpy.input("Choose a name for the girl:")
$ female = female.strip()
if female == "":
    $ female="Natalie"
female "My name is %(female)s."
female "We're assigned as partners in this class! You did check your email, right?"
#

hide girl school

show goddard lab
with dissolve
show girl school at Position(xpos= 0.75, xanchor= 0, ypos= 0.25, yanchor = 1)

female "Hey, let's get started!"
menu:
    "Okay!":
        female "Awesome!"
    "You can do it all. I'll just watch..":
        hide girl school
        show angry at Position(xpos= 0.75, xanchor= 0, ypos= 0.25, yanchor = 1)
        female "NO."
        with vpunch
        play sound "sfx/punch.mp3"
        female "DOING THAT IS BAD."
        with vpunch
        play sound "sfx/punch.mp3"
        female "YOU'LL GET ME EXPELLED!"
        with vpunch
        play sound "sfx/punch.mp3"
        male "Okay.. okay.."

return

# You can place the script of your game in this file.
# Declare characters used by this game.

# The game starts here.
label start:
scene black with dissolve
show text "Day One \n Chemistry Class" at basicfade with Pause(2.5)
scene black with dissolve

scene olin with dissolve

male "{i}It's the first day of classes. I remember facing this day so many times in high school.{/i}"

male "{i}Back then, I wasn’t so prepared. Everything seemed so intimidating, and everyone had their own friends.{/i}"

male "{i}So I ended up just keeping to myself. And it wasn’t so bad! I was fine on my own, and I had some friends at school.{/i}"

male "{i}But I feel like I missed out on something – an entire world I don’t know about. So college is going to be different!!!{/i}"

male "{i}...Or, at least that was the plan. I’ve been here a week and I don’t even know one person’s name.{/i}"

male "{i}I thought Worcester Polytechnic Institute would be the perfect school. I mean, WPI’s great, but I have no skills when it comes to talking with people.{/i}"

male "{i}I’m determined to change that though! Starting now, I’ll make a ton of friends! I’ll go out and have fun and make the most of my time!{/i}"

p "Hello? I was asking you your first name."

"The teacher is staring at you with a piece of paper in her hand. It seems to be a checklist of people’s names in the chemistry class."

male "{i}O-Oh crap! I must have spaced out.{/i}"

male "M-my name? Oh, it's... uh..."
scene olin at dim
show black behind olin


$ m = renpy.input("Type your name here")
$ m = m.strip()
$ blank = "%(m)s"
if m == "":
    $ m="Blank"
    $ blank="a"
    "My name is %(m)s!"
if blank == "a":
    p "Woah, you're not trying to copy NGNL, are you?!"
scene olin at undim
pause 1.0


p "Alright then. %(m)s it is."

"She checks your name off her list and moves onto the next person."

m "{i}I almost couldn’t remember my own name. Class hasn’t even started yet and I’m screwing everything up.{/i}"

m "{i}Things can only get better now, though!{/i}"

p "Alright, we’re going to get straight down to business. For this marking period your grades will be divided into three different portions: homework, projects, and the final exam."

p "The exam is self-explanatory, and for the homework, you will be required to read from your textbooks each week, as well as finishing assignments that will be posted online."

p "Finally, for the entirety of the course you will be assigned a single partner who you will share work with on projects and lab days."

p "You are each required to turn in the assignments separately, but you may have the exact same papers."

m "{i}By this point I wasn’t even listening anymore. My mind was racing at what the professor insinuated.{/i}"

m "{i}We’re gonna have partners who are forced to be with us! This might just be my chance to make a friend here. It might even be a girl too...{/i}"

m "{i}Oh crap, what am I supposed to do if it is a girl? Is it just like with guys? What if she’s also shy? That would be pretty bad...{/i}"

m "{i}But if she’s too enthusiastic then she could be annoying!{/i}"

m "{i}Ahhh, what am I saying?! I don’t even know if it will be a girl! I should stop worrying.{/i}"

p "Alright, now I’ll give you the rest of the time in class to find your partners and discuss your schedules."

m "{i}Crap! Did she announce everyone’s partner? I didn’t even hear it! I was way too distracted.{/i}"

m "{i}How am I supposed to find my partner then? And I still don’t even know who it is. Maybe they’ll find me...{/i}"

"There’s a slight tap on your back, and your heart involuntarily jumps in your chest. You’re so on edge today that you could have a heart attack at any time."
play sound "sfx/punch.mp3"
pause 0.1
with vpunch

"You take a deep breath to quickly calm yourself and turn around to find..."

show fhappy at basicfade, center
female "Hey there! It’s nice to meet you! If I heard right, your name is %(m)s, right? Did you remember my name?"

"It’s a cute girl!"

"Your heart is beating out of your chest as you throw out the first name that comes to mind."

m "O-oh, yeah, I d-did! Uhh, yeah, my name’s %(m)s, and you’re...uhh...you're ...?"
hide fhappy at basicfade
show olin at dim
show black behind olin

show fsassy at basicfade, left with moveinleft
$ f = renpy.input("Choose a name for the girl:")
$ f = f.strip()
if f == "":
    $ f = "Natalie"
show olin at undim
pause 1.0
hide black

f "My name is %(f)s."

f "Yeah, that’s it! I was just making sure you were paying attention. It’s nice to meet you! I’m sure we’re gonna be great partners. We should get going before the next class comes in, though."

menu:
    "As long as you don't slow me down.":
        hide fsassy
        show fangry
        f "Well fine, if you don’t want to work with me, I’ll go get a different partner."
        "She immediately goes over to the professor and although you can’t hear everything, it doesn’t sound good for you." 
        "Afterward, the professor comes over and tells you that the two of you would be working with different partners."
        scene black with dissolve
        show text "Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
    "It is a pleasure to work with you, m'lady.":
        hide fsassy at basicfade
        show fhappy at basicfade, left
        f "We should get going before the next class comes in though!"
    "W-Wait, I actually have to work with a girl?!":
        hide fsassy
        show fangry
        f "Well fine, if you don’t want to work with me, I’ll go get a different partner."
        "She immediately goes over to the professor and although you can’t hear everything, it doesn’t sound good for you." 
        "Afterward, the professor comes over and tells you that the two of you would be working with different partners."
        scene black with dissolve
        show text "Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
    "I-It's nice to meet you!":
        hide fsassy at basicfade
        show fhappy at basicfade, left
        f "We should get going before the next class comes in though!"
"You notice that you’re the last two left in the classroom and students for the next class are about to come in."

f "So, we should plan a time to get together and plan everything out."

m "Well, I’m free right now, if you’re not busy."

f "I actually have a class right now, but how about we meet at the giant tree tomorrow at 5:00?"

m "O-Ok, that works for me! I’ll see you then."

f "Yeah, bye for now."

"You completely forget that you were going to go to the robotics club meeting at 5:00, but you decide that that’s not important anymore."

#scene bg tree
#show placeholder at Position(xpos = 0, xanchor= 0, ypos= 0.25, yanchor = 1)
#################################################

#show white blank

#f "Do you really think I'd do that? I just... I wouldn't want to hurt you. That's because... I..."
#hide placeholder animated
#show girl school at Position(xpos = 0, xanchor= 0, ypos= 0.25, yanchor = 1)

#hide girl school

#show goddard lab
#with dissolve
#show girl school at Position(xpos= 0.75, xanchor= 0, ypos= 0.25, yanchor = 1)

#menu:
#    "Okay!":
#        female "Awesome!"
#    "You can do it all. I'll just watch..":
#        hide girl school
#        show angry at Position(xpos= 0.75, xanchor= 0, ypos= 0.25, yanchor = 1)
#        female "NO."
#        with vpunch
#        play sound "sfx/punch.mp3"
#        female "DOING THAT IS BAD."
#        with vpunch
#        play sound "sfx/punch.mp3"
#        female "YOU'LL GET ME EXPELLED!"
#        with vpunch
#        play sound "sfx/punch.mp3"
#        male "Okay.. okay.."

jump scene2

return

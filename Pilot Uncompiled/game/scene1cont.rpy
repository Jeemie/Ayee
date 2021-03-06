﻿label scene1cont:
scene black with dissolve
show text "Day One \n Chemistry Class" at basicfade with Pause(2.5)
scene black with dissolve

$ f = persistent.f
$ m = persistent.m

show olin with dissolve

m "{i}It's the first day of class. I remember facing this day so many times in high school.{/i}"

m "{i}Back then, I wasn't so prepared. Everything seemed so intimidating, and everyone had their own friends.{/i}"

m "{i}So I ended up just keeping to myself. And it wasn't so bad! I was fine on my own, and I had some friends at school.{/i}"

m "{i}But I feel like I missed out on something – an entire world I don't know about. So college is going to be different!{/i}"

m "{i}...Or, at least that was the plan. I've been here a week, and I don't even know one person's name.{/i}"

m "{i}I thought Worcester Polytechnic Institute would be the perfect school. I mean, WPI's great, but I have no skills when it comes to talking to people.{/i}"

m "{i}I'm determined to change that, though! Starting now, I'll make a ton of friends! I'll go out, have fun, and make the most of my time!{/i}"

p "Hello? I was asking you for your first name."

show text "The teacher is staring at you with a piece of paper in her hand. It seems to be a checklist of the names of the students in the chemistry class." at basicfade,truecenter with Pause(9.0)
pause 2.0
hide text at fastfade 

m "{i}O-Oh crap! I must have spaced out.{/i}"

m "M-my name? Oh, it's...uh..."

m "%(m)s!"

p "Alright then. %(m)s it is."


"She checks your name off her list and moves onto the next person."

m "{i}I almost couldn't remember my own name. Class hasn't even started yet, and I'm screwing everything up!{/i}"

m "{i}Things can only get better now, though!{/i}"

p "Alright, we're going to get straight down to business. For this marking period, your grades will be divided into three different portions: homework, projects, and the final exam."

p "The exam is self-explanatory. As for the homework, you will be required to read from your textbook each week, as well as to finish assignments that will be posted online."

p "Finally, for the entirety of the course, you will be assigned a single partner, who will work with you on projects and lab days."

p "You are each required to turn in the assignments separately, but you may have exactly the same papers."

m "{i}By this point, I wasn't even listening anymore. My mind was racing at what the professor insinuated.{/i}"

m "{i}We're going to have partners who are forced to be with us! This just might be my chance to make a friend here. It might even be a girl, too...{/i}"

m "{i}Oh crap, what am I supposed to do if it is a girl? Is it just like with guys? What if she's also shy? That would be pretty bad.{/i}"

m "{i}But if she's too enthusiastic, then she could be annoying!{/i}"

m "{i}Ahhh, what am I saying?! I don't even know if it will be a girl! I should stop worrying.{/i}"

p "Alright, now I'll give you the rest of the time in class to find your partners and discuss your schedules."

m "{i}Crap! Did she announce everyone's partner? I didn't even hear it! I was way too distracted.{/i}"

m "{i}How am I supposed to find my partner now? And I still don't even know who it is. Maybe they'll find me...{/i}"

show olin at dim
show black behind olin
show text "There's a slight tap on your back, and your heart involuntarily jumps in your chest. You're so on edge today that you could have a heart attack at any time." at basicfade,truecenter with Pause(9.0)
$ renpy.pause(3.0, hard='True')
hide text at basicfade

$ renpy.pause(1.0, hard='True')
show text "You take a deep breath to quickly calm yourself. You turn around to find..." at basicfade,truecenter with Pause(4.2)
$ renpy.pause(3.0, hard='True')
hide text at basicfade
pause 1.0
show olin at undim
pause 1.0
hide black

show fhappy at basicfade, center
female "Hey there! It's nice to meet you! If I heard right, your name is %(m)s, right? Did you remember my name?"

hide fhappy at fastfade
show olin at dim
show black behind olin
show text "It's a cute girl!" at basicfade,truecenter with Pause(1.2)
$ renpy.pause(1.0, hard='True')
hide text at basicfade

$ renpy.pause(1.0, hard='True')
show text "Your heart is beating out of your chest as you throw out the first name that comes to mind." at basicfade,truecenter with Pause(5.7)
$ renpy.pause(3.0, hard='True')
hide text at basicfade
pause 1.0
show olin at undim
pause 1.0
hide black
pause 1.0
show fhappy at basicfade,center

m "O-oh, yeah, I d-did! Uhh, yeah, my name's %(m)s, and you're...uhhh...you're..."

m "Your name is %(f)s."

f "Yeah, that's it! I was just making sure you were paying attention. It's nice to meet you! I'm sure we'll be great partners. We should get going before the next class comes in, though."

menu:
    "{size=40}{b}As long as you don't slow me down.{/b}":
        hide fhappy at fastfade
        show fangry at fastfade
        f "Well fine, if you don't want to work with me, I'll go get a different partner."
        "She immediately goes over to the professor, and although you can't hear everything, it doesn't sound good for you." 
        "Afterward, the professor comes over and tells you that the two of you will be working with different partners."
        scene black with dissolve
        show text "Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
    "{size=40}{b}It is a pleasure to work with you, m'lady.{/b}":
        f "We should get going before the next class comes in!"
    "{size=40}{b}W-wait, I actually have to work with a girl?!{/b}":
        hide fhappy at fastfade
        show fangry at fastfade
        f "Well fine, if you don't want to work with me, I'll go get a different partner."
        "She immediately goes over to the professor, and although you can't hear everything, it doesn't sound good for you." 
        "Afterward, the professor comes over and tells you that the two of you will be working with different partners."
        scene black with dissolve
        show text "Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
    "{size=40}{b}I-it's nice to meet you!{/b}":
        f "We should get going before the next class comes in."

hide fhappy at fastfade
show olin at dim
show black behind olin
show text "You notice that you're the last two left in the classroom. Students from the next class are about to enter." at basicfade,truecenter with Pause(6.3)
$ renpy.pause(3.0, hard='True')
hide text at basicfade
pause 1.0
show olin at undim
pause 1.0
hide black
show fhappy at basicfade,left

f "So, we should plan a time to get together and plan everything out."

m "Well, I'm free right now, if you're not busy."

f "I actually have a class right now, but how about we meet at the giant tree tomorrow at 5:00?"

m "O-okay, that works for me! I'll see you then."

f "Yeah, bye for now."

hide fhappy at fastfade

pause 0.5
show olin at dim
show black behind olin
show text "You completely forget that you were going to go to the robotics club meeting at 5:00, but you decide that's not important anymore." at basicfade,truecenter with Pause(6.9)
$ renpy.pause(3.0, hard='True')
hide text at basicfade

jump scene2
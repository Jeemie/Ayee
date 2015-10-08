label fscene1:
scene black with dissolve
show text "New Beginning" at basicfade with Pause(2.5)
scene black with dissolve

show olin at fastfade

stop music
play music "music/start.mp3"

female "{i}College is so much different than high school.{/i}"

female "{i}In high school, my friends and I would all make sure we got seats together. Not like that made a difference – they weren't really my friends.{/i}"

female "{i}Everyone here is so much more real. There's no sense in hiding yourself because there's nothing to be ashamed of! I can actually feel comfortable with myself and not have to watch everything I do.{/i}"

female "{i}I've already met so many different people! The girls in my dorm, the guys upstairs who bother us, sporty girls, bros, nerds – there's a bit of everything!{/i}"

female "{i}The one thing everyone definitely has in common is that they're all so smart! I really hope I can keep up.{/i}"

female "{i}It's probably a good idea that I start to plan my schedule right now! Let's see...next week, I want to see the art club. I'll also have to meet with my academic advisor to talk about my schedule.{/i}"

female "{i}I'll probably need to go to some help sessions for these classes. They seem hard already – and we haven't even started! I also promised I'd meet my friend Katie at lunch.{/i}"

p "Hello? I was asking you for your first name."

"The teacher is staring at you with a piece of paper in her hand. It seems to be a checklist of the names of the students in the chemistry class."

female "Oh! I'm so sorry. I wasn't paying attention at all. My name is..."

$ persistent.f = renpy.input("Choose a name for the girl:")
$ persistent.f = persistent.f.strip()
if persistent.f == "":
    $ persistent.f = "Natalie"
    $ f = persistent.f
$ f = persistent.f

show olin at undim
pause 1.0
hide black
f "My name is %(f)s."

p "Alright then, %(f)s it is."

"She checks your name off her list and moves onto the next person."

f "{i}I really shouldn't be spacing out like that. Did I not get enough sleep last night?{/i}"

f "{i}But it's the first day of classes! I shouldn't be tired on the first day.{/i}"

f "{i}I'll have to make sure I get enough sleep. That really wasn't a good first impression.{/i}"

p "Alright, we're going to get straight down to business. For this marking period, your grades will be divided into three different portions: homework, projects, and the final exam."

p "The exam is self-explanatory. As for the homework, you will be required to read from your textbook each week, as well as to finish assignments that will be posted online."

p "Finally, for the entirety of the course, you will be assigned a single partner, who will work with you on projects and lab days."

p "You are each required to turn in the assignments separately, but you may have exactly the same papers."

p "Now, I'm going to leave this paper here on the blackboard. You may find your names and your partners' names and meet with them for the rest of the class. Make sure you decide on a time to meet during the week to finish the lab assignments."

"You walk up to the desk at the front of the room to see who exactly your partner is."

"You look up your own name. Listed right next to your name is your partner's."

f "Hmm? How exactly do you pronounce this? Well, I'm guessing the name must be..."

"You take a look around the classroom and notice that most everyone has already paired up with a partner. There is only one person left sitting in his desk, seemingly not paying attention to anything."

show msad at fastfade,center
f "Hmm...how should I approach this..."

menu:
    "{size=40}{b}Sneak up and surprise him!{/b}":
        "You decide to take a tactical approach and go around, walking up slowly so his back is facing you."
        "You tap him on the shoulder gently. He nearly jumps out of his seat."
    "{size=40}{b}Walk up and say hi.{/b}":
        "You decide to go straight up to him and say hi."
        "As you approach, you see him snap out of his daze and look up to you."
    "{size=40}{b}Wait for him to come to you.{/b}":
        "You stand at the front of the room for a while, glancing at him every once in a while to see if he'll come and say hello, but he remains in his seat until the end of class. Then he gets up and leaves."
        "You also decide to head out, but you never end up getting in contact with your partner."
        scene black with dissolve
        show text "Bummer \n Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
        
hide msad at fastfade
show mshocked at fastfade, center

f "Hi there! My name's %(f)s, and we're going to be partners!"

male "O-Oh! H-Hey there! Sorry, I wasn't paying too much attention. My name is..."

show olin at dim
show black behind olin
$ persistent.m = renpy.input("Type his name here")
$ persistent.m = persistent.m.strip()
if persistent.m == "":
    $ persistent.m="Blank"
    $ blank="a"
    $ m = persistent.m
    "My name is %(m)s!"
$ m = persistent.m

show olin at undim
pause 1.0
hide black

hide mshocked at fastfade
show mhappy at basicfade, center

f "Well, I hope you don't do that when we're working – 'cause I know nothing about chemistry. It'd be pretty bad if neither of us did the work."

m "I-I'm sure that's not true. W-we'll both do the work, and it won't be so bad. I'm sure of it."

m "We should get going before the next class comes in."

"You notice that you're the last two left in the classroom. Students from the next class are about to enter."

f "So, we should plan a time to get together and plan everything out."

m "Well, I'm free right now, if you're not busy."

f "I actually have a class right now, but how about we meet at the giant tree at 5:00?"

m "O-okay, that works for me! I'll see you then."

f "Yeah, bye for now!"

show olin at fastfade
show black behind olin
show olin at dim

show text "He seemed a bit strange, as if he were really nervous, but you have no idea why. You guess it must be because it's the first day of classes." at basicfade,truecenter with Pause(8.7)
pause 1
hide text at basicfade
pause 1.0

show text "Hopefully, he isn't hard to deal with." at basicfade,truecenter with Pause(2.1)
pause 1
hide text at basicfade
pause 1.0

jump fscene2

return
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

scene bg dorm

"It’s almost 5:00 pm and you’re sitting in your room waiting to head out to meet %(f)s. It’s a good thing your roommates are out or they might get annoyed with all the pacing you’re doing."

m "{i}It’s nothing to be worried about. I'm supposed to be there, and I’ll talk about...things. And if not, there’s always chemistry work to fall back on.{/i}"

m "{i}But I can’t help thinking how cute she was.{/i}"

m "{i}But I might scare her away.{/i}"

m "{i}But I'm gonna be late if I don’t leave.{/i}"

m "{i}Alright, I’m heading out then!{/i}"

scene bg tree
m "{i}There she is! Wow, I don’t think I got a very good look at her yesterday, but she looks...{/i}"

show fangry

f "There you are!! You’re late! I’ll have you know my time is very precious!"

m "Sorry! I’m sorry!"

m "{i}Mad. She looks pretty mad. I’m not that late am I?{/i}"

f "I knew you weren’t gonna make it in time, didn’t you hear me before?"

m "{i}In class? She didn’t say anything about me being late.{/i}"

m "A-Ah no, I guess I must have missed it. I’m really sorry I’m late, but I’m here now, so we should...get things going, I guess?"

show fhappy
f "Yeah, you’re right. Well, we’ve already introduced ourselves yesterday, so let’s get down to business! I’m free on Wednesdays from 6-8 and then I’m also available at 1, but I have a class at 3 so we might be pressed for time then."

m "Wednesday at 6 works for me!"

f "Alright then! I guess we could bring dinner with us, or if you’re free before that then we can go get some together."

"You can’t stop your heart from pounding when you hear that. Going to get dinner together? Just the two of you? It’s almost like a date!"

f "I guess that’s everything we really need to cover. I guess we could have just e-mailed each other, but this was good anyway."

m "Do you want to go get something to eat right now?"

m "{i}What did I just say?{/i}"

f "Well, I have to get back to my homework later, but, sure! I haven’t eaten yet."

"You let out the breath you hadn’t even known you were holding and smiled. Your legs were shaking a bit, but you were too happy to stop them, and you were certain she wouldn't notice."

m "Great! I th-think they might have Chinese food in the dining h-hall today!"

"You prayed that you would be able to stop stuttering soon as the two of you headed toward the dining hall."

scene bg dininghall
show fshocked
f "No way!! You were a championship fencer??"

m "Well, it’s not that I was that good or anything, but my sophomore year of high school I made it to the semi-finals of this national tournament. At the time I was ranked 4th in the US for my age."

show fhappy
f "That’s so incredible! You must have been awesome at it. So does that mean you’re gonna join the fencing team here?"

m "Well, no, I didn’t plan to..."

f "Why not? It sounds like you’d do really well in it."

m "I guess...but I haven’t actually fenced since I was 15."

f "But you said you had made it to the national championship – why stop after that?"

m "{i}Is this something I should be sharing with a girl I just met? But there’s something that makes me just...trust her.{/i}"

m "After the championship I quit fencing to focus on getting into college. My parents had supported me completely while I was fencing, but I knew that they were having trouble keeping up with everything."

m "With work, and taking me to fencing classes, and then to another state for the championships, I didn’t want to burden them any more."

f "Wow, that’s really nice of you! But now that your parents don’t have to worry about you, you could always start up again, right?"

m "I...I never thought of that. You’re right, I could."

m "But - I don’t know – it’s been a long time since I've fenced."

f "Oh, I’m sure it’s just like riding a bicycle! You’d definitely get back into it!"

m "{i}Maybe I could,but I don’t want to think about that now, all of my focus should be on %(f)s.{/i}"

m "So what about you? I told you what I like to do, so what interests you?"

f "Well, I’m actually really big into art. When I was younger, I always loved art classes and drawing and painting."

f "What I really love though, is creating things – taking empty space and filling it with something grand and beautiful! I {b}love{/b} sculpting and designing – making something that I can love and that others can see!"

f "So that’s why I came here – to become a civil engineer. One day, I’m gonna build something big and beautiful in a city or a town, or even something just for me."

m "{i}Wow, that’s a big dream. It’s kind of strange to know someone who already has their life planned out. Something inside me knows that she’ll be able to do it, too.{/i}"

m "That sounds incredible. I’ve never thought that way about making things: everyone can see it, but you can still call it yours. Actually, that sounds kind of scary. I mean, what if nobody likes it?"

f "Well then, that’s their problem! Besides, what makes you so sure everybody’s going to hate what I make?!"

m "A-Ah, n-no! I didn’t mean it like that! I think w-whatever you’d make would be incredible!"

"Your face is nearly red now as you try to reconcile her, but you completely stop when you see her wide grin."

show flaughing
f "Hahahaha! I’m just kidding, %(m)s. I knew what you meant! It {b}is{/b} fun to tease you, though. You turned pretty red there, too!"

m "{i}I got played! But I don’t really mind. It feels nice talking to her like this.{/i}"

"A bit later, you both check the time and find that you’ve been in the dining hall talking for 2 hours. You both get up in a hurry and exchange phone numbers before heading out. This is the first night at college that you’ve fallen asleep feeling truly content."

scene bg black
"Today is now Tuesday and you have your chemistry class again. The thought of seeing %(f)s again makes you get to class a bit earlier than you normally would."

scene bg classroom
"When you get there, you notice that she hasn’t arrived yet, and there’s hardly anyone else there. Since you have no idea where she was sitting the other day, finding a seat next to her would be nearly impossible."

"You decide to go back to the seat you were originally sitting in and wait for class to start. Last night you had trouble sleeping, and you're paying for it now. You feel so tired that your eyes keep closing against your will."

"???" "Somebody must have had a rough night."
with vpunch

"You jump in your seat, startled at the sudden voice. Looking around, there are many more people in the room now, and sitting next to you is %(f)s."

show fhappy
f "Hi there, %(m)s. I’m glad I could scare you awake! It’s pretty funny to make you jump. Did you not sleep last night?"

m "H-Hey, %(f)s! Uh, no, I didn’t sleep very well for some reason...I think it has to do with the heat here."

f "You’re right. You’d think in Massachusetts it would be a bit colder at the beginning of fall. It doesn’t really bother me though!"

m "Yeah, you seem perfectly fine in the heat. Was it very hot where you came from?"

f "I lived in North Carolina most of my life, so it was pretty hot for most of the year. My grandparents live in Massachusetts though, so I’ve been up here many times, especially in the winter when it’s full of snow."

"As you’re about to respond, the professor walks into the room and calls for everybody’s attention. The class goes by quickly, but you feel like you would’ve fallen asleep if you hadn’t had %(f)s sitting next to you."

"After class, you both say goodbye and remind each other about your meeting the next day. The rest of the day seems a bit brighter now than it had before your chemistry class."

scene bg labroom
show fangry
f "Ahh! I can’t understand this at all! Why do we need to figure out how they’re going to react? Why don’t we just combine them all and see what happens? Isn’t that what experimentation is?"

menu:
    "Go for it!":
        "She pours every chemical within reach into a single beaker, an excited smile on her face. You can’t help but admire her adventurous attitude and look on in wonder as her experiment bubbles."
        show fhappy
        f "Look! It’s doing something! I told you, experiments should –"
        show bg explosion
        "There isn’t any time to react as the solution bubbles to a climax and explodes in her face. You can’t feel anything as you’re caught in the blast."
        scene black with dissolve
        show text "Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
    "Maybe we should try something else...":
        m "I guess so, but I’m sure they don’t want us to cause an explosion. Besides, it’s not so hard. We just have to look up the chemical compounds they’ll form."

f "I’m just not good at chemistry. I took it in high school, so I thought it would be easy now, but I still don’t get it! I’m doomed!"

m "Don’t worry. Since we’re partners, I’ll be here to help, and I’ll make sure you don’t fail! I’ll teach you everything you need to know."

f "You would? Ohh, thank you so much, %(m)s! That’s so nice of you!"

"You then notice that her arms are around you, and you’re pulled into a hug. She nearly squeezes some of the life out of you, but you enjoy it nonetheless. Your cheeks momentarily turn red in the process, but you don’t think she noticed."

"The rest of your lab time is spent performing various infusions of chemicals as you explain their properties to your partner. You feel a warm connection between the two of you, and you hope that you’re not the only one who feels it."

scene bg black
show fhappy
f "So hey...There’s this concert in Boston this week that I’d love to see, but most of my friends are going home over the weekend."

m "Dang, that really sucks. Is there anybody else you can ask?"

f "Well...do you want to go?"

m "Hmm..."

m "O-Oh! Y-Yeah! I’d love to – I mean, that sounds pretty awesome. Of course I’ll go!"

"The two of you began spending more time together."

"Over the next three weeks, the two of you continue your routine lab work and usually find time to eat dinner together during the week."

"She even convinced you to join the fencing club, and you’ve made even more friends there. It seems like things are going right in life."

show fhappy
m "H-Hey, %(f)s, there’s something I want to tell you..."

f "Hmm? What is it? Is it about the lab?"

m "Umm...well..."

"No matter what, you just couldn’t tell her how you felt."

m "Yeah, it is actually about the lab..."

"You begin to notice some things about %(f)s that you hadn’t before; how caring she can be, how she always makes sure all her food is completely separated, how she always makes you laugh even just by laughing herself."

"There are some days however where you’re not sure that she feels the same way about you. Sometimes she’ll give you the cold shoulder and won’t text you back."

"When you ask her if she’s mad at you, she just sighs and replies that nothing’s wrong. After that, things tend to go back to normal for a while until it happens again. You can never tell what’s bothering her though, until one day..."

scene bg labroom
show fangry
"The two of you are in the lab room working on your latest assignment. %(f)s hasn’t asked for any help in a while, and it’s been pretty quiet between you."

"You notice that she hasn’t been doing much work, just holding a beaker full of some strange liquid."

m "Hey, we should probably start to mix the chemicals if we want to finish."

f "Fine, I’ll mix them."

"She proceeds to dump the entire beaker into a bowl full of some white powder, and it immediately begins to smoke."

m "Hey! What are you doing?! Be careful with those! We could get in a lot of trouble for mixing things randomly. You have to think before you do something like that, OK?"

f "Oh really? I have to think first? Well, maybe you’re the one who needs to think before he does things! Or do you just not care about anybody else at all?"

"She suddenly packs up all her things and leaves the classroom before you can even say anything."

m "H-Hey, wait!"

"You get up and chase after her, heading outside and running to catch up."

scene bg tree
show fangry
m "What are you thinking??"

f "What am I thinking? I’m thinking you’re a jerk!"

m "That’s not what I meant! What was up with you back there? You’ve been so hostile lately, and I have no idea why."

f "You have no idea? You’re the problem! I can’t handle your constant mood swings!"

m "What are you talking about?"

f "It’s as if each time I see you you’re a different person! And you act so clueless, like you’re trying to make me feel dumb!"

m "{i}Well, that’s because I am clueless...{/i}"

menu:
    "I think you act strangely each time I see you, too.":
        show fshocked
    "I really don’t understand. Are you sure you’re alright?":
        show fshocked
    "Maybe you’re mistaking someone else for me?":
        show fshocked

f "What?"
show f angry "No, this isn’t about me! Ugh, I can’t believe you sometimes!"

"She storms off in a fit of rage. You’re left to ponder exactly what just happened."

m "{i}Could it have really been something that I did? But everything had seemed to be going so well.{/i}"
m "{i}And I was even going to ask her out if we got a good grade on our assignment!{/i}"
m "{i}Have I really been acting differently though?{/i}"
m "GAHHH! I don’t understand women at all!"

#replace "... " with "...", replace "..." with "...", replace """ with """, replace """ with """, replace %(m)s with %(m)s; same for fem.; replace m with m, etc. for characters
#same name option, scene titles, scene transitions, change vpunch to custom transition, no chem pun intended, renpy dialogue halves for this isn't about me

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

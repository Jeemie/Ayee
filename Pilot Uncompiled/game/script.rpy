# You can place the script of your game in this file.
# Declare characters used by this game.

# The game starts here.
label start:
scene black with dissolve
show text "Day One \n Chemistry Class" at basicfade with Pause(2.5)
scene black with dissolve

scene olin with dissolve

male "{i}It's the first day of classes. I remember facing this day so many times in high school.{/i}"

male "{i}Back then, I wasn't so prepared. Everything seemed so intimidating, and everyone had their own friends.{/i}"

male "{i}So I ended up just keeping to myself. And it wasn't so bad! I was fine on my own, and I had some friends at school.{/i}"

male "{i}But I feel like I missed out on something – an entire world I don't know about. So college is going to be different!!!{/i}"

male "{i}...Or, at least that was the plan. I've been here a week and I don't even know one person's name.{/i}"

male "{i}I thought Worcester Polytechnic Institute would be the perfect school. I mean, WPI's great, but I have no skills when it comes to talking with people.{/i}"

male "{i}I'm determined to change that though! Starting now, I'll make a ton of friends! I'll go out and have fun and make the most of my time!{/i}"

p "Hello? I was asking you your first name."

"The teacher is staring at you with a piece of paper in her hand. It seems to be a checklist of people's names in the chemistry class."

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

m "{i}I almost couldn't remember my own name. Class hasn't even started yet and I'm screwing everything up.{/i}"

m "{i}Things can only get better now, though!{/i}"

p "Alright, we're going to get straight down to business. For this marking period your grades will be divided into three different portions: homework, projects, and the final exam."

p "The exam is self-explanatory, and for the homework, you will be required to read from your textbooks each week, as well as finishing assignments that will be posted online."

p "Finally, for the entirety of the course you will be assigned a single partner who you will share work with on projects and lab days."

p "You are each required to turn in the assignments separately, but you may have the exact same papers."

m "{i}By this point I wasn't even listening anymore. My mind was racing at what the professor insinuated.{/i}"

m "{i}We're gonna have partners who are forced to be with us! This might just be my chance to make a friend here. It might even be a girl too...{/i}"

m "{i}Oh crap, what am I supposed to do if it is a girl? Is it just like with guys? What if she's also shy? That would be pretty bad...{/i}"

m "{i}But if she's too enthusiastic then she could be annoying!{/i}"

m "{i}Ahhh, what am I saying?! I don't even know if it will be a girl! I should stop worrying.{/i}"

p "Alright, now I'll give you the rest of the time in class to find your partners and discuss your schedules."

m "{i}Crap! Did she announce everyone's partner? I didn't even hear it! I was way too distracted.{/i}"

m "{i}How am I supposed to find my partner then? And I still don't even know who it is. Maybe they'll find me...{/i}"

"There's a slight tap on your back, and your heart involuntarily jumps in your chest. You're so on edge today that you could have a heart attack at any time."
play sound "sfx/punch.mp3"
pause 0.1
with vpunch

"You take a deep breath to quickly calm yourself and turn around to find..."

show fhappy at basicfade, center
female "Hey there! It's nice to meet you! If I heard right, your name is %(m)s, right? Did you remember my name?"

"It's a cute girl!"

"Your heart is beating out of your chest as you throw out the first name that comes to mind."

m "O-oh, yeah, I d-did! Uhh, yeah, my name's %(m)s, and you're...uhh...you're ...?"

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

f "Yeah, that's it! I was just making sure you were paying attention. It's nice to meet you! I'm sure we're gonna be great partners. We should get going before the next class comes in, though."

menu:
    "As long as you don't slow me down.":
        hide fsassy
        show fangry
        f "Well fine, if you don't want to work with me, I'll go get a different partner."
        "She immediately goes over to the professor and although you can't hear everything, it doesn't sound good for you." 
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
        f "Well fine, if you don't want to work with me, I'll go get a different partner."
        "She immediately goes over to the professor and although you can't hear everything, it doesn't sound good for you." 
        "Afterward, the professor comes over and tells you that the two of you would be working with different partners."
        scene black with dissolve
        show text "Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
    "I-It's nice to meet you!":
        hide fsassy at basicfade
        show fhappy at basicfade, left
        f "We should get going before the next class comes in though!"

"You notice that you're the last two left in the classroom and students for the next class are about to come in."

f "So, we should plan a time to get together and plan everything out."

m "Well, I'm free right now, if you're not busy."

f "I actually have a class right now, but how about we meet at the giant tree tomorrow at 5:00?"

m "O-Ok, that works for me! I'll see you then."

f "Yeah, bye for now."

"You completely forget that you were going to go to the robotics club meeting at 5:00, but you decide that that's not important anymore."

scene bg dorm

"It's almost 5:00 pm and you're sitting in your room waiting to head out to meet %(f)s. It's a good thing your roommates are out or they might get annoyed with all the pacing you're doing."

m "{i}It's nothing to be worried about. I'm supposed to be there, and I'll talk about...things. And if not, there's always chemistry work to fall back on.{/i}"

m "{i}But I can't help thinking how cute she was.{/i}"

m "{i}But I might scare her away.{/i}"

m "{i}But I'm gonna be late if I don't leave.{/i}"

m "{i}Alright, I'm heading out then!{/i}"

scene bg tree
m "{i}There she is! Wow, I don't think I got a very good look at her yesterday, but she looks...{/i}"

show fangry

f "There you are!! You're late! I'll have you know my time is very precious!"

m "Sorry! I'm sorry!"

m "{i}Mad. She looks pretty mad. I'm not that late am I?{/i}"

f "I knew you weren't gonna make it in time, didn't you hear me before?"

m "{i}In class? She didn't say anything about me being late.{/i}"

m "A-Ah no, I guess I must have missed it. I'm really sorry I'm late, but I'm here now, so we should...get things going, I guess?"

show fhappy
f "Yeah, you're right. Well, we've already introduced ourselves yesterday, so let's get down to business! I'm free on Wednesdays from 6-8 and then I'm also available at 1, but I have a class at 3 so we might be pressed for time then."

m "Wednesday at 6 works for me!"

f "Alright then! I guess we could bring dinner with us, or if you're free before that then we can go get some together."

"You can't stop your heart from pounding when you hear that. Going to get dinner together? Just the two of you? It's almost like a date!"

f "I guess that's everything we really need to cover. I guess we could have just e-mailed each other, but this was good anyway."

m "Do you want to go get something to eat right now?"

m "{i}What did I just say?{/i}"

f "Well, I have to get back to my homework later, but, sure! I haven't eaten yet."

"You let out the breath you hadn't even known you were holding and smiled. Your legs were shaking a bit, but you were too happy to stop them, and you were certain she wouldn't notice."

m "Great! I th-think they might have Chinese food in the dining h-hall today!"

"You prayed that you would be able to stop stuttering soon as the two of you headed toward the dining hall."

scene bg dininghall
show fshocked
f "No way!! You were a championship fencer??"

m "Well, it's not that I was that good or anything, but my sophomore year of high school I made it to the semi-finals of this national tournament. At the time I was ranked 4th in the US for my age."

show fhappy
f "That's so incredible! You must have been awesome at it. So does that mean you're gonna join the fencing team here?"

m "Well, no, I didn't plan to..."

f "Why not? It sounds like you'd do really well in it."

m "I guess...but I haven't actually fenced since I was 15."

f "But you said you had made it to the national championship – why stop after that?"

m "{i}Is this something I should be sharing with a girl I just met? But there's something that makes me just...trust her.{/i}"

m "After the championship I quit fencing to focus on getting into college. My parents had supported me completely while I was fencing, but I knew that they were having trouble keeping up with everything."

m "With work, and taking me to fencing classes, and then to another state for the championships, I didn't want to burden them any more."

f "Wow, that's really nice of you! But now that your parents don't have to worry about you, you could always start up again, right?"

m "I...I never thought of that. You're right, I could."

m "But - I don't know – it's been a long time since I've fenced."

f "Oh, I'm sure it's just like riding a bicycle! You'd definitely get back into it!"

m "{i}Maybe I could,but I don't want to think about that now, all of my focus should be on %(f)s.{/i}"

m "So what about you? I told you what I like to do, so what interests you?"

f "Well, I'm actually really big into art. When I was younger, I always loved art classes and drawing and painting."

f "What I really love though, is creating things – taking empty space and filling it with something grand and beautiful! I {b}love{/b} sculpting and designing – making something that I can love and that others can see!"

f "So that's why I came here – to become a civil engineer. One day, I'm gonna build something big and beautiful in a city or a town, or even something just for me."

m "{i}Wow, that's a big dream. It's kind of strange to know someone who already has their life planned out. Something inside me knows that she'll be able to do it, too.{/i}"

m "That sounds incredible. I've never thought that way about making things: everyone can see it, but you can still call it yours. Actually, that sounds kind of scary. I mean, what if nobody likes it?"

f "Well then, that's their problem! Besides, what makes you so sure everybody's going to hate what I make?!"

m "A-Ah, n-no! I didn't mean it like that! I think w-whatever you'd make would be incredible!"

"Your face is nearly red now as you try to reconcile her, but you completely stop when you see her wide grin."

show flaughing
f "Hahahaha! I'm just kidding, %(m)s. I knew what you meant! It {b}is{/b} fun to tease you, though. You turned pretty red there, too!"

m "{i}I got played! But I don't really mind. It feels nice talking to her like this.{/i}"

"A bit later, you both check the time and find that you've been in the dining hall talking for 2 hours. You both get up in a hurry and exchange phone numbers before heading out. This is the first night at college that you've fallen asleep feeling truly content."

scene bg black
"Today is now Tuesday and you have your chemistry class again. The thought of seeing %(f)s again makes you get to class a bit earlier than you normally would."

scene bg classroom
"When you get there, you notice that she hasn't arrived yet, and there's hardly anyone else there. Since you have no idea where she was sitting the other day, finding a seat next to her would be nearly impossible."

"You decide to go back to the seat you were originally sitting in and wait for class to start. Last night you had trouble sleeping, and you're paying for it now. You feel so tired that your eyes keep closing against your will."

"???" "Somebody must have had a rough night."
with vpunch

"You jump in your seat, startled at the sudden voice. Looking around, there are many more people in the room now, and sitting next to you is %(f)s."

show fhappy
f "Hi there, %(m)s. I'm glad I could scare you awake! It's pretty funny to make you jump. Did you not sleep last night?"

m "H-Hey, %(f)s! Uh, no, I didn't sleep very well for some reason...I think it has to do with the heat here."

f "You're right. You'd think in Massachusetts it would be a bit colder at the beginning of fall. It doesn't really bother me though!"

m "Yeah, you seem perfectly fine in the heat. Was it very hot where you came from?"

f "I lived in North Carolina most of my life, so it was pretty hot for most of the year. My grandparents live in Massachusetts though, so I've been up here many times, especially in the winter when it's full of snow."

"As you're about to respond, the professor walks into the room and calls for everybody's attention. The class goes by quickly, but you feel like you would've fallen asleep if you hadn't had %(f)s sitting next to you."

"After class, you both say goodbye and remind each other about your meeting the next day. The rest of the day seems a bit brighter now than it had before your chemistry class."

scene bg labroom
show fangry
f "Ahh! I can't understand this at all! Why do we need to figure out how they're going to react? Why don't we just combine them all and see what happens? Isn't that what experimentation is?"

menu:
    "Go for it!":
        "She pours every chemical within reach into a single beaker, an excited smile on her face. You can't help but admire her adventurous attitude and look on in wonder as her experiment bubbles."
        show fhappy
        f "Look! It's doing something! I told you, experiments should –"
        show bg explosion
        "There isn't any time to react as the solution bubbles to a climax and explodes in her face. You can't feel anything as you're caught in the blast."
        scene black with dissolve
        show text "Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
    "Maybe we should try something else...":
        m "I guess so, but I'm sure they don't want us to cause an explosion. Besides, it's not so hard. We just have to look up the chemical compounds they'll form."

f "I'm just not good at chemistry. I took it in high school, so I thought it would be easy now, but I still don't get it! I'm doomed!"

m "Don't worry. Since we're partners, I'll be here to help, and I'll make sure you don't fail! I'll teach you everything you need to know."

f "You would? Ohh, thank you so much, %(m)s! That's so nice of you!"

"You then notice that her arms are around you, and you're pulled into a hug. She nearly squeezes some of the life out of you, but you enjoy it nonetheless. Your cheeks momentarily turn red in the process, but you don't think she noticed."

"The rest of your lab time is spent performing various infusions of chemicals as you explain their properties to your partner. You feel a warm connection between the two of you, and you hope that you're not the only one who feels it."

scene bg black
show fhappy
f "So hey...There's this concert in Boston this week that I'd love to see, but most of my friends are going home over the weekend."

m "Dang, that really sucks. Is there anybody else you can ask?"

f "Well...do you want to go?"

m "Hmm..."

m "O-Oh! Y-Yeah! I'd love to – I mean, that sounds pretty awesome. Of course I'll go!"

"The two of you began spending more time together."

"Over the next three weeks, the two of you continue your routine lab work and usually find time to eat dinner together during the week."

"She even convinced you to join the fencing club, and you've made even more friends there. It seems like things are going right in life."

show fhappy
m "H-Hey, %(f)s, there's something I want to tell you..."

f "Hmm? What is it? Is it about the lab?"

m "Umm...well..."

"No matter what, you just couldn't tell her how you felt."

m "Yeah, it is actually about the lab..."

"You begin to notice some things about %(f)s that you hadn't before; how caring she can be, how she always makes sure all her food is completely separated, how she always makes you laugh even just by laughing herself."

"There are some days however where you're not sure that she feels the same way about you. Sometimes she'll give you the cold shoulder and won't text you back."

"When you ask her if she's mad at you, she just sighs and replies that nothing's wrong. After that, things tend to go back to normal for a while until it happens again. You can never tell what's bothering her though, until one day..."

scene bg labroom
show fangry
"The two of you are in the lab room working on your latest assignment. %(f)s hasn't asked for any help in a while, and it's been pretty quiet between you."

"You notice that she hasn't been doing much work, just holding a beaker full of some strange liquid."

m "Hey, we should probably start to mix the chemicals if we want to finish."

f "Fine, I'll mix them."

"She proceeds to dump the entire beaker into a bowl full of some white powder, and it immediately begins to smoke."

m "Hey! What are you doing?! Be careful with those! We could get in a lot of trouble for mixing things randomly. You have to think before you do something like that, OK?"

f "Oh really? I have to think first? Well, maybe you're the one who needs to think before he does things! Or do you just not care about anybody else at all?"

"She suddenly packs up all her things and leaves the classroom before you can even say anything."

m "H-Hey, wait!"

"You get up and chase after her, heading outside and running to catch up."

scene bg tree
show fangry
m "What are you thinking??"

f "What am I thinking? I'm thinking you're a jerk!"

m "That's not what I meant! What was up with you back there? You've been so hostile lately, and I have no idea why."

f "You have no idea? You're the problem! I can't handle your constant mood swings!"

m "What are you talking about?"

f "It's as if each time I see you you're a different person! And you act so clueless, like you're trying to make me feel dumb!"

m "{i}Well, that's because I am clueless...{/i}"

menu:
    "I think you act strangely each time I see you, too.":
        show fshocked
    "I really don't understand. Are you sure you're alright?":
        show fshocked
    "Maybe you're mistaking someone else for me?":
        show fshocked

f "What?"
show f angry
f "What? No, this isn't about me! Ugh, I can't believe you sometimes!"

"She storms off in a fit of rage. You're left to ponder exactly what just happened."

m "{i}Could it have really been something that I did? But everything had seemed to be going so well.{/i}"
m "{i}And I was even going to ask her out if we got a good grade on our assignment!{/i}"
m "{i}Have I really been acting differently though?{/i}"
m "GAHHH! I don't understand women at all!"

scene bg classroom

f "{i}College is so much different.{/i}"

f "{i}In high school my friends and I would all make sure we got seats together. Although it's not like that made a difference, they weren't really my friends.{/i}"

f "{i}Everyone here is so much more real too. There's no sense in hiding yourself because there's nothing to be ashamed of! I can actually feel comfortable with myself and not have to watch everything I do.{/i}"

f "{i}I've already met so many different people! The girls in my dorm, the guys upstairs who bother us, sporty girls, bros, nerds, stoners- there's a bit of everything!{/i}"

f "{i}The one thing everyone definitely has in common is they're all so smart! I really hope I can keep up...{/i}"

f "{i}It's probably a good idea that I start to plan my schedule ahead right now! Let's see, next week I want to go see the art club and I'll have to meet with my academic advisor to talk about my schedule.{/i}"

f "{i}I'll probably need to go to some help sessions for these classes. They seem hard already – and we haven't even started! I also promised I'd meet Katie for lunches.{/i}"

p "Hello? I was asking you your first name."

"The teacher is staring at you with a piece of paper in her hand. It seems to be a checklist of people's names in the chemistry class."

f "Oh! I'm so sorry, I wasn't paying attention at all. Of course, my name is %(f)s."

p "Alright then, %(f)s it is."

"She checks your name off her list and moves onto the next person."

f "{i}I really shouldn't be spacing out like that. Did I not get enough sleep last night?{/i}"

f "{i}But it's the first day of classes! I shouldn't be tired on the first day.{/i}"

f "{i}I'll have to make sure I get enough sleep. That really wasn't a good first impression.{/i}"

p "Alright, we're going to get straight down to business. For this marking period your grades will be divided into three different portions: homework, projects, and the final exam."

p "The exam is self-explanatory, and for the homework, you will be required to read from your textbooks each week, as well as finish assignments that will be posted online."

p "Finally, for the entirety of the course, you will be assigned a single partner, whom you will share work with on projects and lab days."

p "You are each required to turn in the assignments separately, but you may have the exact same papers."

p "Now, I'm going to leave the paper here on the blackboard. You may find your name and your partners and meet with them to discuss for the rest of the class. Make sure you decide on a time to meet during the week to finish the lab assignments."

"You walk up to the desk at the front of the room to see who exactly your partner is."

"You look up your own name. Listed right next to your name is your partner's."

f "Hmm? How exactly do you pronounce this? Well, the name must be %(m)s."

"You take a look around the classroom and notice that most everyone has already paired up with their partners. There is only one guy left sitting in his desk, seemingly not paying attention to anything."

show mdistant
f "Hmm...How to approach this..."

menu:
    "Sneak up and surprise him!":
        "You decide to take a tactical approach and go around, walking up slowly so his back is facing you."
        "You tap him on the shoulder gently. He jumps nearly out of his seat."
    "Walk up and say hi.":
        "You decide to go straight up to him and say hi."
        "As you approach, you see him snap out of his daze and look up to you."
    "Wait for him to come to you.":
        "You stand at the front of the room for a while, glancing at him every once in a while to see if he'll come and say hello, but he only remains in his seat until the end of class. Then he gets up and leaves."
        "You also decide to head out, but you never end up getting in contact with your partner."
        scene black with dissolve
        show text "Bummer \n Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
f "Hi there! If I'm correct, then you must be %(m)s. My name's %(f)s and we're gonna be partners!"

show mshocked
m "O-Oh! H-Hey there! Sorry, I wasn't paying too much attention before."

f "Well, I hope you don't do that when we're working, too – 'cause I know nothing about chemistry, so it'd be bad if neither of us did the work."

m "I-I'm sure that's not true. W-We'll both do the work, and it won't be so bad. I'm sure of it."

m "We should get going before the next class comes in, though."

"You notice that you're the last two left in the classroom, and students for the next class are about to come in."

f "So, we should plan a time to get together and plan everything out."

m "Well, I'm free right now, if you're not busy."

f "I actually have a class right now, but how about we meet at the giant tree at 5:00?"

m "O-OK, that works for me! I'll see you then."

f "Yeah, bye for now!"

"He seemed a bit strange, as if he were really nervous, but you have no idea why. You guess it must just be because it's the first day of classes."

"Hopefully he isn't hard to deal with..."

show bg quad
"You've finished the rest of your classes for the day. You're walking through the Quad to meet your partner at the large tree on campus."

"You get halfway across the quad when you notice someone walking in the opposite direction."

show nhappy
f "Hey %(m)s, where are you going? You're gonna be late! Don't forget that we're meeting at the tree in 5 minutes!"

show nshocked
"He stops as he's walking by and turns to you for a moment. You keep moving past him and give him a smile. He probably just has to stop at his room first or something."

scene bg tree
"It's now 5:05 and you're standing at the tree waiting for %(m)s to arrive. You expected he was going to be late based on how surprised he seemed when you passed him."

"You got the feeling he was the kind of guy who wouldn't do that on purpose. Still, it couldn't hurt to tease him a little when he did show up. Speaking of which..."

f "There you are!! You're late! I'll have you know my time is very precious!"

show msurprised
m "Sorry! I'm sorry!"

f "I knew you weren't gonna make it in time. Didn't you hear me before?"

show mshocked
m "A-Ah no, I guess I must have missed it. I'm really sorry I'm late. But I'm here now, so we should...get things going, I guess?"

f "{i}Haha he can be kinda cute when he's flustered. There's no sense in staying mad at him though.{/i}"

show mhappy
f "Yeah, you're right. Well, we've already introduced ourselves yesterday, so let's get down to business! I'm free on Wednesdays from 6-8 and then I'm also available at 1, but I have a class at 3, so we might be pressed for time then."

m "Wednesday at 6 works for me!"

f "Alright then! I guess we could bring dinner with us. Or if you're free before that, then we can go get some together."

"You see him straighten up a little more after you say that. It's pretty funny seeing him respond to you, as if he doesn't usually talk to girls."

f "I guess that's everything we really need to cover. I guess we could have just emailed each other, but this was good anyway."

m "Do you want to go get something to eat right now?"

f "Well, I have to get back to my homework later, but sure! I haven't eaten yet."

f "{i}Wait...{/i}"

f "{i}Wait...this doesn't count as my first date, right?{/i}"

f "{i}No, of course not!{/i}"

m "Great! I t-think they might have Chinese food in the dining h-hall today."

scene bg dininghall
show mhappy
f "No way! You were a championship fencer?"

m "Well, it's not that I was that good or anything...but my sophomore year of high school, I made it to the semi-finals of this national tournament. At the time I was ranked 4th in the US for my age."

f "{i}I wouldn't have taken him to be a fencer! He looks more like a tennis guy if you ask me.{/i}"

f "That's so incredible! You must have been awesome at it. So does that mean you're gonna join the fencing team here?"

show msad
m "Well, no, I didn't plan to..."

f "Why not? It sounds like you'd do really well in it."

m "I guess, but I haven't actually fenced since I was 15."

f "But you said you had made it to the national championship. Why stop after that?"

m "After the championship, I quit fencing to focus on getting into college. My parents had supported me completely while I was fencing, but I knew that they were having trouble keeping up with everything."

m "With work, and taking me to fencing classes, and then to another state for the championships, I didn't want to burden them anymore."

f "Wow, that's really nice of you! But now that your parents don't have to worry about you, you could always start up again, right?"

m "I-I never thought of that. You're right, I could."

m "But – I don't know – it's been a long time since I've fenced."

f "Oh, I'm sure it's just like riding a bicycle! You'd definitely get back into it!"

f "{i}I'm not actually so sure that's how it works, but encouraging him couldn't hurt.{/i}"

m "So what about you? I told you what I like to do, so what interests you?"

f "Well, I'm actually really big into art. When I was younger, I always loved art classes and drawing and painting."

f "What I really love, though, is creating things – taking empty space and filling it with something grand and beautiful! I {b}love{/b} sculpting and designing – making something that I can love and that others can see!"

f "So that's why I came here – to become a civil engineer. One day, I'm gonna build something big and beautiful in a city or a town, or even something just for me."

m "That sounds incredible. I've never thought that way about making things: so everyone can see it, but you can call it yours. Actually, that sounds kind of scary. What if nobody likes it?"

f "Well then, that's their problem! Besides, what makes you so sure everybody's going to hate what I make?!"

show mshocked
m "A-Ah, n-no! I didn't mean it like that! I think w-whatever you'd make would be incredible!"

"You could see that his face was turning red and that he was getting completely flustered."

f "Hahahaha! I'm just kidding, %(m)s. I knew what you meant! It is fun to tease you though. You turned pretty red there too!"

f "{i}It's fun talking with %(m)s. I don't want to seem too mean though. I'm not sure he could handle it.{/i}"

show mhappy
"A bit later, you both check the time and find that you've been in the dining hall talking for 2 hours. You both get up in a hurry and exchange phone numbers before heading out. You fall asleep tonight thinking of how different people are in college than in high school – and it's a good different."

scene bg black

f "{i}Oh no! I don't want to be late on the second day of school! That'll give the wrong impression for sure!{/i}"

"You were up pretty late last night doing homework after your dinner with %(m)s and ended up missing your alarm. You had to rush around your room getting ready while your roommates stood by laughing, and now you're making a mad dash for your chemistry class."

f "{i}Wait, isn't that –{/i}"

f "{i}But he shouldn't be here...{/i}"

scene bg quad
"You see %(m)s walking into another building."

f "{i}He {b}should{/b} be heading to chemistry.{/i}"

"You have no time to stop, though, as you press onward to class."

scene bg classroom
"You break into your classroom with a minute to spare and find that everyone else has made it before you."

"Not wanting to draw any attention to yourself, you decide to take a seat quickly. You catch the head of a certain brown-haired guy near the front row and move down to take a seat next to him."

"As you approach, you see that his head is nearly face down on the desk. It seems like he got even less sleep than you."

f "Somebody must have had a rough night."

show mshocked
f "Hi there, %(m)s. I'm glad I could scare you awake! It's pretty funny to make you jump. Did you not sleep last night?"

m "H-Hey, %(f)s! Uh, no, I didn't sleep very well for some reason. I think it has to do with the heat here."

f "You're right. You'd think in Massachusetts it would be a bit colder at the beginning of fall. It doesn't really bother me though!"

show mhappy
m "Yeah, you seem perfectly fine in the heat. Was it very hot where you came from?"

f "I lived in North Carolina most of my life, so it was pretty hot for most of the year. My grandparents live in Massachusetts though, so I've been up here many times, especially in the winter, when it's full of snow."

"As he's about to respond, the professor walks into the room and calls for everybody's attention. The class goes by quickly. You're surprised %(m)s hasn't fallen asleep at all."

"After class, you both say goodbye and remind each other about your lab the next day. The rest of your classes seem to go by a bit faster afterward for some reason."

scene bg quad
"It's later in the day now, and you're heading back to your dorm after having dinner with some of the friends from your dorm. So far, it seems like a bright, happy day for some reason, even though you have the most classes on Tuesdays."

"You notice someone sitting on a bench, alone, next to the path you're walking on. As you get closer, you recognize %(m)s sitting and looking serious."

show nsad
f "Hey, %(m)s, what's up? Why are you sitting out here all alone?"

show nangry
m "I don't want to talk to you. Why don't you get out of here?"

f "W-What? What's wrong??"

m "It's nothing."

hide nangry
"%(m)s walks off towards one of the dorm buildings and you're left wondering just what had happened to him. Maybe it was something serious."

"It seemed like he didn't want you to pry into it, though, so you decide to leave it alone. If he wanted to tell you, he would."

"It disappoints you a bit that he didn't, but you don't know why."

scene bg lab
show mhappy
f "Ahh! I can't understand this at all! Why do we need to figure out how they're going to react? Why don't we just combine them all and see what happens? Isn't that what experimentation is?"

menu:
    "Go for it!":
        "You pour every chemical within reach into a single beaker, an excited smile on your face. You can't help but admire your handywork as your experiment starts to bubble."
        show mshocked
        f "Look! It's doing something! I told you, {b}that's{/b} how experiments should be!"
        m "Wait, what did you put –"
        show bg explosion
        "There isn't any time to react as the solution bubbles to a climax and explodes in your face. You can't feel anything as you're caught in the blast."
        scene black with dissolve
        show text "Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
    "Maybe ask for some help...":
        m "Well, I'm sure they don't want us to cause an explosion. Besides, it's not so hard. We just have to look up the chemical compounds they'll form."

f "I'm just not good at chemistry. I took it in high school, so I thought it would be easy now, but I still don't get it! I'm doomed!"

m "Don't worry. Since we're partners, I'll be here to help, and I'll make sure you don't fail! I'll teach you everything you need to know."

f "You would? Ohh, thank you so much, %(m)s! That's so nice of you!"

"You then go over and give him a hug in thanks. You don't notice, but you accidentally squeeze him just a little too hard, nearly cracking a couple bones, but it seems he enjoys it nonetheless. You almost think you saw his cheeks turn a little red..."

"The rest of your lab time is spent performing various infusions of chemicals as %(m)s explains their properties to you. You feel a warm connection between the two of you, and you think it might not just be you."

scene bg quad
"About a week after your first lab, it seems that you and %(m)s have become really good friends. The two of you have clicked on almost everything, and he's not like the other guys you knew from high school."

"It was the second Tuesday that you'd been at WPI, and you were out hanging at the giant tree with some friends. When you looked across campus, you noticed something."

"It was %(m)s, but he was walking with a girl you'd never seen before. In fact, she looked like an older girl – probably at least a junior – and they were chatting very animatedly."

"You feel a slight pain in your chest, but you don't know why. There's no reason to be jealous or anything over this."

"Your eyes make contact with his, and it seems like he notices you. In fact, he starts walking toward you."

show mhappy
m "Hey, %(f)s, what's up?"

f "Oh, h-hey, %(m)s. Nothing really. Who's that you're with?"

m "Oh, that's just this girl whom I'm helping with calculus. You know, she really needed help, so I offered to tutor her privately."

f "That's...so nice of you. I'm glad you could do that. I've got to go now, though."

hide mhappy
"You turn around and start running in the opposite direction. You don't even care that he's still watching you run off, confused."

"{i}Why would you think that you're special for having him teach you chemistry? He obviously helps out all the girls he can.{/i}"

"{i}You can't get mad over this though. It wouldn't be good to have this ruin your chemistry partnership over a misunderstanding on your part. Why did you think he would be into you anyway?{/i}"

"{i}College is different.{/i}"

scene bg lab
show mhappy
"It's Tuesday once again after three weeks of college. You and %(m)s are back in the chemistry lab. Neither of you is doing much work, though."

m "Hey, we should probably start to mix the chemicals if we want to finish."

f "Fine, I'll mix them."

"You proceed to dump the entire beaker into a bowl full of some white powder. It immediately begins to smoke."

show msurprised
m "Hey! What are you doing?? Be careful with those, we could get in a lot of trouble for mixing things randomly. You have to think before you do something like that, OK?"

f "Oh really? I have to think first? Well maybe you're the one who needs to think before he does things! Or do you just not care about anybody else at all?"

"You suddenly pack up all your things and leave the classroom before he can even say anything."

m "H-Hey, wait!"

"You're already out the door and on your way to the quad before he can get up to chase after you."

scene bg tree
show mangry
m "What are you thinking??"

f "What am I thinking? I'm thinking you're a jerk!"

m "That's not what I meant! What was up with you back there? You've been so hostile lately and I have no idea why."

f "You have no idea?? You're the problem! I can't handle your constant mood swings!"

m "What are you talking about?"

f "It's as if each time I see you you're a different person! And you act so clueless like you're trying to make me feel dumb!"

m "Well, it's seems like you're the one who's different every time I see you."

f "What?"
f "What? No, this isn't about me! Ugh, I can't believe you sometimes!"

"You storm off in a fit of rage and he doesn't dare to follow you again. You feel as though you're not in control of your body. Your mind tells you he did nothing wrong."

"But your heart tells your mind that it's dead wrong."

"Unfortunately, you're caught between the two as they rage a war inside."

#PART 3: Epilogue
#Unlocked only after completing the Male and Female paths, regardless of order.

"I'm not a guy who's very experienced with love."

"Well, even if I were, I'm not sure how anybody is supposed to deal with being hit by it."

"The first thing to be said is that movies just don't do it justice. A picture's worth a thousand words, a moving picture worth even more, but love can't even be described in words alone."

"The one thing they've gotten right is that love can make you do some crazy things..."

scene bg quad
show fhappy
f "Hey, %(m)s, where are you going? You're gonna be late! Don't forget that we're meeting at the tree in 5 minutes!"

"And that was the first time I saw her. I guess the movies also got the whole \"love at first sight\" thing too."

scene bg quad
show fhappy
"The second time I saw her was only a day afterward, and it was even less of an encounter. I merely saw her on my way to classes."

"At least she didn't call me by the wrong name this time."

scene bg black
"I barely knew anything about her, but the few times I saw her afterward, she was with this other guy and..."

"I barely knew anything about her, but the few times I saw her afterward, she was with this other guy and...well..."

"I barely knew anything about her, but the few times I saw her afterward, she was with this other guy and...well...he looked exactly like me."

show mhappy
"I found out his name is %(m)s, and they're in the same chemistry class. Apparently they're lab partners."

"It's ironic right? Almost as though two different versions of me were in love with the same girl."

"You wouldn't see that in the movies, right?"

"Oh, and my name's Nick."

"That might explain a bit."

scene bg tree
show fsad
n "Hey, %(f)s, what's up?"

f "Oh, h-hey %(m)s, nothing really. Who's that you're with?"

n "Oh, that's just this girl whom I'm helping with calculus. You know, she really needed help, so I offered to tutor her privately."

f "That's...so nice of you. I'm glad you could do that. I've got to go now, though."

hide fsad
n "I hadn't thought of myself as crazy at the time. I was just mad."

n "Madly in love, that is. Get it?"

n "I thought that if I was gonna get the girl, I had to make sure that she wasn't already taken. Even if she was taken by another me."

show bg black
n "Looking back, maybe I should have questioned why we looked the same anyway..."

n "But that doesn't matter anymore. The only thing that matters is the final choice I have to make."

menu:
    "It was a mistake. They deserve to be together.":
        n "I can't do this – I have to fix it. It wouldn't be right to force them apart."
        "You first go see %(f)s, who is furious at you, until you explain who you are. Afterward, she is only shocked as you take her to see %(m)s."
        "When you both meet, you are stunned at the similarities you share. The resemblance is uncanny, but you quickly explain your side of the story before everything can even be processed. Before anybody knows it, you're gone."
        "You leave them to work it out and mend what was previously broken."
        "A deep sadness fills your heart afterward. Even over a trivial spark like the one you had for her."
        "But there exists no love without sadness."
        "THE END"
        return
    "Maybe I deserve love, and maybe she deserves me.":
        n "Now's my chance. I've waited quite a while for this, and I can't let the chance pass me up!"
        "You decide to wait a day, and you make sure you're wearing distinct clothing."
        "In fact, you end up changing a lot of things about yourself."
        "You decide to get a new haircut."
        "You start wearing lots of hats."
        "You even get glasses to wear."
        "You've changed a lot about yourself, but %(f)s tells you she likes the way it all looks."
        "Maybe she wouldn't have if she knew you changed them."
        "But there exists no love without sacrifice."
        "THE END"
        return
    "This has to be where it ends – neither of us will get her.":
        n "It's better off this way. If I keep another person away from love, then what right do I have to it?"
        "You end up not doing anything about the situation you caused."
        "A couple weeks later, you end up meeting %(m)s in person. The resemblance between the two of you is uncanny, and you eventually figure out that you may be cousins whose families became distant."
        "The two of you end up becoming friends – and even roommates – the next year of college."
        "Maybe you wouldn't have if he'd known what you'd done."
        "But there exists a new bond between two unlikely, but ultimately connected, individuals."
        "For what exists when there is no love?"
        return
    "Where did this all go wrong?":
        n "I can't even begin to think of how I became like this, but I know how I feel about her. To me that justifies everything. Who else will see it that way, though?"
        menu:
            "It was a mistake. They deserve to be together.":
                n "I can't do this – I have to fix it. It wouldn't be right to force them apart."
                "You first go see %(f)s, who is furious at you, until you explain who you are. Afterward, she is only shocked as you take her to see %(m)s."
                "When you both meet, you are stunned at the similarities you share. The resemblance is uncanny, but you quickly explain your side of the story before everything can even be processed. Before anybody knows it, you're gone."
                "You leave them to work it out and mend what was previously broken."
                "A deep sadness fills your heart afterward. Even over a trivial spark like the one you had for her."
                "But there exists no love without sadness."
                "THE END"
                return
            "Maybe I deserve love, and maybe she deserves me.":
                n "Now's my chance. I've waited quite a while for this, and I can't let the chance pass me up!"
                "You decide to wait a day, and you make sure you're wearing distinct clothing."
                "In fact, you end up changing a lot of things about yourself."
                "You decide to get a new haircut."
                "You start wearing lots of hats."
                "You even get glasses to wear."
                "You've changed a lot about yourself, but %(f)s tells you she likes the way it all looks."
                "Maybe she wouldn't have if she knew you changed them."
                "But there exists no love without sacrifice."
                "THE END"
                return
            "This has to be where it ends – neither of us will get her.":
                n "It's better off this way. If I keep another person away from love, then what right do I have to it?"
                "You end up not doing anything about the situation you caused."
                "A couple weeks later, you end up meeting %(m)s in person. The resemblance between the two of you is uncanny, and you eventually figure out that you may be cousins whose families became distant."
                "The two of you end up becoming friends – and even roommates – the next year of college."
                "Maybe you wouldn't have if he'd known what you'd done."
                "But there exists a new bond between two unlikely, but ultimately connected, individuals."
                "For what exists when there is no love?"
                return

jump scene2

return

#same name option, change vpunch to custom transition, no chem pun intended, renpy dialogue halves for this isn't about me
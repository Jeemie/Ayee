label fscene1cont:
scene black with dissolve
show text "New Beginning" at basicfade with Pause(2.5)
scene black with dissolve

scene olin with dissolve

stop music
play music "music/start.mp3"

$ f = persistent.f
$ m = persistent.m

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
        
show mshocked at fastfade, center
f "Hi there! If I'm correct, then you must be %(m)s. My name's %(f)s and we're gonna be partners!"

m "O-Oh! H-Hey there! Sorry, I wasn't paying too much attention before."

hide mshocked at fastfade
show mhappy at basicfade, center

f "Well, I hope you don't do that when we're working, too – 'cause I know nothing about chemistry, so it'd be bad if neither of us did the work."

m "I-I'm sure that's not true. W-We'll both do the work, and it won't be so bad. I'm sure of it."

m "We should get going before the next class comes in, though."

"You notice that you're the last two left in the classroom, and students for the next class are about to come in."

f "So, we should plan a time to get together and plan everything out."

m "Well, I'm free right now, if you're not busy."

f "I actually have a class right now, but how about we meet at the giant tree at 5:00?"

m "O-OK, that works for me! I'll see you then."

f "Yeah, bye for now!"

show text "He seemed a bit strange, as if he were really nervous, but you have no idea why. You guess it must just be because it's the first day of classes." at basicfade,truecenter with Pause(2.5)
pause 1
hide text at basicfade
pause 1.0

show text "Hopefully he isn't hard to deal with..." at basicfade,truecenter with Pause(2.5)
pause 1
hide text at basicfade
pause 1.0

jump fscene2

return

#same name option, change vpunch to custom transition, no chem pun intended, renpy dialogue halves for this isn't about me
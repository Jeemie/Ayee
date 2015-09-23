label scene8:
    
scene black with dissolve
show text "Calamity" at basicfade with Pause(2.5)
scene black with dissolve


scene tree with dissolve
show fangry at fastfade, center
m "What are you thinking??"

f "What am I thinking? I'm thinking you're a jerk!"

m "That's not what I meant! What was up with you back there? You've been so hostile lately, and I have no idea why."

f "You have no idea? You're the problem! I can't handle your constant mood swings!"

m "What are you talking about?"

f "It's as if each time I see you you're a different person! And you act so clueless, like you're trying to make me feel dumb!"

m "{i}Well, that's because I am clueless...{/i}"

menu:
    "I think you act strangely each time I see you, too.":
        hide fangry at fastfade
        show fsad at fastfade,center
    "I really don't understand. Are you sure you're alright?":
        hide fangry at fastfade
        show fsad at fastfade,center
    "Maybe you're mistaking someone else for me?":
        hide fangry at fastfade
        show fsad at fastfade,center

f "What?"
hide fsad at fastfade
show fangry at fastfade,center
f "What? No, this isn't about me! Ugh, I can't believe you sometimes!"
hide fangry at fastfade

show tree at dim
show black behind tree

show text "She storms off in a fit of rage. You're left to ponder exactly what just happened." at basicfade, truecenter
pause 2.0
hide text at basicfade

"{i}Could it have really been something that I did? But everything had seemed to be going so well.{/i}"
"{i}And I was even going to ask her out if we got a good grade on our assignment!{/i}"
"{i}Have I really been acting differently though?{/i}"
"GAHHH! I don't understand women at all!"

if persistent.beat_female == True:
    $ beat_male =True
    $ persistent.epilogue = True
    return
elif persistent.beat_male != True:
    $ persistent.beat_female = True
    $ persistent.beat_game =True
    return
    
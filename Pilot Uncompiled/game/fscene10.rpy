label fscene10:
scene black with dissolve
show text "Bigger Kaboom" at basicfade with Pause(2.5)
scene black with dissolve

show tree at fastfade
show mangry at fastfade, center
m "What are you thinking?!"

f "What am I thinking? I'm thinking you're a jerk!"

m "That's not what I meant! What was up with you back there? You've been so hostile lately, and I have no idea why."

f "You have no idea? You're the problem! I can't handle your constant mood swings!"

m "What are you talking about?"

f "It's as if each time I see you, you're a different person! And you act so clueless, as if you're trying to make me feel dumb!"

m "Well, it's seems that you're the one who's different every time I see you."

f "What?"
f "What? No, this isn't about me! Ugh, I can't believe you sometimes!"


hide mangry at fastfade
show tree at fastfade
show black behind tree
show tree at dim
show text "You storm off in a fit of rage. He doesn't dare to follow you again. You feel as though you're not in control of your body. Your mind tells you he did nothing wrong." at basicfade,truecenter with Pause(10.2)
pause 1
$ renpy.pause(2, hard='True')
hide text at basicfade


show text "But your heart tells your mind that it's dead wrong." at basicfade,truecenter with Pause(3.0)
pause 1
$ renpy.pause(2, hard='True')
hide text at basicfade


show text "Unfortunately, you're caught in the middle of a raging internal war." at basicfade,truecenter with Pause(3.6)
pause 1
$ renpy.pause(2, hard='True')
hide text at basicfade


if persistent.beat_male ==True:
    $ persistent.beat_female =True
    $ persistent.epilogue =True
    jump credits
    return
elif persistent.beat_male != True:
    $ persistent.beat_female =True
    $ persistent.beat_game =True
    jump credits
    return

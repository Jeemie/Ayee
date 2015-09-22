label fscene10:
scene black with dissolve
show text "Bigger Kaboom" at basicfade with Pause(2.5)
scene black with dissolve

scene bg tree with dissolve
show m angry at fastfade
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

if persistent.beat_male ==True:
    $ persistent.beat_female =True
    $ persistent.epilogue =True
    return
elif persistent.beat_male != True:
    $ persistent.beat_female =True
    return

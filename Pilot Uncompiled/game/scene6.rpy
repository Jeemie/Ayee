label scene6:
    
scene black with dissolve
show text "Day Three \n Work Time" at basicfade with Pause(2.5)
scene black with dissolve


scene labroom with dissolve
show fangry at fastfade, center
f "Ahh! I can't understand this at all! Why do we need to figure out how they're going to react? Why don't we just combine them all and see what happens? Isn't that what experimentation is?"

menu:
    "Go for it!":
        "She pours every chemical within reach into a single beaker, an excited smile on her face. You can't help but admire her adventurous attitude and look on in wonder as her experiment bubbles."
        show fhappy at basicfade,center
        f "Look! It's doing something! I told you, experiments should –"
        hide labroom at fastfade
        show black at fastfade
        $ renpy.movie_cutscene("video/boom.mpg")
        show text "There isn't any time to react as the solution bubbles to a climax and explodes in her face. You can't feel anything as you're caught in the blast." at basicfade,truecenter
        $ renpy.pause(5.0, hard='True')
        hide text basicfade
        scene black with dissolve
        show text "Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
    "Maybe we should try something else...":
        m "I guess so, but I'm sure they don't want us to cause an explosion. Besides, it's not so hard. We just have to look up the chemical compounds they'll form."

f "I'm just not good at chemistry. I took it in high school, so I thought it would be easy now, but I still don't get it! I'm doomed!"

m "Don't worry. Since we're partners, I'll be here to help, and I'll make sure you don't fail! I'll teach you everything you need to know."

hide fangry at fastfade
show fhappy at fastfade,center

f "You would? Ohh, thank you so much, %(m)s! That's so nice of you!"

hide fhappy at fastfade
show labroom at dim
show black behind labroom
show text "You then notice that her arms are around you, and you're pulled into a hug. She nearly squeezes some of the life out of you, but you enjoy it nonetheless. Your cheeks momentarily turn red in the process, but you don't think she noticed."  at basicfade,truecenter with Pause(5.5)
$ renpy.pause(1.0, hard='True')
hide text at basicfade
show text "The rest of your lab time is spent performing various infusions of chemicals as you explain their properties to your partner. You feel a warm connection between the two of you, and you hope that you're not the only one who feels it."  at basicfade,truecenter with Pause(4.5)
$ renpy.pause(1.0, hard='True')
hide text at basicfade


scene black with dissolve
show text "Day Three \n Forming the Bond" at basicfade with Pause(2.5)
scene black with dissolve

show goddard at basicfade
show fhappy at basicfade,center
f "So hey...There's this concert in Boston this week that I'd love to see, but most of my friends are going home over the weekend."

m "Dang, that really sucks. Is there anybody else you can ask?"

f "Well...do you want to go?"

m "Hmm..."

m "O-Oh! Y-Yeah! I'd love to – I mean, that sounds pretty awesome. Of course I'll go!"

hide fhappy at fastfade
show black behind goddard
show goddard at dim
show text "The two of you began spending more time together." at basicfade, truecenter
pause 3.0
hide text at basicfade
pause 3.0
show text "Over the next three weeks, the two of you continue your routine lab work and usually find time to eat dinner together during the week." at basicfade, truecenter
pause 3.0
hide text at basicfade
pause 3.0
show text "She even convinced you to join the fencing club, and you've made even more friends there. It seems like things are going right in life." at basicfade, truecenter
pause 4.0
hide text at basicfade
pause 1.0
show goddard at undim
show fhappy at basicfade,center


m "H-Hey, %(f)s, there's something I want to tell you..."

f "Hmm? What is it? Is it about the lab?"

m "Umm...well..."

hide fhappy at fastfade
show goddard at dim
show text"No matter what, you just couldn't tell her how you felt." at basicfade, truecenter
pause 1
hide text at basicfade
pause 1.0

m "Yeah, it is actually about the lab..."

show text "You begin to notice some things about her that you hadn't before; how caring she can be, how she always makes sure all her food is completely separated, how she always makes you laugh even just by laughing herself." at basicfade,truecenter with Pause(2.5)
pause 3.0
hide text at basicfade
pause 1.0

show text "There are some days however where you're not sure that she feels the same way about you. Sometimes she'll give you the cold shoulder and won't text you back." at basicfade,truecenter with Pause(2.5)
pause 3.0
hide text at basicfade
pause 1.0

show text "When you ask her if she's mad at you, she just sighs and replies that nothing's wrong. After that, things tend to go back to normal for a while until it happens again. You can never tell what's bothering her though, until one day..." at basicfade,truecenter with Pause(2.5)
pause 5.0
hide text at basicfade
pause 1.0

jump scene7
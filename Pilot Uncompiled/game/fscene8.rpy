label fscene8:
scene black with dissolve
show text "Chem Time!" at basicfade with Pause(2.5)
scene black with dissolve

show labroom at fastfade
show mhappy at basicfade,center
f "Ahh! I can't understand this at all! Why do we need to figure out how they're going to react? Why don't we just combine them all and see what happens? Isn't that what experimentation is?"

menu:
    "{size=40}{b}Go for it!{/b}":
        "You pour every chemical within reach into a single beaker, an excited smile on your face. You can't help but admire your handywork as your experiment starts to bubble."
        hide mhappy at fastfade
        show mshocked at fastfade, center
        f "Look! It's doing something! I told you, {b}that's{/b} how experiments should be!"
        m "Wait, what did you put –"
        hide labroom at fastfade
        show black at fastfade
        $ renpy.movie_cutscene("video/boom.mpg")
        show text "There isn't any time to react as the solution bubbles to a climax and explodes in your face. You can't feel anything as you're caught in the blast." at basicfade,truecenter with Pause(8.4)
        pause 1
        hide text at basicfade
        scene black with dissolve
        show text "Game Over" at basicfade with Pause(2.5)
        scene black with dissolve
        return
    "{size=40}{b}Maybe ask for some help...{/b}":
        m "Well, I'm sure they don't want us to cause an explosion. Besides, it's not so hard. We just have to look up the chemical compounds they'll form."

f "I'm just not good at chemistry. I took it in high school, so I thought it would be easy now, but I still don't get it! I'm doomed!"

m "Don't worry. Since we're partners, I'll be here to help, and I'll make sure you don't fail! I'll teach you everything you need to know."

f "You would? Oh, thank you so much, %(m)s! That's so nice of you!"

show black behind labroom
show labroom at dim
show text "You then go over and give him a hug in thanks. You don't notice, but you accidentally squeeze him just a little too hard, nearly cracking a couple bones, but it seems he enjoys it nonetheless. You almost think you saw his cheeks turn a little red..." at basicfade,truecenter with Pause(14.1)
pause 1
hide text at basicfade
pause 1.0

show text "The rest of your lab time is spent performing various infusions of chemicals as [m] explains their properties to you. You feel a warm connection between the two of you, and you think it might not just be you." at basicfade,truecenter with Pause(11.7)
pause 1
hide text at basicfade
pause 1.0

jump fscene9
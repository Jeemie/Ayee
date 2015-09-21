label fscene8:
scene black with dissolve
show text "Chem Time!" at basicfade with Pause(2.5)
scene black with dissolve

scene bg lab
show mhappy
f "Ahh! I can't understand this at all! Why do we need to figure out how they're going to react? Why don't we just combine them all and see what happens? Isn't that what experimentation is?"

menu:
    "Go for it!":
        "You pour every chemical within reach into a single beaker, an excited smile on your face. You can't help but admire your handywork as your experiment starts to bubble."
        show mshocked
        f "Look! It's doing something! I told you, {b}that's{/b} how experiments should be!"
        m "Wait, what did you put –"
        $ renpy.movie_cutscene("video/boom.mpg")
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

jump fscene9
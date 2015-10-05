label scene7:
    
scene black with dissolve
show text "Day Three \n The Meltdown" at basicfade with Pause(2.5)
scene black with dissolve


show labroom at basicfade
show labroom at dim
show black behind labroom
show text "The two of you are in the lab working on your latest assignment. [f] hasn't asked for any help in a while, and it's been pretty quiet between you two." at basicfade,truecenter with Pause(9.0)
$ renpy.pause(4.0, hard ='True')
hide text at basicfade
show text "You notice that she hasn't been doing much work, just holding a beaker full of some strange liquid." at basicfade,truecenter with Pause(5.4)
$ renpy.pause(4.0, hard ='True')
hide text at basicfade

show labroom at basicfade
show fangry at fastfade,center

m "Hey, we should probably start to mix the chemicals if we want to finish."

f "Fine, I'll mix them."

hide fangry at fastfade
show labroom at dim
show black behind labroom
show text "She proceeds to dump the entire beaker into a bowl full of some white powder, and it immediately begins to smoke." at basicfade,truecenter with Pause(6.3)

$ renpy.pause(4.0, hard ='True')
hide text at basicfade
show labroom at basicfade
m "Hey! What are you doing?! Be careful with those! We could get in a lot of trouble for mixing things randomly. You have to think before you do something like that, okay?"

f "Oh really? I have to think first? Well, maybe you're the one who needs to think before he does things! Or do you just not care about anybody else at all?"


show text "She suddenly packs up all her things and leaves the classroom before you can even say anything." at basicfade,truecenter with Pause(5.1)
pause 2.0
hide text at basicfade
m "H-Hey, wait!"

show text "You get up and chase after her, heading outside and running to catch up." at basicfade,truecenter with Pause(4.2)
pause 2.0
hide text at basicfade
jump scene8
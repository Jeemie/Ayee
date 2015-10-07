label scene2:

scene black with dissolve
show text "Day Two \n Dorm Room Troubles" at basicfade with Pause(2.5)
scene black with dissolve

show dorm with dissolve

show dorm at dim
show black behind dorm
show text "It’s almost 5:00. You’re sitting in your room waiting to head out to meet her. It’s a good thing your roommates aren't here, or they might get annoyed with all the pacing you’re doing." at basicfade,truecenter with Pause(10.5)
$ renpy.pause(3.5, hard='True')
hide text at basicfade
show dorm at undim
pause 1.0
hide black

m "{i}It’s nothing to be worried about. You’re supposed to be there. You’ll talk about...things. And if not, there’s always chemistry work to fall back on.{/i}"

show dorm at dim
show black behind dorm
show text "But you can’t help thinking how cute she was..." at basicfade,truecenter with Pause(2.7)
pause 1
hide text at basicfade
pause 1.0
show text "But you might scare her away{cps=0.1}...{/cps}" at basicfade,truecenter with Pause(1.8)
pause 1
hide text at basicfade
pause 1.0
show text "But you're going to be late if you don't leave{cps=0.5}...{/cps}" at basicfade,truecenter with Pause(3.0)
pause 1
hide text at basicfade
pause 0.5
m "{cps=1}...{/cps}{nw}"
show dorm at undim
pause 1.0
hide black

play sound "sfx/dramaticpunch.wav"
with vpunch

m "Alright, I'm heading out!"

jump scene3
return
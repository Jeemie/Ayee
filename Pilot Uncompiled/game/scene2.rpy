label scene2:

scene black with dissolve
show text "Day Two \n Dorm Room Troubles" at basicfade with Pause(2.5)
scene black with dissolve

scene dorm with dissolve

"It’s almost 5:00 pm and you’re sitting in your room waiting to head out to meet %(f)s.
 It’s a good thing your roommates are out or they might get annoyed with all the pacing you’re doing."

m "It’s nothing to be worried about, you’re supposed to be there and you’ll talk about… things. And if not… There’s always chemistry work to fall back on."

show text "But you can’t help thinking how cute she was..." at basicfade,truecenter with Pause(2.5)
pause 1
hide text at basicfade
pause 1.0
show text "But you might scare her away{cps=0.1}...{/cps}" at basicfade,truecenter with Pause(2.5)
pause 1
hide text at basicfade
pause 1.0
show text "But you're gonna be late if you don't leave{cps=0.5}...{/cps}" at basicfade,truecenter with Pause(2.5)
pause 1
hide text at basicfade
pause 0.5
m "{cps=1}...{/cps}{nw}"

play sound "sfx/dramaticpunch.wav"
with vpunch

m "Alright, I'm heading out then!"

jump scene3
return
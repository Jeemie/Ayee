label fscene2:
scene black with dissolve
show text "On the Quad" at basicfade with Pause(2.5)
scene black with dissolve

show quad with dissolve
show black behind quad
show quad at dim
show text "You've finished the rest of your classes for the day. You're walking through the Quad to meet your partner at the large tree on campus." at basicfade,truecenter with Pause(7.5)
pause 1
$ renpy.pause(2, hard='True')
hide text at basicfade


show text "You get halfway across the Quad when you notice someone walking in the opposite direction." at basicfade,truecenter with Pause(4.5)
pause 1
$ renpy.pause(2, hard='True')
hide text at basicfade
show quad at basicfade
pause 1.0

show nhappy at fastfade,center
f "Hey, %(m)s, where are you going? You're going to be late! Don't forget that we're meeting at the tree in 5 minutes!"

hide nhappy at fastfade
show nshocked at fastfade,left 
show quad at dim
show black behind quad
show text "He stops as he's walking by and turns to you for a moment. You keep moving past him and give him a smile. He probably just has to stop at his room first, or something like that." at basicfade,truecenter with Pause(11.1)
pause 1
hide text at basicfade
pause 1.0



jump fscene3
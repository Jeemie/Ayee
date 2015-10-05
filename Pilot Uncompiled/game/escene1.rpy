label escene1:
scene black with dissolve
show text "Where It All Began" at basicfade with Pause(2.5)
scene black with dissolve

stop music
play music "music/lament.mp3"

$ f = persistent.f
$ m = persistent.m

show text "I'm not a guy who's very experienced with love." at basicfade,truecenter with Pause(2.7)
pause 1
hide text at basicfade


show text "Well, even if I were, I'm not sure how anybody is supposed to deal with being hit by it." at basicfade,truecenter with Pause(5.7)
pause 1
hide text at basicfade


show text "The first thing to be said is that movies just don't do it justice. A picture's worth a thousand words, and a moving picture's worth even more, but love can't even be described in words alone." at basicfade,truecenter with Pause(10.8)
pause 1
hide text at basicfade

show text "The one thing they've gotten right is that love can make you do some crazy things..." at basicfade,truecenter with Pause(4.8)
pause 1
hide text at basicfade


scene quad with dissolve
show fhappy at basicfade,center
f "Hey, %(m)s, where are you going? You're gonna be late! Don't forget that we're meeting at the tree in 5 minutes!"

show black behind quad
hide quad at fastfade
show fhappy at dim
show text "And that was the first time I saw her. I guess the movies also got the whole \"love at first sight\" thing too." at basicfade,truecenter with Pause(6.9)
pause 1
hide text at basicfade


jump escene2
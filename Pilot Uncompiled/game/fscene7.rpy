label fscene7:
scene black with dissolve
show text "The Rejection" at basicfade with Pause(2.5)
scene black with dissolve

scene bg quad with dissolve
"It's later in the day now, and you're heading back to your dorm after having dinner with some of the friends from your dorm. So far, it seems like a bright, happy day for some reason, even though you have the most classes on Tuesdays."

"You notice someone sitting on a bench, alone, next to the path you're walking on. As you get closer, you recognize %(m)s sitting and looking serious."

show nsad at basicfade, center
f "Hey, %(m)s, what's up? Why are you sitting out here all alone?"

hide nsad at fastfade
show nangry at fastfade, center
m "I don't want to talk to you. Why don't you get out of here?"

f "W-What? What's wrong??"

m "It's nothing."

hide nangry
"%(m)s walks off towards one of the dorm buildings and you're left wondering just what had happened to him. Maybe it was something serious."

"It seemed like he didn't want you to pry into it, though, so you decide to leave it alone. If he wanted to tell you, he would."

show text "It disappoints you a bit that he didn't, but you don't know why." at basicfade,truecenter with Pause(2.5)
pause 1
hide text at basicfade
pause 1.0


jump fscene8
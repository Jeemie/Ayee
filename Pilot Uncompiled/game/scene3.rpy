label scene3:
    

scene black with dissolve
show text "Day Two \n The Big Meeting" at basicfade with Pause(2.5)
scene black with dissolve

scene tree
show black behind tree
m "{i}There she is! Wow, I don’t think I got a very good look at her yesterday, but she looks...{/i}"
stop music

show fangry at fastfade,center with moveinleft

play sound "sfx/objection.wav"
with vpunch
f "{cps=20}{size=+10}There you are!{/size}{/cps}{nw}"
play sound "sfx/objection.wav"
with hpunch
f "{cps=20}{size=+10}You're late!{/size}{/cps}{nw}"
play sound "sfx/objection.wav"
with vpunch
f "{cps=18}{size=+10}I'll have you know {size=+5}my time is {/cps}{cps=6}very precious!{/cps}{/size}{/size}"

m "Sorry! I'm sorry!"

m "{i}...mad. She looks pretty mad...I'm not that late, am I?{/i}"

f "I knew you weren't going to make it in time. Didn't you hear me before?"

m "A-ah, no, I guess I must have missed it. I'm really sorry I'm late, so, we should{cps=2}...{/cps}get things going, I guess?"

hide fangry at fastfade
show fhappy at fastfade,center
play music "music/start.mp3"
f "Yeah, you’re right. Well, we already introduced ourselves yesterday, so let’s get down to business!"
f "I’m free on Wednesdays from 6-8 and then I’m also available at 1, but I have a class at 3, so we might be pressed for time then."
m "Wednesday at 6 works for me!"
f "Alright then! I guess we could bring dinner with us. Or if you're free before that, we can go get some together."

show tree at dim
hide fhappy at fastfade,center
show text "You can't stop your heart from pounding when you hear that. Going to get dinner together? Just the two of you?" at basicfade,truecenter with Pause(6.3)
pause 1
hide text at basicfade
"{cps=2}...{/cps}"
play sound "sfx/idea.wav"
"...{fast}!!"
"{size=+15}{cps=30}It's almost like a date!{/cps}{/size}"
show tree at undim
hide fhappy at fastfade
show fsassy at fastfade,center
f "I guess that’s everything we really need to cover."
f "I guess we could have just e-mailed each other, but this was good anyway."
m "Do you want to go get something to eat right now?"
show tree at dim
hide fsassy at fastfade,center
show text "What did you just say?"  at basicfade,truecenter with Pause(1.5)
pause 1
hide text at basicfade
m "{i}What did I just say?{/i}"
show tree at undim
show fsassy at fastfade,center


f "Well, I have to get back to my homework later, but sure! I haven't eaten yet."
hide fsassy at basicfade with moveoutright
show tree at dim
show text "You let out the breath you hadn’t even known you were holding and smiled." at basicfade,truecenter with Pause(4.2)
pause 1
hide text at basicfade
show text "Your legs are shaking a bit, but you're certain she won't notice. Besides, you're much too happy to stop them!" at basicfade,truecenter with Pause(6.0)
pause 1
hide text at basicfade
show tree at undim

m "Great! I t-think they might have Chinese food in the dining h-hall today!"

show tree at dim
show text "You prayed that you would be able to stop stuttering soon as the two of you headed toward the dining hall." at basicfade,truecenter with Pause(6.3)
pause 1
hide text at basicfade


jump scene4
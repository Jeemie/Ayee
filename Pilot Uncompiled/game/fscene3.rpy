label fscene3:
scene black with dissolve
show text "First Meeting at the Tree" at basicfade with Pause(2.5)
scene black with dissolve

show black at basicfade

show text "It's now 5:05, and you're standing at the tree, waiting for [m] to arrive. You expected he would be late based on how surprised he seemed when you passed him." at basicfade,truecenter with Pause(9.0)
pause 1
$ renpy.pause(2, hard='True')
hide text at basicfade
show text "You got the feeling he was the kind of guy who wouldn't do that on purpose. Still, it couldn't hurt to tease him a little when he did show up. Speaking of which..." at basicfade,truecenter with Pause(9.6)
pause 1
$ renpy.pause(2, hard='True')
hide text at basicfade

play sound "sfx/objection.wav"
with vpunch
f "{cps=20}{size=+10}There you are!{/size}{/cps}{nw}"
play sound "sfx/objection.wav"
with hpunch
f "{cps=20}{size=+10}You're late!{/size}{/cps}{nw}"
play sound "sfx/objection.wav"
with vpunch
f "{cps=18}{size=+10}I'll have you know {size=+5}my time is {/cps}{cps=6}very precious!{/cps}{/size}{/size}"
hide black at fastfade
show tree at basicfade
show black behind tree
m "Sorry! I'm sorry!"

f "I knew you weren't going to make it in time. Didn't you hear me before?"

show mshocked at fastfade, left
m "A-ah, no, I guess I must have missed it. I'm really sorry I'm late, so, we should{cps=2}...{/cps}get things going, I guess?"

"{i}Haha! he can be kinda cute when he's flustered. There's no sense in staying mad at him though.{/i}"

hide mshocked at fastfade
show mhappy at fastfade, left
f "Yeah, you're right. Well, we already introduced ourselves yesterday, so let's get down to business! I'm free on Wednesdays from 6-8 and then I'm also available at 1, but I have a class at 3, so we might be pressed for time then."

m "Wednesday at 6 works for me!"

f "Alright then! I guess we could bring dinner with us. Or if you're free before that, then we can go get some together."

"You see him straighten up a little more after you say that. It's pretty funny seeing him respond to you, as if he doesn't usually talk to girls."

f "I guess that's everything we really need to cover. I guess we could have just e-mailed each other, but this was good anyway."

m "Do you want to go get something to eat right now?"

f "Well, I have to get back to my homework later, but sure! I haven't eaten yet."

show tree at dim
show text "{i}Wait...{/i}" at basicfade,truecenter with Pause(1.0)
pause 1
hide text at basicfade
pause 1.0

f "{i}Wait...this doesn't count as my first date, right?{/i}"

f "{i}No, of course not!{/i}"

m "Great! I t-think they might have Chinese food in the dining h-hall today."

jump fscene4
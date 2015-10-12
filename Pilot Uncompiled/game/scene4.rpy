label scene4:
    
scene black with dissolve
show text "Day Two \n Dinner Time!" at basicfade with Pause(2.5)
scene black with dissolve

show dininghall 
#show fshocked at basicfade,center

play sound "sfx/objection.wav"
f "{size=+10}No way!! You were a championship fencer??{/size}"

m "Well, it's not that I was that good or anything, but in my sophomore year of high school I made it to the semifinals of this national tournament. At the time I was ranked 4th in the US for my age."

#hide fshocked at fastfade,center
show fhappy at fastfade,center

f "That's so incredible! You must have been awesome at it. So does that mean you're going to join the fencing team here?"

m "Well, no, I didn't plan to..."

f "Why not? It sounds like you'd do really well in it."

m "I guess...but I haven't actually fenced since I was 15."

f "But you said you had made it to the national championship – why stop after that?"

m "{i}Is this something I should be sharing with a girl I just met? But there's something that makes me just...trust her.{/i}"

m "After the championship I quit fencing to focus on getting into college. My parents had supported me completely while I was fencing, but I knew that they were having trouble keeping up with everything."

m "With work, and taking me to fencing classes, and then to another state for the championships, I didn't want to burden them any more."

f "Wow, that's really nice of you! But now that your parents don't have to worry about you, you could always start up again, right?"

m "I...I never thought of that. You're right, I could."

m "But - I don't know – it's been a long time since I've fenced."

f "Oh, I'm sure it's just like riding a bicycle! You'd definitely get back into it!"

m "{i}Maybe I could,but I don't want to think about that now, all of my focus should be on %(f)s.{/i}"

m "So what about you? I told you what I like to do, so what interests you?"

f "Well, I'm actually really big into art. When I was younger, I always loved art classes and drawing and painting."

f "What I really love though, is creating things – taking empty space and filling it with something grand and beautiful! I {b}love{/b} sculpting and designing – making something that I can love and that others can see!"

f "So that's why I came here – to become a civil engineer. One day, I'm gonna build something big and beautiful in a city or a town, or even something just for me."

m "{i}Wow, that's a big dream. It's kind of strange to know someone who already has their life planned out. Something inside me knows that she'll be able to do it, too.{/i}"

m "That sounds incredible. I've never thought that way about making things: everyone can see it, but you can still call it yours. Actually, that sounds kind of scary. I mean, what if nobody likes it?"

f "Well then, that's their problem! Besides, what makes you so sure everybody's going to hate what I make?!"

m "A-Ah, n-no! I didn't mean it like that! I think w-whatever you'd make would be incredible!"

m "{i}Your face is nearly red now as you try to reconcile her, but you completely stop when you see her wide grin.{/i}"

f "Hahahaha! I'm just kidding, %(m)s. I knew what you meant! It {b}is{/b} fun to tease you, though. You turned pretty red there, too!"

m "{i}I got played! But I don't really mind. It feels nice talking to her like this.{/i}"

show dininghall at dim
hide fhappy at fastfade,center
show text "A bit later, you check the time and find that you've been in the dining hall talking for two hours. You both get up in a hurry and exchange phone numbers before heading out. This is the first night at college that you've fallen asleep feeling truly content."  at basicfade,truecenter with Pause(14.7)
$ renpy.pause(3.0, hard='True')
hide text at basicfade
jump scene5
return
﻿label fscene5:
scene black with dissolve
show text "I'm Late! I'm Late!" at basicfade with Pause(2.5)
scene black with dissolve

scene black with dissolve

f "{i}Oh no! I don't want to be late on the second day of school! That'll give off the wrong impression for sure!{/i}"

"You were up pretty late last night doing homework after your dinner with %(m)s and ended up missing your alarm. You had to rush around your room getting ready while your roommates stood by laughing. Now you're making a mad dash for your chemistry class."

f "{i}Wait, isn't that –{/i}"

f "{i}But he shouldn't be here...{/i}"

show quad with dissolve
"You see %(m)s walking into another building."

f "{i}He should be heading to chemistry.{/i}"

show black behind quad
show quad at dim
show text "You have no time to stop. You must press onward to class." at basicfade,truecenter with Pause(3.6)
pause 1
hide text at basicfade
pause 1.0

jump fscene6
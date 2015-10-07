label escene4:
scene black with dissolve
show text "Thick Like Cool Whip" at basicfade with Pause(2.5)
scene black with dissolve

show tree with fastfade
show fsad at basicfade,center
n "Hey, %(f)s, what's up?"

f "Oh, h-hey %(m)s, nothing really. Who's that you're with?"

n "Oh, that's just this girl whom I'm helping with calculus. You know, she really needed help, so I offered to tutor her privately."

f "That's...so nice of you. I'm glad you could do that. I've got to go now, though."

hide fsad at basicfade
n "I hadn't thought of myself as crazy at the time. I was just mad."

n "Madly in love, that is. Get it?"

n "I thought that if I was going to get the girl, I had to make sure that she wasn't already taken. Even if she was taken by another me."

show black at basicfade
n "Looking back, maybe I should have questioned why we looked the same..."

n "But that doesn't matter anymore. The only thing that matters is the final choice I have to make."

menu:
    "{size=40}{b}It was a mistake. They deserve to be together.{/b}":
        n "I can't do this – I have to fix it. It wouldn't be right to force them apart."
        "You first see %(f)s, who is furious at you until you explain who you are. You take her to see %(m)s, and she is once again shocked."
        "When you both meet, you are stunned at the similarities you share. The resemblance is uncanny, but you quickly explain your side of the story before everything can even be processed. Before anybody knows it, you're gone."
        "You leave them to work it out and mend what was previously broken."
        "A deep sadness fills your heart afterward – even over a trivial spark like the one you had for her."
        "But there exists no love without sadness."
        "THE END"
        jump credits
        return
    "{size=40}{b}Maybe I deserve love, and maybe she deserves me.{/b}":
        n "Now's my chance. I've waited quite a while for this, and I can't let the chance pass me up!"
        "You decide to wait a day, and you make sure you're wearing distinct clothing."
        "In fact, you end up changing a lot of things about yourself."
        "You decide to get a new haircut."
        "You start wearing lots of hats."
        "You even start wearing glasses."
        "You've changed a lot about yourself, but %(f)s tells you she likes the way it all looks."
        "Maybe she wouldn't have if she knew you changed them."
        "But there exists no love without sacrifice."
        "THE END"
        jump credits
        return
    "{size=40}{b}This has to be where it ends. Neither of us will get her.{/b}":
        n "It's better off this way. If I keep another person away from love, then what right do I have to it?"
        "You end up not doing anything about the situation you caused."
        "A couple weeks later, you meet %(m)s in person. The resemblance between the two of you is uncanny, and you eventually figure out that you may be cousins whose families became distant."
        "The two of you end up becoming friends – and even roommates – the next year of college."
        "Maybe you wouldn't have if he'd known what you'd done."
        "But there exists a new bond between two unlikely, but ultimately connected, individuals."
        "For what exists when there is no love?"
        jump credits
        return
    "{size=40}{b}Where did this all go wrong?{/b}":
        n "I can't even begin to think of how I became like this, but I know how I feel about her. To me, that justifies everything. Who else will see it that way, though?"
        menu:
            "{size=40}{b}It was a mistake. They deserve to be together.{/b}":
                n "I can't do this – I have to fix it. It wouldn't be right to force them apart."
                "You first see %(f)s, who is furious at you until you explain who you are. You take her to see %(m)s, and she is once again shocked."
                "When you both meet, you are stunned at the similarities you share. The resemblance is uncanny, but you quickly explain your side of the story before everything can even be processed. Before anybody knows it, you're gone."
                "You leave them to work it out and mend what was previously broken."
                "A deep sadness fills your heart afterward – even over a trivial spark like the one you had for her."
                "But there exists no love without sadness."
                "THE END"
                jump credits
                return
            "{size=40}{b}Maybe I deserve love, and maybe she deserves me.{/b}":
                n "Now's my chance. I've waited quite a while for this, and I can't let the chance pass me up!"
                "You decide to wait a day, and you make sure you're wearing distinct clothing."
                "In fact, you end up changing a lot of things about yourself."
                "You decide to get a new haircut."
                "You start wearing lots of hats."
                "You even start wearing glasses."
                "You've changed a lot about yourself, but %(f)s tells you she likes the way it all looks."
                "Maybe she wouldn't have if she knew you changed them."
                "But there exists no love without sacrifice."
                "THE END"
                jump credits
                return
            "{size=40}{b}This has to be where it ends. Neither of us will get her.{/b}":
                n "It's better off this way. If I keep another person away from love, then what right do I have to it?"
                "You end up not doing anything about the situation you caused."
                "A couple weeks later, you meet %(m)s in person. The resemblance between the two of you is uncanny, and you eventually figure out that you may be cousins whose families became distant."
                "The two of you end up becoming friends – and even roommates – the next year of college."
                "Maybe you wouldn't have if he'd known what you'd done."
                "But there exists a new bond between two unlikely, but ultimately connected, individuals."
                "For what exists when there is no love?"
                jump credits
                return
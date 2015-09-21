# You can place the script of your game in this file.
# Declare characters used by this game.

# The game starts here.
label start:


menu:
    "Play Male Side":
        if persistent.beat_female == True:
            jump scene1cont
        elif persistent.beat_female != True:
            jump scene1
    
    
    "Play Female Side":
        if persistent.beat_male == True:
            jump fscene1cont
        elif persistent.beat_male != True:
            jump fscene1
        
    "Play Epilogue" if persistent.epilogue == True:
        jump escene1
        










#same name option, change vpunch to custom transition, no chem pun intended, renpy dialogue halves for this isn't about me
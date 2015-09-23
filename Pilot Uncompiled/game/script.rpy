# You can place the script of your game in this file.
# Declare characters used by this game.

# The game starts here.
label start:



show bg3 at mmenu4

show heart at mmenu5

menu:
    
    "Play New Game +" if persistent.beat_game == True:
        jump menu2
    
    
    "Play Male Side":
        jump scene1
    
    
    "Play Female Side":
        jump fscene1
        
label menu2:
    

show bg3 at mmenu4

show heart at mmenu5

menu:
    
    "Play Male Side":
        jump scene1cont

    
    "Play Female Side":
        jump fscene1cont

        
    "Play Epilogue" if persistent.epilogue == True:
        jump escene1
        
#to do later: same name option, change vpunch to custom transition, no chem pun intended
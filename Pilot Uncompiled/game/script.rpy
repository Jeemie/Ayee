# You can place the script of your game in this file.
# Declare characters used by this game.

# The game starts here.
label start:



show bg3 at mmenu4, topleft

show heart at mmenu5, topleft

menu:
    

    
    "{size=40}{b}Play New Game +{/b}" if persistent.beat_game == True:
        jump menu2
    
    
    "{size=40}{b}Play Male Side{/b}":
        jump scene1
    
    
    "{size=40}{b}Play Female Side{/b}":
        jump fscene1
        
label menu2:
    

show bg3 at mmenu4

show heart at mmenu5

menu:
    
    "{size=40}{b}Play Male Side{/b}":
        jump scene1cont

    
    "{size=40}{b}Play Female Side{/b}":
        jump fscene1cont

        
    "{size=40}{b}Play Epilogue{/b}" if persistent.epilogue == True:
        jump escene1
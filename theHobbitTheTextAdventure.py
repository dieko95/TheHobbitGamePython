'''
The Hobbit, the text adventure

The purpose of this text adventure is to briefly experience the case scenario of being in the shire and being confused by Bilbo. 
The game is based on Tolkien’s The Hobbit and it includes excerpts of this book. The game is based on probabilities according to what the user
 responds in the beginning (smelly feet and sense of adventure). One bug was identified in the input of the player’s name, it is possible to input numbers. 

Thank you for playing this text adventure, I hope you enjoy it!  

'''



import sys
from time import sleep
import random
import re

goblinLifePoints = 100
playerLifePoints = 100


# Helper Function for Input Hobbit Name
    # It has a bug, it permits users to input numbers

def hobbitNameInput():

    hobbitName = input("> What's your Hobbit name\n")
    wordsFinalPattern = re.search('\w', hobbitName)

    while wordsFinalPattern == None or hobbitName == '':
        print(
            '> Please write your hobbit name with no White Spaces and at least one letter'
        )
        hobbitName = input("> What's your Hobbit name?")
        wordsFinalPattern = re.search('\w', hobbitName)

    return hobbitName


# Adventure Sense Input, if user selects 3 or 4 they will be more likely to offend the dwarves

def adventureSenseInput():

    try:

        adventureSenseList = [1, 2, 3, 4]
        adventureSense = int(input("> From 1 to 4 how adventurous are you?\n"))

        while adventureSense not in adventureSenseList:
            print('> Please write any integer number between 1 to 4 (e.g. 2)')
            adventureSense = int(input("> From 1 to 4 how adventurous are you?\n"))
        
        return adventureSense
    
    except:

        print('\n> Something went wrong, Gandalf just arrived to fix it!')
        print('> Please write any integer number between 1 to 4 (e.g. 1)')
        adventureSenseInput()

# Smelly feet input, helpful during the battle. The player inflinges more damage.
def smellyFeet():
    smellyFeetList = ['yes', 'no']
    smellyFeet = input("> Do you have smelly feet? yes/no\n").lower()

    while smellyFeet not in smellyFeetList:
        print('> Please write yes or no')
        smellyFeet = input("> Do you have smelly feet? yes/no\n").lower()
   
    return smellyFeet



# Cool Ascii art generated with jp2a ubuntu package.
 # e.g. jp2a --background=light --invert dwight1.jpg  

dwight = ("""

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKOxdkK0KXX0O0NNXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMX0kdc;,,,;;,....';;ccccldkKNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWKxl,................',;:;;;;:::cokKWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWKx:,,'......  .............',;;,''',,;;:oOWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMM0c,''............................',.......'';oKMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWo,'..................',,;;'''''.................:KMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMX:'.........''.....':loddxxdoc:,'.'''.... ....... ..:KMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMK:'..'...'',,;,'.';cxO000000OOkxl:;,'...... ......   ..KMMMMMMMMMMMMMM
MMMMMMMMMMMMMMK;,.....''',,,;,,:oxO0KKKKKKK00Okxdl:,'.....   .....    .XMMMMMMMMMMMMM
MMMMMMMMMMMMMW,.'''...',,;;:,;lxO0KXXXXXXKKK00Okkxoc,...     .....     lMMMMMMMMMMMMM
MMMMMMMMMMMMMN..''''.,,,;;:;;ok0KXXXXXXXXXKKK0OOkkxdc,..      .. .     ,MMMMMMMMMMMMM
MMMMMMMMMMMMMk..'',',,,;:::;ok0KXXXXXXXXXXKK00OOOkxdol;..              ,MMMMMMMMMMMMM
MMMMMMMMMMMMMl .',,'',,cc:;:x0KXXXXNXXXXXXKK000OOkxddolc,.            .;MMMMMMMMMMMMM
MMMMMMMMMMMMN. ..'''.,:dlc:oOKXXXXXXXXXXKXKK00OOkkxdddolc;.            ,MMMMMMMMMMMMM
MMMMMMMMMMMMo   ....',dkolldKXXXXXXXXXKKKKKK00OOOkxxxdolc:;...         ;MMMMMMMMMMMMM
MMMMMMMMMMMM;    ...;xO0dkxOKKXXXXXXXKKKK0KKK00OOOkkxdolc::;....       'WMMMMMMMMMMMM
MMMMMMMMMMMM,      ;dO00OOO0KKXXXXXKKKK000KK0K000OOkxdolcc:;''...  .   .XMMMMMMMMMMMM
MMMMMMMMMMMMc      oOO0000KKKXXXXXXKKKK0000KKK00OOOkxxdolc:,''...  .   'WMMMMMMMMMMMM
MMMMMMMMMMMMNl.    lOO00000000KKKKXKKKK0000K00OOOkkddoll:,'..''..     .dMMMMMMMMMMMMM
MMMMMMMMMMMMMMX,. .'okOOkkxxxdolccllllodkkkxoool:;,''..'.'...'''..   .:WMMMMMMMMMMMMM
MMMMMMMMMMMMMMWx:.'c;xxxddlcl:,..;;;;:ooxkxl;;..'';,...'...'';,'..   .xMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMXOc,dkOkOkxddxdcccolldkxox0Oxc:';:coolc:;,,',:l:,..  ..KMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNO:xO000000OOOOkkkxkOOcoKK0Ol,:;coxxxxdoolc:cc:,.....cMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMXddO00O00K00000OO0KKOxKXK0kl,;ccdxxkkkkkxdocc,'.....KMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWkok0K000000000KK00Ok0KK00kl;,;codxkkkkxdoc:,'.....cMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMXlkO0KKKK00OOkkkkOO0KKXKKOo;'';odxxxxddol:;,''....XMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMxxO000KKXXXK0OkO00Oxk00kd:',,'lxOOOOOkxo:;''....oMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMXdOO000KKK0Okk0KK0kxxOxl:'';;:odxkOOkxdl:,''....0MMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMKOO00000OkOOKKKK000K0Okkxdoolooooddxxdc;,,'..'0MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMXkO00000OO000KKKKKKKOkO0Okxdolccclcdkdc,,,'..lMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMOO00000K00OkOOkkxxxxddllcc;,,,,:ldkko:,,,'.'KMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNkO0000KK00O00Okkkxxxxdol:;,,;coxOko:;;,,'.xMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMXkO000KK0000K000OOxxddolc;;:lodxkdc;;;,'.lWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMM0kO00000000KKK00Okxxxxdoooddddddl:;;,'.;NMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWOkO0000000KKK00000Okxdoddddolcc:;;,...kMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWkkOO000000K000000OOkxoloolc:;;;,'...'NMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNkkkOOOOO0000000OOkxdolloc;,,''.....cMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMKOkxkkkkkkOOkkkxddolccc;,'.........dMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWOkOOkxxxxxdoollcc::;;,,''..........:dNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWOoxxO000kxdddddooolcc:;,'''...',,'..,,;'xMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMM0l:ldkxk0000Okxdollcc:;;,,,,,,;;:;'',,.':..lWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNOl:;;odxkkxO00000OOOkxdolcccc::cllc:;;'..';'..:NMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWNK0Okxl::;;;'oxxkOOxxO0000000OOkxddolloddol:,'...''....'xWMMMMMMMMMMMMMMM
MMMMMMX0xl:,''';:::;;;;;'lxxkOOOkooxO0000OOOkxxdooxxdl:,'''..........:0WMMMMMMMMMMMMM
MWKko;,,''...,:::;;;;;,,,cxxkOOOOkdclxO00OOOOOkxxxdolc:,''''.. .......';cdk0XWMMMMMMM
:,,''''''.',:::;;;;;,'',,:xxkOOOOOkxlcloxOOOOkkxxdollc:;,,'.. ..........''.'',:ldOKWM
'''''''.';::::::;;,'''',,;xkkOOOOx:;:dddoodooxxddollc:;;,,'.. ..........''''..'',;::o
''''''..,;:::;;;,,,''''',,xkkkkl.;',xOkddolc:codolc:::;;,'.. ..........'''''....',;;:
''''''.  ..,;;,;;,,''''','okkd'.dxcox0Oxxxkd:,',:lc::;;,,'. ......',;;,,,;;,;''',;;;;
''''''''',;;;,,,,,,,'''',,:xl..,ldlOKo;,,,,'.....:o:;;,,,.. ..........''''''''...',,;
'''';;;;;;;;;;,,,,,,'''',,,d.;c:dOOXc;,'. .....':ldd;,,,'.............''.'........',;




""")


ring = (                                                                                                     
"""                                      ...,,,;;::::::::;'.                                             
                                 ..,::;;;'.''',,;;;:::cllol;.                                         
                              .:dkkkxdl,     ...'''',;;:::ccc:'                                       
                            'd0OdddddkOx;      ...',,,;;;;;::::c'                                     
                           lkc;:cc;,,',:ll'     ..',,;;;;;::::;:::.                                   
                          dl.'ll:::;,....,ol.  ...';,;;,,,;:::::;:c'                                  
                         c:.:ol::::',......:o;  ..',;::;,,,,,;:::;;c'                                 
                        .l.,l'lo:,,,'.......'dl..',;;::c::::;,;;;;;;:.                                
                        l.'loldd';;,..''''....oo.',:;;::c;;;::::;;;;;;.                               
                       ':.'ckOx:;;,'''''''...  ol'',,;;;;;;;;;;;:::;;;'.                              
                       c.'collc';;,'''.''....  .dc',:c:::;c;;;;;;;;:;;.'                              
                       c.,dolc;,::;,,,''''''    .xc,;::coc:ccc:;;;;;;;;.'                             
                      .:';dlc:,;;:;;:c:;;,:;     'x:,;:::lclc;:ccc:;;;c...                            
                      ';;;occc;cc:;;;;clodo:      :o;;collc;ol:l:::c:cl. .                            
                      ,;l.;:c,'cc:,;cc:cll:;       dl,;;;:olc::lc;;::d:,. .                           
                      ,cl.';c..::cccccc::::;       ;d:;cllcocdddxkOOOOo;. .                           
                      ,ll..:l'.;:olloolclc:;        do,;codxO000KKKK0Ox;,. .                          
                      .odclod: ..:dddddoool;.       :d;lK0KOO0k0OOOO00Olol..                          
                      .dooxdko.';:lodxkxddo;.       .x:oXxO0xkxdddkOkkkxol:.                          
                       l:xkoxx:lloxO0KKK0Ooc.        l::Oxxddoolllllooloolc'                          
                       ;,dkkxkoOO0XXXKKK00o, .       :l,OOxllc::';:llc:::c:;                          
                       .llOxdkdKXXXXXK0O00k:..       'd:OKlcc:'..;;;:cllc;;;.                         
                        o:clloolollcc::ccoxd,        .xcOk::,,.. ,;;;;;::;;;.                         
                        ,l;,c:,::;;::::c;;;;:..      .dckd:;',.. ,;;;;;;;;;;.                         
                         l;;:l:ccc:cc:l:;;;;;,.       dcxo:;,,.. ';;;;;;;;;;.                         
                         ,c;;;llcocc:ccc;;;;;;,.      o;xd:;,,.'';::::;;;;;;.                         
                          c;;,l:ccllll:;;;;;;;;,.    .l'xd:::;''.;:ccccc;,,;                          
                          .l;;locccoocl:::::;;;;:.   .c':l::::;:;;;;;::::;''                          
                           'l,:dllloollc::;:::c::c.  ;:';:c;:c::::c;,,,;:,..                          
                            :c.;d;locclllccccccc::c. o'',,,,:cc;,,,::,''';'                           
                             c:.:;'lxl:lcc::::cclccc;o.';;,,c:c,,,,',:''...                           
                              l:.cllx0dcllcc::ccccc:o;.',;,:::;,,'''''....                            
                               :: ,oxdooclcc::::cccco.',;;,:,;',,,,,'....                             
                                ,l. ;llllclcccclllcd'.''''';',''...',...                              
                                 .c:..:xlllccllllod'.',,,,;,,'.........                               
                                   ,dkxollooolclxo'''.........'''',;'                                 
                                    .,d0KOxxxx0x;.cc;,',,,;;;::ccc

""")




fail  =  ( f""" \n 

┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
""" )


# helper functions 

    # Function when it is game over
    # This function gives the player the option to replay
def failure():
    
    print('_'*80)
    print(fail)
    
    replay = input('> Do you want to play the game again? yes/no\n').lower()
    wordsFinalPattern = re.search('\w', replay)
    
    
    
    while wordsFinalPattern == None or replay == '':    
        print(
                '> Please write "yes" or "no"\n'
            )
        replay = input('> Do you want to play the game again? yes/no').lower()
        wordsFinalPattern = re.search('\w', replay)

    if replay == 'yes':
        intro()
    else:
        print(dwight)
        print('Thanks for Playing! Here is some sublime art of the best assistant to the regional manager in the paper business.')
        
    # A shorter way to press enter
def pressEnter():
    input("Press Enter to Continue...\n")

    # Typewriter effect, it is necessary to implement print(flush) in future development.
def typeWriter(text):
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    # Goblin Fight input, returns the fight option as an integer
        
def fightInput():
    '''
    This helper function includes the appropriate handling and returns the
    Fight Option as an integer
    '''
    
    fightValidOptions = ['1', '2', '3']
    
    
    fightOptions = input(genericBorderMessage (f'''
        Select any number from the fighting options:
        
         1. Use your legendary sword "Sting".
         2. Poke the goblin's eyes. 
         3. Say a mama joke to hurt the goblin's feelings. 
        ''',skipLine=True,numberOfSkippedLines=3,tripleQuoutes=True))
    
    
    while fightOptions not in fightValidOptions:
        print(
            'Please type a number according to each fighting option (1,2 or 3)'
        )
        fightOptions = input(genericBorderMessage (f'''
            Select any number from the fighting options:

             1. Use your legendary sword "Sting".
             2. Poke the goblin's eyes. 
             3. Say a mama joke to hurt the goblin's feelings. 
            ''',skipLine=True,numberOfSkippedLines=3,tripleQuoutes=True))
        
    return int(fightOptions)
    

    # Border for the fight phase. 

def borderMessageFight(msge):
    '''
    This function is not for any message!
    It's just written for the fight dialogue!
    '''
    row = int(len(msge) * 0.7 ) #/1.5
    # ''.join(['+'] + ['-' *  row * 2] + ['+'])
    verticalLine = f"+{'-' * row}+"
    horizontalLineWidth = f"{' ' * int(row * 0.13)}"
    # result= h + '\n'"|" + msg + "|"'\n' + h
    print(verticalLine+'\n' +
          '|' + 
            msge + '\t' + '|'
         '\n' + verticalLine)

    # This function creates borders based on the number of letters and skipped lines

def genericBorderMessage(msge,skipLine=False,numberOfSkippedLines=1,tripleQuoutes=False):
    
    '''
    Parameters
    ---------------------------------------------
    msge: Text to print inside the borders.
    skipLine: text to print contains \\n
    numberOfSkipepdLines: Number of skipped lines that contain text.
    tripleQuoutes: True if the string is wrapped in triple quotes eg. \''' foo \'''
    
    Details
    ----------------------------------------------
    This function is designed as a border for any message. 
    If the message has \\n please set skipLine = True. 
    Set tripleQuotes=True if the string is wrapped with \''' \'''. Implemented to 
    prevent printing 'none'. It needs to be wraped in a print function when called!
    
    Examples
    ---------------------------------------------
         # 1. Have 1 skipped line containing text
         txt1 = "Hello \\n  world."
        
        
       print( genericBorderMessage(txt1,skipLine=True,
                            numberOfSkippedLines=1,
                            tripleQuoutes=False))
                            
        # 2. Between each \\n there has no text.
         txt2 = "Hello \\n   my \\n   world."# Have 2 skipped lines containg text.
        
        print(genericBorderMessage(txt1,skipLine=True,
                            numberOfSkippedLines=2,
                            tripleQuoutes=False))
     
    '''
    
    if skipLine == False:
        row = int(len(msge)/2)
    else: 
        row = int(len(msge)/(2.5 * numberOfSkippedLines)) # 2.5 is the appropriate rate of change to fit the text
        
    verticalLine = f"+{'-' * row * 3}+"
    horizontalLineWidth = f"{' ' * row * 1}"
    
    if tripleQuoutes == True:
        return(verticalLine + 
           '\n  ' + msge +
           '\n' + verticalLine + '\n')
    else:
        print(verticalLine + 
           '\n  ' + msge +
           '\n' + verticalLine + '\n')
 

    # Function for the goblin attack
        # Depending on the smelliness of the feet, the probabiity weights will vary. 
def goblinAttack():

    if smellyFeet == 'yes':
        
        goblinAttackDamageList = [20, 30, 40]
        
        goblinAttackDamage = random.choices(goblinAttackDamageList,
                                          weights=[50, 40, 10])
        
        goblinAttackIndex = goblinAttackDamageList.index(goblinAttackDamage[0])
        
        goblinAttackMessage = ['The Goblin is afraid of your smelly feet. He throws you a rock, a tiny rock',
                             'The Goblin hates your smelly feet. He makes a fat-mom joke, it hurts you a bit',
                             'The Goblin starts to cry because of your smelly feet. It makes you feel a bit uncomfortable']
        
        return goblinAttackDamage[0], goblinAttackMessage[goblinAttackIndex]

    else:
        
        goblinAttackDamageList = [40, 50, 60]
        
        goblinAttackDamage = random.choices(goblinAttackDamageList,
                                          weights=[50, 40, 10])
        
        goblinAttackIndex = goblinAttackDamageList.index(goblinAttackDamage[0])

        goblinAttackMessage = ['The Goblin starts talking about accounting, it bores you so much that it hurts',
                               'The Goblin punches you, with a pan. It hurts a lot.',
                               'The Goblin slaps you so badly that you reconsider all your life decisions']
    
        return goblinAttackDamage[0], goblinAttackMessage[goblinAttackIndex]


#Introduction

    # The introduction to the story begins here

def intro():

    typeWriter(f"""
    
    In a hole in the ground there lived a hobbit. 
    Not a nasty, dirty, wet  hole,  filled  with  the  ends  of  worms  and  an  oozy  smell, 
    nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: 
    it was a  hobbit-hole,  and  that  means  comfort.    
    """)

    pressEnter()

    typeWriter("""
    
    This  hobbit  was  a  very  well-to-do  hobbit,  and  his  name  was Bilbo Baggins. 
    Despite he always was in his house, something happened… He suddenly disappeared! 
    """)
    
    pressEnter()

    typeWriter(f'''
    However, you are not Bilbo Baggins! You are {hobbitName}!
    ''')
    
    pressEnter()


# First Phase - Proof that you are a hobbit!

    # If the user answers yes to the adventure, the game will end. True hobbitses don't like adventures!

def firstPhase():
    
    intro()
    
    typeWriter('''
    
    Suddenly, Gandalf the maia (wizard) approaches you and starts talking to you. 
    You are confused, however you nod to everything because you don't have any idea of what is happening! 
    Suddenly, out of nowhere, Gandalf asks you:
    
    ''')
    
    adv = input(" > Would you like to have and adventure? (Yes/No) \n\n ").lower()
    phaseOneQuestions = ['yes', 'no']

    while adv not in phaseOneQuestions:
        print('please type yes or no')
        adv = input("> Would you like to have and adventure? (Yes,No) \n\n ").lower()

    # Hobbits hate adventure, if the player selects yes: automatically loose, otherwise the game continues

    if adv == 'yes':
        print(
            ' \n > A hobbit will never say that he/she loves adventures!'
        )
        failure()
    else:
        secondPhase()

# Phase 2 -  Unexpected Gathering

    # The user will only need to press enter for this section.
        # The probability depends on their sense of adventure. The higher it is,
        # the more likely to offend the party of dwarves.

def secondPhaseContext():

    typeWriter("""

    You were succesfull in convincing Gandalf that you are Bilbo!  
    """)

    pressEnter()

    typeWriter("""
    
    13 Dwarves suddenly arrive to your home:
    
    Dwalin, Balin, Kili, Fili, Dori, Nori, Ori, Oin, Gloin, Bifur, Bofur, Bombur, and Thorin.
    """)

    pressEnter()

    typeWriter("""
    
    Your are confused about what's happening, 
    you don't know who is Bilbo and don't know who this people are!
    """)

    pressEnter()

    
    typeWriter("""
    Thorin, the heir of the Lonely Mountain kingdom, explains that they need an expert burglar.
    Their home, the Lonely Mountain, was stolen by Smaug. The last great dragon of the Middle-age. 
    
    The job of this burglar is to steal an important gem from the dwarves' previous home, the Lonely mountain.
    This gem is called the Arkenstone. It is important because it is the kingdom heirloom. 
    
    Thorin and his party want to steal it in order to claim again their previous home, the Lonely Mountain.  
    
    """)

    typeWriter("""
    
    You are really nervous! You are not Bilbo but you are curious what is happening!
    Suddenly you remember your great ability in telling great jokes!
    You are going to tell one joke to be friend of the dwarves and gain their trust...
    """)

    pressEnter()


def secondPhase():

    secondPhaseContext()
    

    typeWriter(f"""
    
    Ehem, Ehem... me, {hobbitName}... BILBO I mean! I am Bilbo! 
    
    Me, Bilbo will now tell you a joke. I hope you like it!
    
    """)

    input('> Press enter to tell a joke! \n')

    jokes = {
        "jokes": [
            "what do you call a chubby dwarf?",
            "How many times does a dwarf laugh at a joke?",
            "Why are most hobbits good guys?",
            "Why Gandalf was always smoking that pipe?",
            "Why did the hobbit fall"
        ],
        "PunchLines": [
            "Low Fat!",
            "Three times: \n Once when he hears it, once when it's explained to him, and once when he gets it.",
            "Because they don't look down on people",
            "Because he had a bad Hobbit!", "He had a Frodoian slip"
        ]
    }

    if adventureSense >= 2:

        jokeList = random.choices([0, 1, 2, 3], weights=[40, 40, 10, 10])
        jokeNumber = jokeList[0]

        print(jokes['jokes'][jokeNumber])

        pressEnter()

        print(jokes['PunchLines'][jokeNumber])

    else:

        jokeList = random.choices([0, 1, 2, 3], weights=[10, 10, 40, 40])
        jokeNumber = jokeList[0]

        print(jokes['jokes'][jokeNumber], "\n")

        pressEnter()

        print(jokes['PunchLines'][jokeNumber], "\n")

    if jokeNumber <= 1:

        print(f""" 
        \n > Because you said that your adventure level is {adventureSense}, you risked it and offended the dwarves!
        The Dwarves tie you to a column and leave your house with all your groceries
        
        """)
        failure()

    else:
        print("""
        
       > Congrats! Your joke was enough to entertain the dwarves and gain a bit of their trust!! 
        
        """)

        pressEnter()

        # CHECK AGAIN THE STORY OF THE HOBBIT!!!!!
        type(f"""
        
        Thanks to your natural abilities to gain trust from others, the dwarves hand you a contract. 
        This contract is to go to smokey mountain and rob the blabla
        
        """)

        thirdPhase()


# Phase 3 - Goblin fight

    # Player health and goblin are tracked as global variables. 
        # The probabilities will vary according the smelliness of feet. 
        # If the player only flees there is small likelyhood to pass to the next phase
        # fleeing ultimately will be game over.
        # The best way to win is fighting with option 1 (stinger). 

def thirdPhase():
    
    global goblinLifePoints
    global playerLifePoints
    
    # Third Phase Context
    typeWriter('''
        
        You start your journey with the Dwarves! 
        
        After surviving a battle with trolls, 
            receiveng help from Rivendell's elves, 
            and surviving a giant stone storm...
            
        You suddenly arrive to a giant goblin's cave!
        
        ''')

    #     Local variables are set for the fight!
    decisionOptions = ['flee', 'fight']

    # The player needs to decide if he/she is going to flee or fight
    decision = input(
        'You encounter a Goblin! What do you want to do? (flee or fight) \n').lower()

    # Error handling for the previous user input
    while decision not in decisionOptions:
        print('Please type "Flee" or "Fight"')
        decision = input(
            f'You encounter a Goblin! What do you want to do? (flee or fight) \n '
        ).lower()

    # Fight begins here. If the player stated that had smelly feet, 
     # they will have a higher probability
        # to survive the fight
    
    # Fight and Smelly Feet
    
    if decision == 'fight' and smellyFeet == 'yes':

        print('''
        
        You decided to fight against a random Goblin! \n
        Thanks to your smelly feet, you will inflict extra damage to the Goblin!
        
        ''')

        while goblinLifePoints > 0:
            
            pressEnter()
            
            playerLifePoints = playerLifePoints - goblinAttack()[0]
            
            genericBorderMessage(
                '> {} \n > You lost {}% life points \n > You now have {}% life points'
                .format(goblinAttack()[1],
                        goblinAttack()[0], playerLifePoints),
                skipLine=True,numberOfSkippedLines=2)
            
            if playerLifePoints < 0:
                break
            else:
            
                pressEnter()

                fightSelected = fightInput()

                pressEnter()

                if fightSelected == 1:
                    damageList = [50, 60, 70]
                    damageToInflict = random.choices(damageList,
                                                     weights=[50, 40, 10])
                    goblinLifePoints = goblinLifePoints - damageToInflict[0]
                    genericBorderMessage(
                    f' > You inflicted {damageToInflict[0]}% damage \n > The goblin has {goblinLifePoints}% life points',
                                        skipLine=True,
                                        numberOfSkippedLines=2
                                    )

                elif fightSelected == 2:
                    damageList = [40, 50, 60]
                    damageToInflict = random.choices(damageList,
                                                     weights=[50, 40, 10])
                    goblinLifePoints = goblinLifePoints - damageToInflict[0]
                    genericBorderMessage(
                    f' > You inflicted {damageToInflict[0]}% damage \n > The goblin has {goblinLifePoints}% life points',
                                        skipLine=True,
                                        numberOfSkippedLines=2
                                    )

                else:
                    damageList = [30, 60, 50]
                    damageToInflict = random.choices(damageList,
                                                     weights=[50, 40, 10])
                    goblinLifePoints = goblinLifePoints - damageToInflict[0]
                    genericBorderMessage(
                    f' > You inflicted {damageToInflict[0]}% damage \n > The goblin has {goblinLifePoints}% life points',
                                        skipLine=True,
                                        numberOfSkippedLines=2
                                    )
                
                
        if goblinLifePoints <= 0:
            genericBorderMessage('You killed the Goblin!')
            fourthPhase()
        else:
            print("THE GOBLIN KILLED YOU")
            failure()

    # Fight and no smelly feet
    elif decision == 'fight' and smellyFeet == 'no':

        print('''
        
        You decided to fight against a random Goblin! \n
        Because you don't have smelly feet, you will not inflinge extra damage!
        
        ''')

        
        while goblinLifePoints > 0: 
            
            playerLifePoints = playerLifePoints - goblinAttack()[0]

            pressEnter()
            
            genericBorderMessage(
                '> {} \n > You lost {}% life points \n > You now have {}% life points'
                .format(goblinAttack()[1],
                        goblinAttack()[0], playerLifePoints),
                skipLine=True,numberOfSkippedLines=2)
            
            
            if playerLifePoints < 0:
                break
                
            else:
            
                pressEnter()

                fightSelected = fightInput()

                pressEnter()


                if fightSelected == 1:
                    damageList = [40, 50, 60]
                    damageToInflict = random.choices(damageList,
                                                     weights=[50, 40, 10])
                    goblinLifePoints = goblinLifePoints - damageToInflict[0]
                    genericBorderMessage(
                    f' > You inflicted {damageToInflict[0]}% damage \n > The goblin has {goblinLifePoints}% life points',
                                        skipLine=True,
                                        numberOfSkippedLines=2
                                    )

                elif fightSelected == 2:
                    damageList = [30, 40, 50]
                    damageToInflict = random.choices(damageList,
                                                     weights=[50, 40, 10])
                    goblinLifePoints = goblinLifePoints - damageToInflict[0]
                    genericBorderMessage(
                    f' > You inflicted {damageToInflict[0]}% damage \n > The goblin has {goblinLifePoints}% life points',
                                        skipLine=True,
                                        numberOfSkippedLines=2
                                    )

                else:
                    damageList = [20, 30, 40]
                    damageToInflict = random.choices(damageList,
                                                     weights=[50, 40, 10])
                    goblinLifePoints = goblinLifePoints - damageToInflict[0]
                    genericBorderMessage(
                    f' > You inflicted {damageToInflict[0]}% damage \n > The goblin has {goblinLifePoints}% life points',
                                        skipLine=True,
                                        numberOfSkippedLines=2
                                    )
            
            
        if goblinLifePoints <= 0:
            genericBorderMessage('You killed the Goblin!')
            fourthPhase()
        else:
            print("THE GOBLIN KILLED YOU")
            failure()

    # Flee and Smelly Feet
    elif decision == 'flee' and smellyFeet == 'yes':
        
        print('''
            > You decided to run! 
            > No one wants to attack you because of your smelly feet!
            ''')
    
        fleeListOptions = [0,1,2]
    
        fleeOutput = random.choices(fleeListOptions,weights=[50,40,10])
    
        if fleeOutput[0] == 0:
        
            print('You regret running, you want to fight!')
        
            thirdPhase()
    
        elif fleeOutput[0] == 1:
            print('You run and suddenly fall into a hole!')

            fourthPhase()

        else: 

            print('''
            > You fall and lose consciousness!
            > When you open your eyes you are in a big cauldron.
            > The Goblins will have Hobbit for dinner!
            ''')

            failure()
    
    # Flee and no Smelly feet
    elif decision == 'flee' and smellyFeet == 'no':
    
            print('''
                    > You decided to run! 
                    > No matter where you go you are attacked by Goblins!
                    ''')


            playerLifePoints = playerLifePoints - goblinAttack()[0]

            genericBorderMessage(
                            '> {} \n > You lost {}% life points \n > You now have {}% life points'
                            .format(goblinAttack()[1],
                                    goblinAttack()[0], playerLifePoints),
                            skipLine=True,numberOfSkippedLines=2)
                
            if playerLifePoints > 0:
                    
                
                    thirdPhase()

            
            else:
                print("THE GOBLIN KILLED YOU")
                
                failure()

            
# Fourth Phase - Gollum's riddles

    # The user needs to correctly answer 2 out of 4 riddles in order to win the game. 

def fourthPhase():
    typeWriter('''
    You suddenly fall through a hole.
    
    When you open your eyes, you wonder where you are. 
    No one is anywhere near you. 
    You cannot hear or see anything. 
    You feel nothing except the stone of the floor.
    
    Deep down here by the dark water lived old Gollum, a small slimy creature.
    He was Gollum -- as dark as darkness, except for two big round pale eyes in his thin face.
    
    Suddenly Gollum sees you.
    He says: 
    - "What iss he, my preciouss?"
    - "Praps ye sits here and chats with it a bitsy, my preciousss. It like riddles, praps it does, does it?
    
    Gollum challenges you to a riddle competition, if you answer correctly 2 riddles he will not eat you!
    If you fail to correctly answer 3 times you will lose and Gollum will eat you!
    
    ''')



    riddles = [
        ' What has roots as nobody sees, Is taller than trees, Up, up it goes, And yet never grows?',
        ' Voiceless it cries, Wingless flutters, Toothless bites, Mouthless mutters.',
        ''' It cannot be seen, cannot be felt, Cannot be heard, cannot be smelt. 
                    It lies behind stars and under hills, And empty holes it fills.
                    It comes first and follows after,Ends life, kills laughter.''',
        ' Alive without breath, As cold as death; Never thirsty, ever drinking, All in mail never clinking.',
        ''' This thing all things devours: Birds, beasts, trees, flowers;
                    Gnaws iron, bites steel;
                    Grinds hard stones to meal;
                    Slays king, ruins town,
                    And beats high mountain down.'''
    ]

    answers = ['Mountains', 'Wind', 'Darkness', 'Fish', 'Time']

    answersOptions = [
        '1. Forests \n 2. Big Data \n 3. Mountains',
        '1. Blockchain \n 2. Boston\'s Winter \n 3. Wind',
        '1. Oxygen \n 2. Dark \n 3. Cats', '1. Ice \n 2. Fire \n 3. Fish',
        '1. Hungry People \n 2. Time \n 3. Artificial Intelligence'
    ]
    
    solutionsList = [3, 3, 2, 3, 2]
    riddlesIndexList = [0, 1, 2, 3, 4]

    answerCount = 2
    askedQuestionsNumber = 5

    while askedQuestionsNumber > 0:

        # Error Handling
        randomIndex = random.choice(riddlesIndexList)
        riddlesIndexList.remove(randomIndex)

        
        if randomIndex == 0 or randomIndex == 1 or randomIndex == 3:
        
            print(genericBorderMessage(f'> Gollum asks you: \n\n {riddles[randomIndex]}\n',
                                      tripleQuoutes=True,skipLine=True))
            
        else:
             print(genericBorderMessage(f'> Gollum asks you: \n\n {riddles[randomIndex]}\n',
                                      tripleQuoutes=True,skipLine=True,numberOfSkippedLines=3))
            
        # answer error handling 
        answerErrorHandlingList = ['1', '2', '3']
            
            
        userAnswer = input(
            f'Please Select one of the following answers: \n {answersOptions[randomIndex]} \n'
        )

        
        while userAnswer not in answerErrorHandlingList:
            print(' \n Please type a number (e.g. 1)')
            userAnswer = input(
                f'Please Select one of the following answers: \n {answersOptions[randomIndex]} \n'
            )

       #  Answer logic
            
            #Wrong answer
        if userAnswer != str(solutionsList[randomIndex]): #solutionsList:
        
            if askedQuestionsNumber - answerCount < 1:
                break
            
            else:
                print(genericBorderMessage(
                    f'\nWrong answer! You need to respond correctly {answerCount} out of {askedQuestionsNumber-1} questions\n',
                    skipLine = True, tripleQuoutes = True )
                )
                
            # Correct answer
        elif userAnswer == str(solutionsList[randomIndex]):#in solutionsList:

            answerCount = answerCount - 1

            if answerCount != 0:
                print(genericBorderMessage(
                    f'\n Congrats! You need to answer {answerCount} more question to win the ring to rule them all! \n',
                    skipLine = True, tripleQuoutes = True)
                )
            else:
                
                break

        else:
            print('AN ERROR OCCUR, CONTACT GANDALF')

        askedQuestionsNumber = askedQuestionsNumber - 1

    if answerCount == 0:
        typeWriter('''
        You Win!
        
        Gollum goes away.
        
        Not far from gollum's place, you find one very beautiful thing, very
        beautiful, very wonderful. He had a ring, a golden ring, a precious ring...
        
        ''')
        
        print(ring)
    
    else:
        print('\n YOU FAILED, GOLLUM WILL HAVE A NICE DINNER!')
        failure()



adventureSense = adventureSenseInput()
hobbitName = hobbitNameInput()
smellyFeet = smellyFeet()

firstPhase()
import time as t
import webbrowser as wb
import pyautogui as pg
points = 0
show = pg.prompt ("What is your favorite TV show? ")

if show == "Minecraft Lets Play":
    pg.alert ("OMG lol xD :P thats my fav show too")
    points += 69
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=uilHIYY2p1Q")
elif show == "The Office":
    pg.alert ("-100 ur normie")
    points += -100
elif show == "The Secret Life of Pets":
    pg.alert ("That is so for the memes")
    points += 69
    wb.open("https://www.youtube.com/watch?v=63thpSIHEBQ")
elif show == "Greys Anatomy":
    pg.alert ("That shows sounds good but gross ;P")
    points += 1
elif show == "Family Guy":
    pg.alert ("Such memeeemes:}:}:}:}:}::}:}")
    points += 23.2345
elif show == "Big Mouth":
    pg.alert ("pUbErTy iS fUnn")
    points += -420
else:
    pg.alert ("Naw the best is Minecraft Lets Play you are uncultured")
    points += -5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=ViImRYlarcM")
           

fortnite = pg.prompt ("What is your favorite fortnite skin? ")

if fortnite == "Crackshot":
    pg.alert ("Omegalul I have that skin memes")
    points += 6.7
    wb.open ("https://www.youtube.com/watch?v=8dEoRwDdLug")
elif fortnite == "Skull Trooper":
    pg.alert ("Skull trooper came back so u are have big normie")
    points += -100
    wb.open ("https://www.youtube.com/watch?v=bOM97DPsrgY")
elif fortnite == "Renegade Raider":
    pg.alert ("OMG do you now stud zoom?")
    points += 20
    wb.open ("https://www.youtube.com/watch?v=HVQp8WC_9z0")
elif fortnite == "Default":
    pg.alert ("Tfue is a god church according to Jake pall")
    points += 1000
    wb.open ("https://www.youtube.com/watch?v=uhuxVFktLk4")
elif fortnite == "Dark Voyager":
    pg.alert ("DARK'T Vangaurdn't")
    points += 261.2352
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=uilHIYY2p1Q")
elif fortnite == "Ginger Gunner":
    pg.alert ("STUD QINOMOIUA")
    points += 54.463
else:
    pg.alert ("Skull trppoer is coming back :P :D :O :B :S :X")
    wb.open ("https://www.youtube.com/watch?v=bLd-bSGUjrw")
shoes = pg.prompt ("What is your favorite type of shoe? ")

if shoes == "Yeezys":
    pg.alert ("Those r kewl")
    points+= 17
    wb.open ("https://www.youtube.com/watch?v=90SlJnXT2HQ")
elif shoes == "Ultra Boosts":
    pg.alert ("kewl kat those are good shoes")
    points += 23
    wb.open ("https://www.youtube.com/watch?v=y98De45A94Y")
elif shoes == "Nike":
    pg.alert ("Okay colin")
    points += 76
    wb.open ("https://www.youtube.com/watch?v=Qw1c_bEjKIw")
elif shoes == "Brooks":
    pg.alert ("Okay big man woohoo briggs")
    points += 10000
elif shoes == "Reebok":
    pg.alert ("Silly geezer")
    points += 23.2351
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=eN7dYDYfvVg")
elif shoes == "Vans":
    pg.alert ("nOrMiE")
    points += 10000
else:
    pg.alert ("Peppa PIG")
    points += 13.8
    wb.open ("https://www.youtube.com/watch?v=d66otUvnLzM")
Movies = pg.prompt ("What is your favorite movie? ")

if Movies == "Grownups":
    pg.alert ("kewl")
    points+= 17
elif Movies == "Fortnite the TV show":
    pg.alert ("memes")
    points += 23
elif Movies == "Avatar":
    pg.alert ("Okay colin")
    points += 76
elif Movies == "The God Father":
    pg.alert ("Solid")
    points += 10000
elif Movies == "Dispicable Me":
    pg.alert ("Minion MOlly")
    points += 10
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=ityVW2gR0Rs")
elif Movies == "The Smurfs Go to New York":
    pg.alert ("How bout lithuania")
    points += 100000
else:
    pg.alert ("<-\_({*#*})_/->")
    points += 13.8
    wb.open ("https://www.youtube.com/watch?v=uilHIYY2p1Q")
dance = pg.prompt ("What is your favorite fortnite dance? ")

if dance == "Infinite Dab Emote":
    pg.alert ("LOLOLOLOLOLOLOLOL")
    points += 6.7
    wb.open ("https://www.youtube.com/watch?v=8dEoRwDdLug")
elif dance == "The Worm":
    pg.alert ("KITKAT")
    points += -100
    wb.open ("https://www.youtube.com/watch?v=bOM97DPsrgY")
elif dance == "Take the L":
    pg.alert ("sEaSoN 3")
    points += 20
    wb.open ("https://www.youtube.com/watch?v=HVQp8WC_9z0")
elif dance == "Dance Moves":
    pg.alert ("bAsS BOOSTE")
    points += 1000
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=uhuxVFktLk4")
elif dance == "Floss":
    pg.alert ("Cleveland Brown")
    points += 261.2352
    wb.open ("https://www.youtube.com/watch?v=uilHIYY2p1Q")
elif dance == "T-Pose":
    pg.alert ("Head up, Chin Straight")
    points += 54.463
else:
    pg.alert ("the best fortnitete dance is me")
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=bLd-bSGUjrw")
pg.alert ("your final score is " + str(points))

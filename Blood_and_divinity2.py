from random import *
from Sprite import *
from time import *
#---------------------- ^^ Importing random and sprites from seperate program, aswell as functions and classes.

Real_Cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
P1_Hand = [12]
P1_Hold = []
P2_Hand = []
P2_Hold = []
#---------------------- ^^ The lists for cards and such aswell as the imports.

P1Pop = 4000
P1Power = 3
P1Monster = 1
P1Hero = 2
P1Relic = 1
P1Realm = 0
P1Turn = True
P1PonderStatus = False
P1Seduce = False
P1Followgain = False
P1Followincrease = 0
P1Lethality = False
P1Seducetime = 0
P1Extradmg = 0
P1ActionDull = False
P1ActionSurge = False
P1SurgeTime = 0
#------------------------ ^^The values for P1
P2Pop = 4000
P2Power = 3
P2Monster = 3  
P2Hero = 1
P2Relic = 2
P2Realm = 0
P2Turn = False
P2PonderStatus = False
P2Seduce = False
P2Followgain = False
P2Followincrease = 0
P2Lethality = False
P2Seducetime = 0
P2Extradmg = 0
P2ActionDull = False
P2ActionSurge = False
P2SurgeTime = 0
#----------------------- ^^The values for P2
TurnsMade = 1
#-----------------------^^ Universal values
GameRun = True
Gamecondition = False

MaxTurn = int(input("How many turns do you want there to be?: "))
while Gamecondition == False:
    if MaxTurn <= 5:
        verify = str(input("Are you sure?: (Y/N) ").upper())
        if MaxTurn <= 0:
            print("Invalid number")
            MaxTurn = int(input("How many turns do you want there to be?: "))
        elif 'Y' in verify and MaxTurn > 0:
            Gamecondition = True   
        else:
            MaxTurn = int(input("How many turns do you want there to be?: "))

    elif MaxTurn >= 50:
        verify = str(input("Are you sure?: (Y/N) ").upper())
        if 'Y' in verify:
            Gamecondition = True
        else:
            MaxTurn = int(input("How many turns do you want there to be?: "))
            
    else:
        Gamecondition = True
#--------------------------------- ^^ Establishes the amount of turns and sets loop conditions.
while GameRun == True:
    if P1Turn == True:
#---------------------------------
        P1Action = 6
        if P1ActionSurge == True:
            P1Action = ActionSurge(P1Action,2)
            P1SurgeTime =- 1
            if P1SurgeTime == 0:
                print("You no longer are action surged.")
        if P1ActionDull == True:
            P1Action = ActionSabotage(P1Action,2)
            P1DullTime =- 1
            if P1DullTime == 0:
                P1ActionDull = False
                print("Your action points are no longer hindered.")
#---------------------------------
        if P1PonderStatus == True:
            P1CardGain = P1CardGain
            P1PonderStatus = False
            P1PonderStatus = False
        elif P1PonderStatus == False:
             P1CardGain = 4 #Cards gained for a turn   
#---------------------------------
        if P1Seduce == True:
            print("You have",P1Seducetime,"turns left of control mind")
        if P1Followgain == True:
            print("You have", P1Followtime,"turns left of passive follower gain")
            
#--------------------------------- ^^ The conditions that are set at the start of every full turn.
    for i in range(P1CardGain):
        CardChosen = randint(1,25)
        if CardChosen in P1_Hand or CardChosen in P1_Hold:
            while CardChosen in P1_Hand or CardChosen in P1_Hold:
                CardChosen = randint(1,25)
        P1_Hand.append(CardChosen)
        P1_Hand.sort()  
        
    if len(P1_Hold) > 0:
        Held = P1_Hold[0]
        P1_Hand.append(Held)
        P1_Hold = []
        print("No longer holding any card")
#---------------------------------- ^^ Getting new unique cards.
    while P1Turn == True:
        P1Menu = Menu(P1Pop,P1Power,P1Action,P1Monster,P1Hero,P1Relic,P1Realm,MaxTurn,TurnsMade)
        P1Menu.ShowMenu()
        P1Choice = P1Menu.ReturnOption()
        if P1Choice == '1':
            P1Menu.ShowCards(P1_Hand) #Shows avaliable cards (See Sprite.py)
            P1Card = P1Menu.CardChoice(Real_Cards) #Offers choice and stores it (See Sprite.py)
            
            if P1Card == 1:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,2): #Current card, Player hand, Action, Power, Pop, Relic, action requirement, power requirement etc.
                    P1Action -= 2
                    event = randint(1,5)
                    if event == 1:
                        print("A grandous monument has risen, giving 250 Followers.")
                        P1Pop = Seduce(P1Pop,P1Seduce,250)
                    if event == 2:
                        print("Your monument has turned out worse than expected, giving 150 Followers ")
                        P1Pop = Seduce(P1Pop,P1Seduce,150) 
                    if event == 3:
                        print("Your monument is even more grand than planned! Giving 400 Followers!")
                        P1Pop = Seduce(P1Pop,P1Seduce,400)
                    if event == 4:
                        print("Your monument has risen, but it along side the followers... You gain a Hero! Giving 250 Followers and 1 Hero")
                        P1Pop = Seduce(P1Pop,P1Seduce,250)
                    if event == 5:
                        print("Your monument has risen, but it along side the followers... You gain a Relic! Giving 250 Followers and 1 Relic")
                        P1pop = Seduce(P1Pop,P1Seduce,250)
                        P1Relic += 1
            if P1Card == 2:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,2):
                    P1Action -= 2
                    event = randint(1,4)
                    if event == 1:
                        print("You tamed a fierce beast, giving 1 monster")
                        P1Monster += 1
                    if event == 2:
                        print("The beast outsmarted you... somehow. Nothing was gained")
                    if event == 3:
                        print("The beast turns out to be worshipped by a small tribe, giving +1 Monster and 200 Followers")
                        P1Monster += 1
                        P1Pop = Seduce(P1Pop,P1Seduce,200)
                    if event == 4:
                        print("You tamed two fierce beasts! Giving 2 monsters")
                        P1Monster += 2
            if P1Card == 3:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,2):
                    P1Action -= 2
                    event = randint(1,4)
                    if event == 1:
                        print("You venerate a former general, bringing his loyal followers along with him. Gaining +1 Hero and 200 Followers")
                        P1Pop = Seduce(P1Pop,P1Seduce,200)
                        P1Hero += 1
                    if event == 2:
                        print("You venerated twins! Gaining +2 Heroes")
                        P1Hero += 2
                    if event == 3:
                        print("You venerate a peasant, but he fails to show up.")
                    if event == 4:
                        print("You venerate a peseant, turning them into a might hero. Gaining +1 Hero")
                        P1Hero += 1
            if P1Card == 4:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,3):
                    P1Action -= 3
                    event = randint(1,3)
                    if event == 1:
                        print("You successfully control the mind of a mortal, the effect will last 3 turns")
                        P1Seduce = True
                        P1Seducetime = 3
                    if event == 2:
                        print("You failed to control the mind of a mortal.")
                    if event == 3:
                        print("You succeeded, but you the event also gathered followers + 200 Followers. The effect will last 4 turns")
                        P1Seduce = True
                        P1Seducetime = 4
                        P1Pop = P1Pop + (200*2)
                        print("Followers have been doubled, due to -Control Mortal-")
            if P1Card == 5:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,2):
                    P1Action -= 2
                    event = randint(1,4)
                    if event == 1:
                        print("You have recreated a sacred relic that poeple worship. Gaining +200 Followers and 1 relic")
                        P1Pop = Seduce(P1Pop,P1Seduce,200)
                        P1Relic += 1
                    if event == 2:
                        print("In passion, you've made 2 relics! Gaining +2 Relics")
                        P1Relic += 2
                    if event == 3:
                        print("Your new relic crumbles due to poor design.")
                    if event == 4:
                        print("You've created a new relic! Granting +1 Relic")
                        P1Relic += 1
            if P1Card == 6:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,4,1):
                    P1Action -= 4
                    P1Power -= 1
                    event = randint(1,4)
                    if event == 1:
                        print("You help a minor god by getting them ore followers. In return you recieve some relics as payment. +2 Relics")
                        P1Relic += 2
                    if event == 2:
                        print("You help a minor god in a fight. Rewarding you some followers for your valor. +250 Followers")
                        P1Pop = Seduce(P1Pop,P1Seduce,250)
                    if event == 3:
                        print("After helpong a minor god, they reveal themselves to be a major god. You gain +2 on all resources and 300 followers")
                        P1Relic += 2
                        P1Hero += 2
                        P1Monster += 2
                        P1Pop = Seduce(P1Pop,P1Seduce,300)
                    if event == 4:
                        print("You help a minor god, gaining some of their sacred beasts. +2 Monsters")  
                        P1Monster += 2
            if P1Card == 7:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,5):
                    P1Action -= 4
                    P1Power -= 1
                    event = randint(1,5)
                    if event == 1:
                        print("You have done all thirteen herculean deeds in one day, everyone is very impressed. +850 Followers")
                        P1Pop = Seduce(P1Pop,P1Seduce,850)
                    if event == 2:
                        print("You have granted a mortal your aid, hopefully not making another kratos. +850 Followers")
                        P1Pop = Seduce(P1Pop,P1Seduce,850)
                    if event == 3:
                        print("You've made yourself a giant pyramid made of pure gold +850 Followers")
                        P1Pop = Seduce(P1Pop,P1Seduce,850)
                    if event == 4:
                        print("You did a backflip +850 Followers")
                        P1Pop = Seduce(P1Pop,P1Seduce,850)
                    if event == 5:
                        print("You craft a legendary weapon, which impressed all +850 Followers and +1 Relic")
                        P1Pop = Seduce(P1Pop,P1Seduce,850)
                        P1Relic += 1
            if P1Card == 8:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,5):
                    P1Action -= 5
                    event = randint(1,3)
                    if event == 1:
                        print("You grant a few wishes for you followers, gaining +50 Followers per turn")
                        P1Followgain = True
                        P1Followincrease += 50
                        P1Followtime = 5
                    if event == 2:
                        print("You help many villages, gaining +100 Followers per turn")
                        P1Followgain = True
                        P1Followincrease += 100
                        P1Followtime = 5
                    if event == 3:
                        print("You lead a successful crusade, gaining +150 Followers per turn")
                        P1Followgain = True
                        P1Followincrease += 150
                        P1Followtime = 5
            if P1Card == 9:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,2):
                    P1Action -= 2
                    event = randint(1,100)
                    if event == 1:
                        print("Your assault is less effective than usual, -100 followers to enemy")
                        P2Pop = Lethality(P2Pop,P1Lethality,P1Extradmg,100)
                    if event == 2:
                        print("Your assault has lead to wipe a majority of enemy forces, -300 followers to enemy")
                        P2Pop = Lethality(P2Pop,P1Lethality,P1Extradmg,300)
                    if event >= 3 and event <= 99:
                        print("Your assault is successful, -150 followers to enemy")
                        P2Pop = Lethality(P2Pop,P1Lethality,P1Extradmg,150)
                    if event == 100:
                        print("You have completely annilihated all of your enemies followers, -ALL ENEMY FOLLOWERS AND -500")
                        if P2Pop < 0:
                            P2Pop = Lethality(P2Pop,P1Lethality,P1Extradmg,(P2Pop - P2Pop)-500)
                        else: 
                            P2Pop =- P2Pop - 500
            if P1Card == 10:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,2,1):
                    P1Lethality = True
                    P1Action -= 2
                    P1Power -= 1
                    event = randint(1,3)
                    if event == 1:
                        P1Extradmg += 100
                        print("You prepare you armaments, giving +100 extra dmg against opponent")
                    if event == 2:
                        P1Extradmg += 200
                        print("You efficiently prepare your armaments, giving +200 extra dmg against opponent")
                    if event == 3:
                        P1Extradmg += 85
                        print("You manage scraps and add them to your armaments, giving +85 extra dmg against opponent")
        
            if P1Card == 11:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,5):
                    P1Action -= 2
                    event = randint(1,3)
                    if event == 1:
                        P2DullTime = 3
                        P2ActionDull = True
                        print("For three turns, your opponent has 2 less action points.")
                    if event == 2:
                        P2Pop = Lethality(P2Pop,P1Lethality,P1Extradmg,150)
                        P2Relic =- 2
                        print("The gods personally pillage your opponent and steal 2 Relics and kill 200 of their followers")
                    if event == 3:
                        P1DullTime = 2
                        P1ActionDull = True
                        print("Turns out the gods didn't belive you, and now you have 2 less action points for two turns")
                    
            if P1Card == 12:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,3):
                    P1Action -= 3
                    print("You stir chaos:")
                    event = randint(1,6)
                    event2 = randint(1,6)
                    if event == 1:
                        P1Pop += 200
                        print("You gain 200 followers ",end="")
                    if event == 2:
                        P1Pop -= 200
                        print("You lose 200 followers ",end="")
                    if event == 3:
                        P1Relic += 2
                        print("You gain 2 relics ",end="")
                    if event == 4:
                        P1Relic -= 2
                        print("You lose 2 relics ",end="")
                    if event == 5:
                        P1Hero += 1
                        P1Monster += 1
                        print("You gain a monster and a hero ",end="")
                    if event == 6:
                        P1Hero -= 1
                        P1Hero -= 1
                        print("You lose a hero and a monster ",end="")
                        
                    if event2 == 1:
                        P1Power += 2
                        print("and you gain 2 power points.")
                    if event2 == 2:
                        P1Power -= 2
                        print("but also lose 2 power.")
                    if event2 == 3:
                        print("and also you feel fatigue (-2 action points for 2 turns)")
                        P1DullTime = 2
                        P1ActionDull = True
                    if event2 == 4:
                        P1ActionSurge = True
                        P1SurgeTime = 2
                        print("and you feel a sudden surge of energy! (+2 action points for 2 turns)")
                    if event2 == 5:
                        P1Action += 3
                        print("and you gain the action points back!")
                    if event2 == 6:
                        print("and you lose 3 further action points.")
                        if P1Action - 3 < 0:
                            P1Action = 0
                        else:
                            P1Action -= 3
                               
            if P1Card == 13:
                if P1Menu.CardCheck(P1Card,P1_Hand,P1Action,P1Power,P1Pop,P1Relic,2):
                    P1Action -= 2
                    event = randint(1,5)
                    print("You kill 200 of the opponent's followers ",end="")
                    P2Pop = Lethality (P2Pop,P1Lethality,P1Extradmg,200)
                    if event == 1:
                        print(".")
                    if event == 2:
                        if P2Relic >= 2:
                            print("and you manage to take two enemy relics too.")
                            P2Relic -= 2
                            P1Relic += 2
                        else:
                            print("aswell as mishmashing stuff into one relic.")
                            P1Relic += 1
                    if event == 3:
                        print("aswell as capturing 150 more of their followers")
                        P2Pop -= 150
                        P1Pop += 150
                    if event == 4:
                        print("but lose 50 of your own in the battle.")
                        P1Pop -= 50
                    if event == 5:
                        print("but it takes a little bit more ffort than usual.")
                        P1Action -= 1
                        
        if P1Choice == '2':
            P1Menu.SpecMenu()
            P1Choice = P1Menu.ReturnOption()
            if P1Choice == '1':
                if P1Menu.Ponderstatus(P1Action):
                    P1Action -= 2
                    P1PonderStatus = True
                    P1CardGain += 1
            
            if P1Choice == '2':
                if P1Menu.Sacrifice(P1Action,P1Pop):
                    P1Action -= 1
                    P1Pop -= 200
                    P1Power += 1
                
            if P1Choice == '3':
                P1Choice = 0
                if P1Menu.Hold(P1Action,P1_Hand,P1_Hold):
                    print("Holding card",P1_Hold[0])
                    P1Action -= 1

        if P1Choice == "3":
            P1Turn = False
            P2Turn = True
            P1_Hand = []
            

    if P2Turn == True:
        P2Turn = False
        P1Turn = True
        TurnsMade += 1
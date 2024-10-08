class Menu():
    
    def __init__(self,pop,power,action,monster,hero,relic,realm,max_turn,turn_done):
        self.pop = pop
        self.power = power
        self.action = action
        self. monster = monster
        self.hero = hero
        self.relic = relic
        self.realm = realm
        self.max_turn = max_turn
        self.turns = turn_done
    
    def ShowMenu(self):
        print("█████████████████████████████████████████")
        print("██                                     ██ Popularity/Followers:",self.pop,"")
        print("██      ▪1(Play Cards)                 ██ Power Points:",self.power,"")
        print("██                                     ██ Action Points:",self.action,"     Realms:",self.realm,"")
        print("██      ▪2(Ponder / Sacrifice)         ██ Monsters:",self.monster,"          Turns left:",(self.max_turn - self.turns),"")
        print("██                                     ██ Heroes:",self.hero,"")
        print("██      ▪3(End your turn)              ██ Relics:",self.relic,"")
        print("██                                     ██ Turn:",self.turns,"")
        print("█████████████████████████████████████████")
    
    def ReturnOption(self):
        Choice = input("What is your choice?: ")
        return Choice      

    def ShowCards(self,card_in):
        for card in card_in:
            if 1 == card:
                Card1()

            if 2 == card:
                Card2()
            
            if 3 == card:
                Card3()
            
            if 4 == card:
                Card4()
            
            if 5 == card:
                Card5()
            
            if 6 == card:
                Card6()
                
            if 7 == card:
                Card7()
            
            if 8 == card:
                Card8()
            
            if 9 == card:
                Card9()
            
            if 10 == card:
                Card10()
            
            if 11 == card:
                Card11()
            
            if 12 == card:
                Card12()
        
            if 13 == card:
                Card13()
            
            if 14 == card:
                Card14()
            
            if 15 == card:
               Card15()
            
            if 16 == card:
                Card16()
            
            if 17 == card:
                Card17()
            
            if 18 == card:
                Card18()
            
            if 19 == card:
                Card19()
            
            if 20 == card:
                Card20()
            
            if 21 == card:
                Card21()
            
            if 22 == card:
                Card22()
            
            if 23 == card:
                Card23()
            
            if 24 == card:
                Card24()
            
            if 25 == card:
                Card25()
    
    def CardChoice(self,real_cards):
        Validity = False
        while Validity == False:
            print("If you want to go back press 0")
            CardPlay = input("Choose Card ID to play: ")
            if CardPlay in str(real_cards):
                CardPlay = int(CardPlay)
                return CardPlay
                Validity = True
            if CardPlay == '0':
                break
        else:
            print("Invalid")

    def CardCheck(self,p_card = 0,p_hand = 0,action_in = 0,power_in = 0,pop_in = 0,relic_in = 0,action_req = 0, power_req = 0, pop_req = 0, relic_req = 0): #Fill in criteria as if they were the requirement.
        cardcheck = False
        actioncheck = False
        powcheck = False
        popcheck = False
        relcheck = False
        if p_card in p_hand:  #Checks if play is even legal
            cardcheck = True
            if action_in >= action_req:
                actioncheck = True
                if power_in >= power_req:
                    powcheck = True
                    if pop_in >= pop_req:
                        popcheck = True
                        if relic_in >= relic_req:  #Note to self: Keep the pattern up if you decide to add more card thresholds.
                            relcheck = True
                        else:
                            print("You don't have the required relics.") #Error messages
                    else:
                        print("You don't have the required population.")
                else:
                    print("You dont have the required power.")
            else:
                print("You dont have the required action points.")
        else:
            print(p_card,"is not in your hand deck.")
        
        if cardcheck == True and actioncheck == True and powcheck == True and popcheck == True and relcheck == True: #If all thresholds pass then the card is avaliable to play
            return True

    def SpecMenu(self):
        print("█████████████████████████████████████")
        print("██              <P1>               ██")
        print("██   1. (Ponder)                   ██")
        print("██                                 ██")
        print("██   2. (Sacrifice)                ██")
        print("██                                 ██")
        print("██   3. (Back)                     ██")
        print("██                                 ██")
        print("█████████████████████████████████████")
    
    def Ponderstatus(self,action):
        success = False
        if action >= 2:
            success = True
            print("█████████████████████████████████████████")
            print("██                <P1>                 ██")
            print("██+     Gained +1 Card next round     +██")
            print("██                                     ██")
            print("█████████████████████████████████████████")
        else:
            print("█████████████████████████████████████████")
            print("██                <P1>                 ██")
            print("██  Not enough Action Pts to continue  ██")
            print("██                                     ██")
            print("█████████████████████████████████████████")
        return success
    
    def Sacrifice(self,action,pop):
        success = False
        if pop >= 200 and action >= 1:
            success = True
            print("█████████████████████████████████████████")
            print("██                <P1>                 ██")
            print("██+       Gained +1 Power point       +██")
            print("██                                     ██")
            print("█████████████████████████████████████████")
        else:
            print("█████████████████████████████████████████")
            print("██                <P1>                 ██")
            print("██     Not enough Pop or Action pts    ██")
            print("██                                     ██")
            print("█████████████████████████████████████████")
        return success
def Card1():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██      -Construct monument-       ██")
    print("██      ▪ +250 Followers           ██")
    print("██                                 ██")
    print("██      ▪ -2 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Build yourself a mighty      ██")
    print("██    statue worth of a god. This  ██")
    print("██    card may have additional     ██")
    print("██    effects, such as giving      ██")
    print("██    power or relics.             ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██              (1)                ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card2():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██        -Tame Wild Beast-        ██")
    print("██      ▪ +1 Monster               ██")
    print("██                                 ██")
    print("██      ▪ -2 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Go into the wild and attempt ██")
    print("██    to catch a beast. Results    ██")
    print("██    may vary. This new world has ██")
    print("██    become more hostile than     ██")
    print("██    before.                      ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██              (2)                ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card3():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██       -Venerate a Peasant-      ██")
    print("██      ▪ +1 Hero                  ██")
    print("██                                 ██")
    print("██      ▪ -2 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Reward a mortal with power,  ██")
    print("██    for they are a part of your  ██")
    print("██    cause. May bring more        ██")
    print("██    followers to your cause.     ██")
    print("██    Choose wisely.               ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██              (3)                ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card4():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██         -Control Mortal-        ██")
    print("██      ▪ +100% follower gain      ██")
    print("██                                 ██")
    print("██      ▪ -3 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Forcefully control a mortal, ██")
    print("██    this doubles follower prod.  ██")
    print("██    May give some strange        ██")
    print("██    scenarios what may hinder or ██")
    print("██    benefit you                  ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██              (4)                ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card5():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██         -Create a Relic-        ██")
    print("██      ▪ +1 Relic                 ██")
    print("██                                 ██")
    print("██      ▪ -2 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Create a relic from divine   ██")
    print("██    power, this relic might      ██")
    print("██    hinder or strengthen you.    ██")
    print("██    Take tremendous care of this ██")
    print("██    as unknown dangers await     ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██              (5)                ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card6():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██       -Help a fellow God-       ██")
    print("██      ▪ +Buff or Resource        ██")
    print("██                                 ██")
    print("██      ▪ -4 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Do something for a minor god ██")
    print("██    and hopefully gain something ██")
    print("██    out of it.                   ██")
    print("██    This card will not hinder    ██")
    print("██    progress.                    ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 1 Power    ██")
    print("██              (6)                ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card7():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██       -Mimic famous heroes      ██")
    print("██      ▪ +850 Followers           ██")
    print("██                                 ██")
    print("██      ▪ -5 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Perform deeds of greatness   ██")
    print("██    from different mythologies.  ██")
    print("██    They got famous with these,  ██")
    print("██    so why can't you?            ██")
    print("██    This card will never hinder. ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██              (7)                ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card8():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██    -Give back to the mortals-   ██")
    print("██      ▪ +Followers per turn      ██")
    print("██                                 ██")
    print("██      ▪ -5 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Dedicate your time to give   ██")
    print("██    back to your followers.      ██")
    print("██    Depending on the deed, you   ██")
    print("██    will gain a number of        ██")
    print("██    followers per turn           ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██              (8)                ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card9():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██         -Minor Assualt-         ██")
    print("██      ▪ -250 followers for opp.  ██")
    print("██                                 ██")
    print("██      ▪ -2 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Fabricate a force to         ██")
    print("██    attack your opponent. May    ██")
    print("██    backfire or be more          ██")
    print("██    effective than usual.        ██")
    print("██    Perfectly balanced           ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██              (9)                ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card10():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██       -Create Battlements-      ██")
    print("██      ▪ +100 damage to opp.      ██")
    print("██            (Stacks)             ██")
    print("██      ▪ -2 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Prepare your forces for an   ██")
    print("██    allout war. Kills 100 more   ██")
    print("██    followers than usual in      ██")
    print("██    assaults. May increase or    ██")
    print("██    descrease in effectiveness   ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 1 Power    ██")
    print("██              (10)               ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card11():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██        -Deflect the Blame-      ██")
    print("██      ▪ +1 Debuff to Opp.        ██")
    print("██                                 ██")
    print("██      ▪ -5 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Blame a tragic event on your ██")
    print("██    opponent, which makes the    ██")
    print("██    gods hurl curses and spears. ██")
    print("██    PS. Not a very nice action   ██")
    print("██    and might backfire. Or not.  ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██               (11)              ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card12():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██         -Bet with Chaos-        ██")
    print("██      ▪ +Good or Bad event       ██")
    print("██                                 ██")
    print("██      ▪ -3 Action Points         ██")
    print("██                                 ██")
    print("██   ▪You bet against a primordial ██")
    print("██    power that was here before   ██")
    print("██    time. It is bound to get     ██")
    print("██    risky. But the payoff is     ██")
    print("██    worth total annihilation.    ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██               (12)              ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card13():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██        -Raid a settlement-      ██")
    print("██      ▪ Attacks an opp. city     ██")
    print("██                                 ██")
    print("██      ▪ -2 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Find a settlement and raid   ██")
    print("██    it for its' valuables and    ██")
    print("██    followers. May go badly or   ██")
    print("██    better than usual depending  ██")
    print("██    on where you raid.           ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██               (13)              ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card14():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██        -Duel a minor God-       ██")
    print("██      ▪ +Resources from the god  ██")
    print("██                                 ██")
    print("██      ▪ -3 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Fight against a random god   ██")
    print("██    you find in the aether.      ██")
    print("██    Success may vary, depending  ██")
    print("██    on who you fight or how the  ██")
    print("██    fight goes. (Low fail %)     ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 2 Power    ██")
    print("██               (14)              ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")
def Card15():
    print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
    print("█████████████████████████████████████")
    print("██       -Take over a realm-       ██")
    print("██      ▪ +1 Realm                 ██")
    print("██                                 ██")
    print("██      ▪ -6 Action Points         ██")
    print("██                                 ██")
    print("██   ▪A true power move. Just go   ██")
    print("██    and steal a realm completely ██")
    print("██    and reap its benefits.       ██")
    print("██    Realms may give resources    ██")
    print("██    every turn. Never fails      ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 4 Power    ██")
    print("██               (15)              ██")
    print("█████████████████████████████████████")
    print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
    print(" ")
def Card16():
    print("◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣")
    print("█████████████████████████████████████")
    print("██     -Create a Greater Relic-    ██")
    print("██      ▪ +3 Relics                ██")
    print("██                                 ██")
    print("██      ▪ -4 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Create a Greater Relic along ██")
    print("██    with two smaller relics.     ██")
    print("██    The greater relic will give  ██")
    print("██    bonuses to resources and     ██")
    print("██    maybe a permanent buff.      ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 1 Power    ██")
    print("██               (16)              ██")
    print("█████████████████████████████████████")
    print("◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤")
    print(" ")
def Card17():
    print("◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣")
    print("█████████████████████████████████████")
    print("██      -Crown a Greater Hero-     ██")
    print("██      ▪ +3 Heroes                ██")
    print("██                                 ██")
    print("██      ▪ -4 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Crown a Greater Hero along   ██")
    print("██    with two of their friends.   ██")
    print("██    Will grant more resources    ██")
    print("██    alongside with a possible    ██")
    print("██    permanent buff.              ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 1 Power    ██")
    print("██               (17)              ██")
    print("█████████████████████████████████████")
    print("◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤")
    print(" ")
def Card18():
    print("◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣")
    print("█████████████████████████████████████")
    print("██   -Capture a Greater Monster-   ██")
    print("██      ▪ +3 Heroes                ██")
    print("██                                 ██")
    print("██      ▪ -4 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Capture a mythical creature  ██")
    print("██    along side their pack.       ██")
    print("██    Will grant more resources    ██")
    print("██    alongside with a possible    ██")
    print("██    permanent buff.              ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 1 Power    ██")
    print("██               (18)              ██")
    print("█████████████████████████████████████")
    print("◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤")
    print(" ")#
def Card19():
    print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
    print("█████████████████████████████████████")
    print("██       -Capture Shærimnir-       ██")
    print("██      ▪ +6 action points         ██")
    print("██                                 ██")
    print("██      ▪ -6 Action Points         ██")
    print("██                                 ██")
    print("██   ▪A legendary boar that makes  ██")
    print("██    the consumer filled with     ██")
    print("██    vigor and might. Gives 6     ██")
    print("██    action points for 4 turns.   ██")
    print("██    This card never fails.       ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 2 Power    ██")
    print("██               (19)              ██")
    print("█████████████████████████████████████")
    print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
def Card20():
    print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
    print("█████████████████████████████████████")
    print("██       -Create Equipment-        ██")
    print("██      ▪ +1 Permanent Buff        ██")
    print("██                                 ██")
    print("██      ▪ -5 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Create equipment that is     ██")
    print("██    worthy of a grand god. But   ██")
    print("██    you'll need to meld your     ██")
    print("██    relics to create one.        ██")
    print("██    This card will never fail    ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 2 Relics   ██")
    print("██               (20)              ██")
    print("█████████████████████████████████████")
    print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
    print(" ")

def Card21():
    print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("█████████████████████████████████████")
    print("██  -Accept gifts from followers-  ██")
    print("██      ▪ +Relics,Heroes,Monsters  ██")
    print("██                                 ██")
    print("██      ▪ -3 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Gain resources based on the  ██")
    print("██    amount of followers you have ██")
    print("██    (Have atleast 1000 followers)██")
    print("██    This card will never fail.   ██")
    print("██     Perfectly balanced          ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 1000+ pop  ██")
    print("██               (21)              ██")
    print("█████████████████████████████████████")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print(" ")

def Card22():
    print("◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣")
    print("█████████████████████████████████████")
    print("██      -Divine Proficiency-       ██")
    print("██      ▪ +Buffs & 3 Power         ██")
    print("██                                 ██")
    print("██      ▪ -4 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Take time to increase your   ██")
    print("██    godhood and improve your     ██")
    print("██    divine status for later      ██")
    print("██    benefit.                     ██")
    print("██    Card will never fail         ██")
    print("██                                 ██")
    print("██      ▪ Requirements: None       ██")
    print("██               (22)              ██")
    print("█████████████████████████████████████")
    print("◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤")
    print(" ")

def Card23():
    print("◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣◢◣")
    print("█████████████████████████████████████")
    print("██        -Grant Miracles-         ██")
    print("██      ▪ +1500 Followers          ██")
    print("██                                 ██")
    print("██      ▪ -4 Action Points         ██")
    print("██                                 ██")
    print("██   ▪Grant miracles in hope to    ██")
    print("██    gain a large following.      ██")
    print("██    May be more or less          ██")
    print("██    effective depending on what  ██")
    print("██    happens.                     ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 2 Power    ██")
    print("██               (23)              ██")
    print("█████████████████████████████████████")
    print("◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤◥◤")
    print(" ")

def Card24():
    print("👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁")
    print("█████████████████████████████████████")
    print("██          -Judgement-            ██")
    print("██      ▪ Results may vary         ██")
    print("██                                 ██")
    print("██      ▪ 0 Action Point           ██")
    print("██                                 ██")
    print("██   ▪Pray. And face judgement     ██")
    print("██    from the one above all.      ██")
    print("██    May give tremendous rewards  ██")
    print("██    or huge failiures.           ██")
    print("██    Completely random.           ██")
    print("██                                 ██")
    print("██      ▪ Requirements: 3 Power    ██")
    print("██              (24)               ██")
    print("█████████████████████████████████████")
    print("👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁")
    print(" ")

def Card25():
    print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
    print("█████████████████████████████████████")
    print("██       -Create new Realm-        ██")
    print("██      ▪ +1 Realm                 ██")
    print("██                                 ██")
    print("██      ▪ ALL Action Points        ██")
    print("██                                 ██")
    print("██   ▪Create a realm in your own   ██")
    print("██    vision. Can only have made   ██")
    print("██    one realm at a time.         ██")
    print("██    Potency of this realm will   ██")
    print("██    depend on how much is given. ██")
    print("██                                 ██")
    print("██      ▪ Requirements: ALL Power  ██")
    print("██               (25)              ██")
    print("█████████████████████████████████████")
    print("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★")
    print(" ")

def Seduce(Pop,Seduce,Gain):
    if Seduce == True:
        Pop += (Gain * 2)
        print("Followers have been doubled, due to -Control Mortal-")
    else:
        Pop += Gain
    return Pop 

def Lethality(Pop,Lethal,Damage,Normaldmg):
    if Lethal == True:
        Pop -= (Damage + Normaldmg)
        print("You dealt",Damage,"extra damge to your opponent")
    else:
        Pop -= Normaldmg
    return Pop

def ActionSabotage(PlayerAction,ActAmnt):
    PlayerAction -= ActAmnt
    return PlayerAction 


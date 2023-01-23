
import random
import time
from enum import Enum
#ToDo - write a CAPS program to capitalize all input so that it doesn't matter how they enter their name or make things one letter to select. 
#ToDo - Make validators into functions, make input into function with min and max acceptance stuff
#ToDo - Turn hpPotions into a bonus life in combat 
Weapon = Enum("Weapon", "Longsword, Warhammer, Spear")
Spell = Enum("Spells", "Fireball, IceStorm, LightningBolt")
Tool = Enum("Tools", "Lockpick, GrapplingHook, " )
Shield = Enum("Defense","Shield, ChainMail, Cloak")
Resistance = Enum("Resistance","MagicShield, RingOfProtection, Counterspell")
Weapons = {}
Spells = {}
Tools = {}
Shields = {}
Resistances = {}
Weapons["Fist"] = {"Name": "Fist", "dmgBonus": 2, "dmgType": "Bludgeoning"}
Weapons["BatFist"] = {"Name": "BatFist", "dmgBonus": 50, "dmgType": "Kill"}
Weapons["TrollMace"] = {"Name": "TrollMace", "dmgBonus": 20, "dmgType": "Bludgeoning"}
Weapons["Longsword"] = {"Name": "Longsword","dmgBonus": 5, "dmgType": "Slashing"}
Weapons["Warhammer"] = {"Name": "Warhammer","dmgBonus": 5, "dmgType": "Bludgeoning"}
Weapons["Spear"] = {"Name": "Spear","dmgBonus": 5, "dmgType": "Piercing"}
Weapons["ObsidianEdge"] = {"Name": "Obsidian edge","dmgBonus": 15, "dmgType": ["Slashing", "Fire"]}
Spells["Fireball"] = {"Name": "Fire ball","dmgBonus": 10, "dmgType": "Fire"}
Spells["IceStorm"] = {"Name": "Ice storm","dmgBonus": 10, "dmgType": "Cold"}
Spells["LightningBolt"] = {"Name": "Lightning bolt","dmgBonus": 15, "dmgType": "Lightning"}
Spells["EclipticBeam"] = {"Name": "Ecliptic beam","dmgBonus": 35, "dmgType": "Dark"}
Spells["NoMagic"] = {"Name": "No Magic for you", "dmgBonus": 2, "dmgType": "Bad"}

def checkForDead():
  if player.hp <= 0 and player.hpPotions > 0:
    print("Thankfully just as you're about to fall you manage take a swig of that potion you found. Returning some hp.")
    player.hp = player.hp + .5 * player.maxhp
  elif player.hp <= 0:
    print("You Have Died")
    print("Play again? y/n")
    userInput =  input()
    if userInput == "y":
      playeracterSelect()
    else:
      quit()
  else:
    pass

def levelUp():
  if player.xp >= 10 * player.lvl:
    player.xp -= 10 * player.lvl
    increases = 0
    print("Level up!")
    player.maxhp += 10
    player.lvl += 1
    calcStats()
    printStats()
    print("Choose two stats to increase by 2")
    ##stats = ["strength","dexterity","constitution","intelligence","wisdom"] <- in case some particular slimmer code doesn't work
    print(f"1: Strength")
    print(f"2: Dexterity")
    print(f"3: Constitution")
    print(f"4: Intelligence")
    print(f"5: Wisdom")
    while increases < 2:
      print("Type the number of the stat you wish to increase")
      userChoice = int(input())
      if userChoice == 1:
        player.strength +=2
        print("Strength + 2!")
        increases += 1
      elif userChoice == 2:
        player.dexterity +=2
        print("Dexterity + 2!")
        increases += 1
      elif userChoice == 3:
        player.constitution +=2
        print("Constitution + 2!")
        increases += 1
      elif userChoice == 4:
        player.intelligence +=2
        print("Intelligence + 2!")
        increases += 1
      elif userChoice == 5:
        player.wisdom +=2
        print("Wisdom + 2!")
        increases += 1
      else:
        print("please enter a number 1-5")
    calcStats()
    player.hp = player.maxhp
    print("You feel invigorated by your level up. Health restored!")
    levelUp()
  else:
    pass
#toDo - Make a printStats functions to display stats, and a calcStats to reintialize stats
def calcStats():
  player.conModifier = player.constitution/10
  player.maxhp = player.maxhp*player.conModifier
  if player.race == "Warrior":
    player.dmg = 10 + player.strength + player.weapon["dmgBonus"]
    player.dmgType = player.weapon["dmgType"]
  elif player.race == "Rogue":
    player.dmg = 10 + player.dexterity + player.weapon["dmgBonus"]
    player.dmgType = player.weapon["dmgType"]
  elif player.race == "Wizard":
    player.dmg = 10 + player.intelligence + player.spell["dmgBonus"]
    player.dmgType = player.spell["dmgType"]
  player.critMultiplier = player.dexterity/5

def printStats():
  print(f"""

  Adventurer:{player.name} the lvl {player.lvl} {player.race}

  Max HP:{player.maxhp} -- How many hits you can take

  Strength: {player.strength} -- Affects warrior dmg and your ability to complete tasks of heft

  Dexterity:{player.dexterity} -- Affects rogue dmg and your ability to complete mobility based feats and increases your crit dmg

  Constitution:{player.constitution} -- Affects your max HP and resistance to some attacks

  Intelligence:{player.intelligence} -- Affects wizard dmg and understanding of things

  Wisdom:{player.wisdom} -- Affects perception and noticing secrets

  Weapon:{player.weapon['Name']} -- Affects your dmg type and amount

  Shield:{player.shield} -- Blocks physical damage

  Tool:{player.tool} -- Situational items

  Spell:{player.spell['Name']} -- Decides damage type and power of the mage, some noncombat use

  Resistance:{player.resistance} -- Provides blocking power against magic

  Damage:{player.dmg} -- Base damage before rolls and calculations, decided by your main stat

  Damage Type:{player.dmgType} -- Decided by your main method of attack, some enemies are weaker or stronger against specific types of dmg

  XP:{player.xp} -- Counts experience total until next level up, XP requirement is your level * 10

  Damage Stop:{player.dmgStop} -- Blocks a flat amount of damage, provided by advanced defensive items

  Damage Bonus:{player.dmgBonus} -- Additional damage added onto your base before calculations, added by your weapon or spell

  Constitution Modifier:{player.conModifier} -- Your constitution/10, multiplies into your max hp

  Crit Multiplier:{player.critMultiplier} -- Your dexterity/5, increases your critical hit damage mildly increases likelihood
  """)
  
#Should allow players to select their class, altering their base stats and equipment.
class char:
    def __init__(self, race, name, hp, strength, dexterity, constitution, intelligence, wisdom,):
        self.name = name 
        self.race = race
        self.maxhp = hp
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.weapon = Weapons["Fist"] 
        self.shield = None  
        self.tool = None 
        self.spell = Spells["NoMagic"]
        self.resistance = None 
        self.dmg = 10
        self.dmgType = None
        self.xp = 0 
        self.dmgStop = 0 
        self.dmgBonus = 0
        self.lvl = 1
        self.conModifier = self.constitution/10
        self.maxhp = self.maxhp*self.conModifier
        self.critMultiplier = self.dexterity/5
        self.hpPotions = 0
## toDo - write a simple level up function that checks xp and then allows them to choose some stat increases and increases their HP
## toDo - make a calculate function that adds up damage and stats before fights to make things more progressive, con is a modifier to HP
## toDo - make it so weapons affect your dmg bonus, not dmg and thus don't stack
    def __str__(self):
        return f"{self.race}{self.weapon}{self.shield}{self.tool}{self.spell}{self.resistance}{self.dmgType}{self.name}()"
    def selectThings(self):
        if self.race == "Warrior":
          weapons = [f"{weapon.value}-{weapon.name}" for weapon in Weapon]
          weapons = ", ".join(weapons[:-1]) + " or " + weapons[-1]
          choice = int(input(f"Choose your weapon {weapons}:  "))
          self.weapon = Weapon(choice)
          if self.weapon == Weapon.Warhammer:
            self.weapon = Weapons["Warhammer"]
            self.dmgType = self.weapon["dmgType"]
            self.dmgBonus = self.weapon["dmgBonus"]
          if self.weapon == Weapon.Longsword:
            self.weapon = Weapons["Longsword"]
            self.dmgType = self.weapon["dmgType"]
            self.dmgBonus = self.weapon["dmgBonus"]
          if self.weapon == Weapon.Spear:  
            self.weapon = Weapons["Spear"]
            self.dmgType = self.weapon["dmgType"]
            self.dmgBonus = self.weapon["dmgBonus"]
          shields = [f"{shield.value}-{shield.name}" for shield in Shield]
          shields = ", ".join(shields[:-1]) + " or " + shields[-1]
          choice = int(input(f"Choose your shield {shields}:  "))
          self.shield = Shield(choice)
          self.dmg += self.strength
          print("You're stronging, Sir")

        elif self.race == "Wizard":
          spells = [f"{spell.value}-{spell.name}" for spell in Spell]
          spells = ", ".join(spells[:-1]) + " or " + spells[-1]
          choice = int(input(f"Choose your weapon {spells}:  "))
          self.spell = Spell(choice)
          if self.spell == Spell.Fireball:           
            self.spell = Spells["Fireball"]
            self.dmgType = self.spell["dmgType"]
          if self.spell == Spell.IceStorm:
            self.spell = Spells["IceStorm"]
            self.dmgType = self.spell["dmgType"]
          if self.spell == Spell.LightningBolt:
            self.spell = Spells["LightningBolt"]
            self.dmgType = self.spell["dmgType"]
          resistances = [f"{resistance.value}-{resistance.name}" for resistance in Resistance]
          resistances = ", ".join(resistances[:-1]) + " or " + resistances[-1]
          choice = int(input(f"Choose your shield {resistances}:  "))
          self.resistance = Resistance(choice)
          self.dmg += self.intelligence
          print("May your magic burn bright")

        elif self.race == "Rogue":
          weapons = [f"{weapon.value}-{weapon.name}" for weapon in Weapon]
          weapons = ", ".join(weapons[:-1]) + " or " + weapons[-1]
          choice = int(input(f"Choose your weapon {weapons}:  "))
          self.weapon = Weapon(choice)
          if self.weapon == Weapon.Warhammer:
            self.weapon = Weapons["Warhammer"]
            self.dmgType = self.weapon["dmgType"]
            self.dmgBonus = self.weapon["dmgBonus"]
          if self.weapon == Weapon.Longsword:
            self.weapon = Weapons["Longsword"]
            self.dmgType = self.weapon["dmgType"]
            self.dmgBonus = self.weapon["dmgBonus"]
          if self.weapon == Weapon.Spear:  
            self.weapon = Weapons["Spear"]
            self.dmgType = self.weapon["dmgType"]
            self.dmgBonus = self.weapon["dmgBonus"]
          tools = [f"{tool.value}-{tool.name}" for tool in Tool]
          tools = ", ".join(tools[:-1]) + " or " + tools[-1]
          choice = int(input(f"Choose your tool {tools}:  "))
          self.tool = Tool(choice)
          self.dmg += self.dexterity
          print("Happy hunting")
          
#same as the above character template but for monsters, much shorter
class monster:
    def __init__(self, name, hp, damage, weakness, blockedBy, xp):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weakness = weakness
        self.blockedBy = blockedBy 
        self.xp = xp
    def __str__(self):
        return f"{self.name}{self.weakness}{self.blockedBy}()"
    
 #First attempts at making a combat system, make dmg a variable thats set in classes and then modified based off of stats.Give weapons a strength to match weaknesses      
 #Based on a combat system that I saw on stack overflow. Works a bit differently and is expanded but that's where I got the general form of it. 
 #Potentially have weakness and resistance be dictionarys and use the check for key function with the input of the players dmg to check
class combat:
  def __init__(self):
    calcStats()
    self.round = 0
    self.gameOver = False
    self.playerDmg = 0
    self.opponentDmg = 0 
  def newRound(self):
    self.round += 1
    print(f"\n***   Round: {self.round}   ***\n") 
  def checkWin(self,player, opponent):
    if opponent.hp <= 0:
      self.gameOver = True
      print("You win")
      player.xp += opponent.xp 
    elif player.hp <= 0:
      print("You have died")
      quit()
  def takeTurn(self,player,opponent):
    roll = random.randint(1,20)
    self.playerDmg = 0 
    roll += player.dexterity/5 
    if player.dmgType == opponent.weakness:
      print("Your dmg type seems particularly strong against this monster, roll + 5!")
      roll += 5 
    if roll >= 20:
      print(f"You rolled a {roll} for attacking")
      self.playerDmg = (player.dmg + random.randint(1,10))*player.critMultiplier
      self.playerDmg = round(self.playerDmg)
      opponent.hp = opponent.hp - self.playerDmg
      print("\033[1;31;40m POWER LEVELS OVER 9000!!!\033[0m")  
    elif roll >= 15:
      print(f"You rolled a {roll} for attacking")
      self.playerDmg = (player.dmg + random.randint(1,10))*(player.critMultiplier/2)
      self.playerDmg = round(self.playerDmg)
      opponent.hp = opponent.hp - self.playerDmg
      print(f"Critical Hit!")
    elif roll < 10:
      print(f"You rolled a {roll} for attacking")
      print("you missed!")
    else:
      print(f"You rolled a {roll} for attacking")
      self.playerDmg = (player.dmg+ random.randint(1,10))
      self.playerDmg = round(self.playerDmg)
      opponent.hp = opponent.hp - self.playerDmg
      print(f"You land a hit")
  def monsterTurn(self,player,opponent):
    roll = random.randint(1,20)
    if player.resistance == opponent.blockedBy or player.shield == opponent.blockedBy:
      print("Your defenses seem particularly strong against this creature, roll + 5!")
      roll += 5 
    if roll >= 15:
      print(f"You rolled a {roll} for defense ") 
      print("\033[32mTanked that hit like a boss\033[0m")
      self.opponentDmg = ((opponent.damage + random.randint(1,10))/2) - player.dmgStop
      player.hp = player.hp - self.opponentDmg
    else:
      print(f"You rolled a {roll} for defense ") 
      print("You take a solid hit")
      self.opponentDmg = ((opponent.damage + random.randint(1,10))) - player.dmgStop
      player.hp = player.hp - self.opponentDmg 
  def displayResult(self,player,opponent):
    if player.race == 'Wizard': 
      print(f"{player.name} blasted a {player.spell['Name']} at {opponent.name} it dealt {self.playerDmg} {player.dmgType} dmg.")
      print(f"{opponent.name} attacked {player.name} they dealt {self.opponentDmg} dmg")
      print(f"{opponent.name} hp:{opponent.hp}")
      print(f"{player.name} hp:{player.hp}")
    else:
      print(f"{player.name} used a {player.weapon['Name']} on {opponent.name} it dealt {self.playerDmg} {player.dmgType} dmg.")
      print(f"{opponent.name} attacked {player.name} they dealt {self.opponentDmg} dmg")
      print(f"{opponent.name} hp:{opponent.hp}")
      print(f"{player.name} hp:{player.hp}")
    
def playeracterSelect():
  print("Let's start with your name: ") 
  name = input()  
  print("Good luck, " +name+ ".")  
  classes = ["w","r","z"]
  print("Next we'll need your class. What kind of adventure are you?")
  userInput = ""
  global player
  player = ()
  while userInput not in classes:
    print("Options: (r)ogue/(w)arrior/wi(z)ard")
    userInput = input()
    if userInput == "r":
      player = char('Rogue', name, 100, 10, 18, 12, 14, 16)
      player.selectThings()
      playerStart()
    elif userInput == "z":
      player = char('Wizard', name, 75, 8, 10, 10, 22, 14)
      player.selectThings()
      playerStart()
    elif userInput == "w":
      player = char('Warrior', name, 125, 18, 14, 14, 8, 10) 
      player.selectThings()
      playerStart()
    else: 
      print("Please enter a valid option.")

def playerStart():
  actions = ["l","r","f"]
  print("You begin in a dusty room made of cobbled stone. There are 3 paths.")
  userInput = ""
  while userInput not in actions:
    print("Options: (l)eft/(r)ight/(f)orward")
    userInput = input()
    if userInput == "f":
      ghoulGames()
    elif userInput == "r":
      longHallway()
    elif userInput == "l":
      trollBridge()
    else: 
      print("Please enter a valid option.")

#First room that you find by going forwards. Requires a stat check to pass the course
#if they opt to fight or fail the course it initiates combat with the ghoul
#upon completeing the games playeracters with a high wis stat can find a secret room
    
def ghoulGames():
  actions = ["p","f","t"]
  print("Welcome young",player.race,"to the Ghoul Games. Announces an undead ringmaster")
  print("To escape my room you must prove your worth in my obstacle course")
  userInput = ""
  while userInput not in actions:
    print("Options: (p)lay along/(f)ight the ghoul/(t)urn and run")
    userInput = input()
    if userInput == "f":
      vsGhoul() 
    elif userInput == "p":
      if player.dexterity >= 16 or player.strength >= 16:
        print("Thanks to your athletcism you manage to duck, dodge, and weave through the obstacles")
        print("'Well done young ",player.race," take this amulet as a testament to your feat' exclaims the Ringmaster before vanishing into a mist")
        print("As you don the amulet you feel a sharp burst of magical energy course through you, making you faster")
        player.dexterity = player.dexterity + 2
        player.wisdom = player.wisdom + 2
        if player.wisdom < 18:
          print("A single door opens on the left wall of the room")
          input("press enter to continue")
          longHallway()
        else:
          print("While you do notice a door open to the left that seems too obvious a route for catacomb such as this.")
          print("Your trained eyes, now heightened by the amulet, notice the seems of a small trapdoor below the ringmaster.")
          print("Unable to resist the same curiosity that brought you deep underground you slip into the hatch, barely able")
          print("to hear the ringmaster's cries of protest behind you")
          input("press enter to continue")
          treasureRoom()
      else:
        print("You make it part way through the course but you lose your grip on a rope and fall")
        print("partially into a pool of lava, singeing your leg")
        print("'Bah, what a poor showing. You must die for wasting my audience's valuable time'")
        player.hp = player.hp - 15
        checkForDead()
        vsGhoul() 
    elif userInput == "t":
      print("You find the door has slammed closed behind you")
      ghoulGames()
    else: 
      print("Please enter a valid option.")
   
#First combat, player fights the ghoul and either dies or gains access to long hallway or treasure room

def vsGhoul():
  actions = ["t","d"]
  print("hohoho, I see you have chosen death, young adventurer.")
  ghoul = monster('ghoul', 225, 8, 'Fire', Resistance, 10 )
  currentCombat = combat() 
  input("Press enter to continue ")
  while not currentCombat.gameOver:
    currentCombat.newRound()
    currentCombat.takeTurn(player,ghoul)
    currentCombat.monsterTurn(player,ghoul)
    currentCombat.displayResult(player,ghoul)
    currentCombat.checkWin(player,ghoul)
    input("Press enter to continue")
    levelUp()
  print("""As the ghoul dies he drifts apart into whisps "Beware the beast that lays within, you don't know the powers you play with" """)
  print("""
  A small hatch pop open from underneath where the ghost died. You think you can see treasure down there but you're not too sure.
  You also notice a door off to the side that looks much less rewarding, but also much less ominous.
  """)
  print("Options: small (t)rapdoor/(d)oorway ")
  userInput = ""
  while userInput not in actions:
    userInput = input()
    if userInput == "d":
      longHallway()
    elif userInput == "t":
      treasureRoom()
    else:
      print("please enter a valid option")
   
def treasureRoom():
  actions = ["s", "a", "w"]
  print("""
  As you duck down into the trapdoor you're greeted by luminescent piles of gold, amongst which you spy 
  multiple magic weapons. You get the feeling that these are powerful enough that you can probably only handle using one of them.
  There's a a jagged and cruel looking sword cut from obsidian, some well crafted dwarven platemail, and a steel wand inlayed with 
  saphires all resting on pedestals.
  """)
  userInput = ""
  while userInput not in actions:
    userInput = input("Options: Take (s)word/Take (a)rmor/Take (w)and")
    ending = "Taking your newfound item you travel through a plain wood door at the end of the room, deeper into the catacombs."
    if userInput == "s":
      print("""
      As you grasp the hilt the hilt of the black stone blade you feel infernal strength race through you. You feel both stronger and as though you 
      would take less damage from fire.
      """)
      player.resistance = 'Fire'
      player.weapon = Weapons["ObsidianEdge"]
      player.strength += 5
      player.dexterity += 2 
      calcStats()
      print(ending)
      dungeon() 
    elif userInput == "a":
      print(""" 
      Picking up the heavy suit of armor feels like a momentous task, let alone donning it. Thankfully, after some manuevering you manage to get it on
      you definately feel like regardless of whats attacking you this will help prevent damage.  
      """)
      player.dmgStop = 5
      print(ending)
      dungeon()
    elif userInput == "w":
      print(""" 
      As you pick up the wand you feel a jolt of electricity course through you, your senses seem to be moving faster. 
      or at least everything else seems slower. Your magic feels more powerful as well  
      """)
      player.wisdom += 4
      player.intelligence += 4
      calcStats()
      print(ending)
      dungeon()
    else:
      print("please enter a valid option")
  
def trollBridge():
  actions = ["a","f","t", "j"]
  print("""
  As you wander the tunnels you find and step through a door into large chamber with a chasm nearly 20 ft across in the middle, thankfully there's a well built stone bridge crossing it.
  The only issue is that there's a lorge troll standing in the middle of the bridge, munching on an apple. 'Why hello there little one, you must want to be exploring of the dungeon, yes? 
  I'm sorry to say that I only let people who answer my riddle pass' declares the troll. 
  While he doesn't seem particularly hostile the troll is quite large and has what appears to be a large mace sitting next to him. 
  """)

  userInput = ""
  while userInput not in actions:
    print("Options: (a)nswer/(f)ight/(t)urn back/(j)ump across")
    userInput = input()
    if userInput == "a":
      print("""'Ohh yes, this is very good, it's been a long time since something so living and fleshy wanted to talk to me. Here's the riddle:
      My life can be measured in hours,

      I only serve to be devoured.

      Slim, I am quick.

      Fat, I am slow.

      Wind is my foe.
      
      What am I?

      It's really good isn't it? I came up with it myself!'
      """)
      playerAnswer = ""
      answer = "candle"
      attempts = 0
      print("So anyways, I will need an answer if imma let you pass. Because it's been s long since I've seen anyone I'll give you 3 tries(answer in lowercase)")
      while answer not in playerAnswer:
        print(f"You have {3 - attempts} remaining little one")
        playerAnswer = input()
        if answer not in playerAnswer:
          print("Sorry, but that's not it")
          attempts += 1 
        if attempts == 2:
          print("you have one more try, make it a good one ")
        elif attempts == 3:
          print("Oh well, we can't all be as smart as me I suppose")
          trollFight()
        
## toDo - Make an option to double down for a reward
      print(f"'Oh excellent, so well done little {player.race}. Here, you may cross my bridge' the troll steps aside and lets you pass")
      print("As you turn away from the troll and continue down the passage the air thickens and you think you hear voices ahead")
      player.intelligence += 2
      print("Player intelligence + 2!")
      input("press enter to continue")
      cultGathering() 
    elif userInput == "j":
      print("You decide that you'd rather trust your own athleticism than the word of a troll or his bridge")
      if player.strength >= 20 or player.dexterity >= 20:
        print("You make a running jump and manage to sail over the chasm. Tucking into a roll on the other side you rapidly pop to your feet.")
        print("The troll turns around 'Oh ho, I see. Well aren't you quite the individual, don't even need my bridge. Perhaps you could could actually survive what lay ahead.")
        print("As you turn away from the troll and continue down the passage the air thickens and you think you hear voices ahead")
        input("press enter to continue")
        cultGathering() 
      else:
        print("""
        Unfortunately you overestimated you abilities and while you do make a running jump you realize all too late that you aren't going to make it.
        You tumble down into the darkness.
        """)
        player.hp -= 40
        checkForDead()
        ## toDo - make a race system that gives abilities and stats
        print("Thankfully you were in good enough shape to survive the fall. You slowly come to crumpled in the dark on cobbles wet with your blood")
        time.sleep(2)
        dungeon()
    elif userInput == "f":
      print("You draw your breath and prepare for battle hopeing to get the first strike in before the eventual battle.")
      trollFight()
    elif userInput == "t":
      print("You find the door has slammed closed behind you")
      trollBridge()
    else: 
      print("Please enter a valid option.")
      trollBridge()
    

def trollFight ():
  troll = monster('troll', 400, 12, ['Fire','Slashing'], Shields, 25)
  actions = ["c", "e", "p"]
  currentCombat = combat()
  input("Press enter to continue ")
  while not currentCombat.gameOver:
    currentCombat.newRound()
    currentCombat.takeTurn(player,troll)
    currentCombat.monsterTurn(player,troll)
    currentCombat.displayResult(player,troll)
    currentCombat.checkWin(player,troll)
    input("Press enter to continue")
    levelUp()
  print("""
  The troll crashes to the ground, dropping his mace, deafeated. You see the yawning passsage way beyond the bridge is dimly lit and appears to almost be
  leaking darkness into the rest of the room. With the door locked behind you the only other option seems to be down the pit beneath the bridge. There's a well worn 
  rope tied to the edge that you could maybe shimmy down, but it would be very difficult. If only you had something like a grappling hook to tie up here.... Also, the trolls mace rests heavily on the ground. It's incredibly massive but you
  could try to lift it...
  """)
  userInput = ""
  while userInput not in actions:
    print("Options: (c)limb down/(e)nter the cave/(p)ickup the mace")
    userInput = input()
    if userInput == "c":
      if player.dexterity >= 20 or player.strength >= 24:
        print("You nimbly wind your way down the threadbare rope into the darkness")
        dungeon()
      elif "GrapplingHook" in player.tools:
        print("Thankfully you came prepared. You tie the grapple up here and descend into the darkness")
        dungeon()
      else:
        print("Unfortunately your hands slip and you lose grip on the rope, tumbling into the dark.")
        player.hp = player.hp - 30
        dungeon()
    elif userInput == "e":
      cultGathering()
    elif userInput == "p":
      if player.strength >= 22:
        print("Thanks to your absolute immensity you manage to heave the mace over your shoulder. This thing probably deals some serious damage")
        player.weapon = Weapons["TrollMace"]
        print("Options: (c)limb down/(e)nter the cave")
        playerAnswer = input()
        if playerAnswer == "c":
          dungeon()
        elif playerAnswer == "e":
          cultGathering()
        else:
          print("please enter a valid option")
      else:
        print("You find that you can barely budge the mace, let alone lift it. Sadge.")
        userInput = ""
    else:
      print("please enter a valid option")

def longHallway(): 
  actions = ["a","i","t"]
  print("You step into a long hallway, dimly lit and dank. The walls seems to covered in a scrawl that looks like a language, though not one that you know")
  print("At the end of the hallway you see a tall door carved of ebony.")
  print("The door is covered in latches and locks on your side... meaning there must have been, or may still be, something trapped in there")
  userInput = ""
  while userInput not in actions:
    print("Options: (a)pproach the door/(i)nvestigate the walls/(t)urn and run")
    userInput = input()
    if userInput == "a":
      print("""
      As you walk down the hallway you can't help but feel like the air clings to you in an unnatural way,
      making the air itself feel thick and oily. Upon reaching the door you realize it's even larger than you initially thought.
      The door is easily over 9ft tall and the locks are rusted over. Theres a series of claw marks on the sarrounding floor and walls. 
      """)
      print("Options: (o)pen the door/(b)ack away")
      choices = ["o","b"]
      choice = input()
      while choice not in choices:
        if choice == "o":
          print("You slowly unlock the old rusty locks, grinding the bolts in their grooves. The tall door swings open with an unnatural silence.")
          denOfTheBeast()
        elif choice == "b":
          longHallway()
        else:
          print("please enter a valid option")
      

    elif userInput == "i":
      print("""
      As you approach the wall you begin to hear whispering from the edges of your vision, 
      it's almost as though some unseen force is laughing at you. Now that the writing comes into focus it takes
      nearly all your willpower to to stay focused on the swirling caligraphy of the text as the laughing gets louder.
      It's beginning to sound like you yourself are also laughing.
      """)
      if player.intelligence >= 18:
        print("""
        Thankfully because of your rigorous mental training you find yourself able to fight through the laughter and find your own mental voice.
        You make out the text "Here, imprisoned, lies Krushok, Firstborn Tyrant of the Moon" underneath seems to be inscribed some kind of spell that you
        can copy down.
    
        "Ecliptic beam" 
        """)
        player.spell = Spells["EclipticBeam"]
        userInput =""
        longHallway()
      else:
        print("""
        As you get within range of touching the wall the voices grow so loud that they begin to drown out your thoughts
        until all you can experience is the mania that rolls over you. You stumble into the wall and hit your head on the stone, knocking yourself out.
        When you come too it the wall seems perfectly mundane and you can't see any writing. You feel like a bit of your sanity has been crippled. But, perhaps, you gained a bit of knowledge. 
        As you walk away from the wall you begin to hear the whispers again...
        """)
        player.wisdom = player.wisdom - 2
        player.intelligence = player.intelligence + 1
        player.hp = player.hp - 10
        input("Press enter to continue")
        longHallway()
    elif userInput == "t":
      print("You turn and exit the way you came")
      playerStart()
    else:
      print("Please enter a valid option")

## toDo - denOfTheBeast, dungeon, cultGathering -- dungeon should have chest that requires rogue tools
## toD0 - Make list of weapons into a dictionary so I can jsut add new weapons with new types whenever and have it be easier(done)
## toDo - made weaknesses into a list instead of just one input. see if that breaks everything??(It sort of does)
def dungeon():
  actions = ["h", "i", "c"]
  chestUnlocked = False
  userInput = ""
  print(""" 
  You find yourself in the middle of what could only be a dungeon. The ceiling is caved in, allowing for a trickle of light from above. Softly illuminating a dank passageway 
  lined with the iron bars of prison cells, that continues long into the dark. In one of the cells you see an ironbound chest, but you're not sure you can brute force these
  bars or this chest. Another cell seems to have a prisoner hanging by chains. The bedraggled figure dangles from their wrists, barely alive.
  From further ahead you hear breath. Breath that echoes between the walls and leaves your mind feeling empty, a deep and primal rasp. Something is sleeping.
  """)
  while userInput not in actions:
    print("Options: (h)elp prisoner/(i)nvestigate chest/(c)ontinue down")
    userInput = input() 
    if userInput == "h":
      prisonerOptions = ["h", "l"]
      prisonerInput = ""
      while prisonerInput not in prisonerOptions:
        print(""" You cross the hallway and approach the groaning prisoner. He dangles by locked iron manacles "Oh, hello there. Is that someone? It's been so long
        I can hardly see anymore." he creaks. "Will you help me?" """)
        if player.wisdom >= 18:
          print("As you listen to the man you get an eery feeling from him. Some part of this individual seems coiled to strike.")
        prisonerInput = input("Options: (h)elp with the manacles/(l)eave him be ")  
        if prisonerInput == "h":
          print(""""As you approach the prisoner he cackles "Bahah, someone is a bit too trusting." The manacles detach from the walls, elongating, shifting, and hardening
          until they ressemble spikes made of bone prottruding from the forearms of the prisoner. With teeth now bared to reveal large fangs, the vampire lunges. 
          """)
          vampireFight()
        elif prisonerInput == "l":
          print(""" "Wait, wait, are you just leaving me? I can help you! You'll never live if you go alone!" """)
          dungeon()
        else:
          print("please enter a valid option")
    elif userInput == "i":
      chestInput = ""
      chestOptions = ["s","p","t"]
      while chestInput not in chestOptions:
        print("As you stand in front of the chest it appears to be mildly rotten but it ")
        chestInput = input("Options: (p)ick lock/(s)mash it/(tu)rn away")
        if chestInput == "t":
          dungeon()
        elif chestInput == "p":
          if chestUnlocked == False:
            if player.tool == Tool["Lockpick"]:
              print("You succesfully open the chest and pull out a small ornate crystalline bottle filled with a viscous red fluid inside. This health potion will save you from death once")
              player.hpPotions += 1
              chestUnlocked = True
              dungeon() 
            else:
              print("You don't have the tools or expertise to do that.")
              input("Press enter to continue")
              dungeon()
          else:
            print("The chest is already open, leave dweebus.")
            input("Press enter to continue")
            dungeon()
        elif chestInput == "s":
          if chestUnlocked == False:
            if player.strength >= 20:
              print("""Using your massive muscles you tear the chest in twain. Unfortunately you seem to have broken th small bottle that was in the chest.""")
              chestUnlocked == True
              dungeon()
            else:
              print("Unfortunately you're too weak. The chest sits there mockingly.")
              dungeon()
          else:
            print("The chest is already in pieces.")
            dungeon()
    elif userInput == "c":
      print("As you slowly walk down the corridor, away from the pleas of the prisoner, you feel an unnatural cold wash over you and hear chanting ahead.")
      cultGathering()
    else:
      print("please enter a valid option.")
    
def vampireFight():
  vampire = monster("vampire", 50, 12, Spells, Shields, 15)
  currentCombat = combat() 
  input("Press enter to continue ")
  while not currentCombat.gameOver:
    currentCombat.newRound()
    currentCombat.takeTurn(player,vampire)
    currentCombat.monsterTurn(player,vampire)
    currentCombat.displayResult(player,vampire)
    currentCombat.checkWin(player,vampire)
    input("Press enter to continue")
    levelUp()
  print("As you look around the small dungeon your fight with the vampire smashed the old chest, breaking whatever was inside. It looks like your only choice is to continue forward")
  time.sleep(2)
  cultGathering()

def cultGathering():
  actions = ["s","a"]
  print("""
        As you walk down the hallway you begin to hear eerie voices chanting. Rounding the corner you see 3 cultists standing around a pile of dead sheep.
        It looks like you might be able to sneak around them, but at the same time you get a bad feeling about what would happen if they completed their ritual.
         """)
  userInput = ""
  while userInput not in actions:
    print("Options: (s)neak around/(a)mbush them")
    global ambushed 
    ambushed = False
    userInput = input()
    if userInput == "s":
      if player.dexterity >= 16:
        print("""You successfully stalk around the room, as you sneak through the passageway at the end of the room you get a sinking feeling in your stomach""")
        denOfTheBeast()
      else:
        print("You attempt to sneak around the room but unfortunately you stumble and alert the cultists who quickly draw daggers and charge you.")
        ambushed = True 
        cultistFight() 
    elif userInput == "a":
      print("Rushing right in you manage to get the drop on one of the cultists, killing him, before the other two draw their daggers and turn towards you.")
      cultistFight()
    else: 
      print("Please enter a valid option.")
  quit()

def cultistFight():
  numCultists = 3
  cultistsKilled = 0
  global ambushed
  if ambushed == True:
    numCultists = 2
  while cultistsKilled < numCultists:
    currentCombat = combat() 
    cultist = monster("cultist", 70, 15, Weapons, Shields, 15)
    while not currentCombat.gameOver:
      currentCombat.newRound()
      currentCombat.takeTurn(player,cultist)
      currentCombat.monsterTurn(player,cultist)
      currentCombat.displayResult(player,cultist)
      currentCombat.checkWin(player,cultist)
      input("Press enter to continue")
    cultistsKilled += 1
    print("One down")
    levelUp()
  print("""
        Standing over the bodies of the cultists you're drawn deeper into the dungeon towards the breathing.
        """)
  input("Press enter to continue")
  denOfTheBeast()
  

def denOfTheBeast():
  rightHead = monster("Golden head", 100 , 25, Weapons , Resistances, 15) 
  leftHead = monster("Black head", 150, 15, Weapons, Resistances, 15)
  krushok = monster("Krushok", 400, 30, None, None, 55)
  actions = ["l","r"]
  rightHeadDead = False
  leftHeadDead = False
  print(""" 
  Upon entering the room you find yourself in what looks like a large ampitheater. You don't feel like you walked upwards at any
  point, yet you're somehow on a mountaintop. Over the edges of the ampitheater you can see down into the valley where little towns speckle the hillsides.
  In the middle
  of the ampitheater, illuminated by the light of the full moon, lies the source of the breathing. Shackles as large around as you
  bind every limb of a creature you don't recognize. It almost looks like a cerberous but the body is too feline and the heads look almost draconic, something
  about the lines of its face. Slightly more angular and rigid than they should be with smoke rising from the nostrils of the right head.
  Everything about this creature reeks of unnatural magic. 

  As you take one quiet step into the ampitheater you hear the grinding of stone behind you as the passageway seemingly closes of its own accord. 
  Disturbed by the grinding the right head lazily opens its eyes predatory inquisition, revealing eyes comsumed by a golden iris with a slitted
  pupil being the only break in the sheen. As the beast rises to its feat it creates almost no sound, save growl now emitting from the right head.
  Hastily looking around the circular ampitheater you don't see a way out. Maybe because of the chains you could run it in a circle and fight only one head
  but you have to choose quickly. Glancing at the approaching creature you see that its left head is completely blind, eyelids flicking over empty socket,
  that being said it also looks physically stronger than the left head. 
  """)
  userInput = ""
  def rightHeadFight():
    currentCombat = combat()
    while not currentCombat.gameOver:
      currentCombat.newRound()
      currentCombat.takeTurn(player,rightHead)
      currentCombat.monsterTurn(player,rightHead)
      currentCombat.displayResult(player,rightHead)
      currentCombat.checkWin(player,rightHead)
      input("Press enter to continue")
      levelUp()
    rightHeadDead = True 
    if leftHeadDead == False:
      print("Cutting the right head down causes the left to roar in agony and spit fire at you.")
      time.sleep(2)
      leftHeadFight()
    else:
      time.sleep(1)
      krushok()
  def leftHeadFight():
    currentCombat = combat()
    while not currentCombat.gameOver:
      currentCombat.newRound()
      currentCombat.takeTurn(player,leftHead)
      currentCombat.monsterTurn(player,leftHead)
      currentCombat.displayResult(player,leftHead)
      currentCombat.checkWin(player,leftHead)
      input("Press enter to continue")
      levelUp()
    rightLeftDead = True 
    if rightHeadDead == False:
      print("As the smoke from the left head dies the right head takes a deep breath through its nose. Picking up your scent it turns it's empty eyes to you.")
      time.sleep(2)
      rightHeadFight()
    else:
      time.sleep(1)
      krushok()
  def krushok():
  # as you kill it the blood will flow out into the veins of what you now realize is an alter and then the moon cracks and Krushok comes out.
    print("""
    As you triumphantly stand over the defeated beast you feel a sense of dread seep into you. Blood draining from the wounds of the giant creature begins to 
    flow into veins cut in the stone, revealing the acropolis for what it is, an altar. The now blood soaked veins in the stone begin to form a pattern and the moon
    begins to glow red, cracks emerging in it that mimic the pattern in the altar. Before you can think to stop the bleeding the air is pulled from your lungs, drawn in
    by some kind of incredible gravity, just before you begin to see the moon crumple. Meteors and debris begin falling from the sky around you just as the shockwave hits, knocking
    you over just in time to see a small meteor hit the center of the altar, and stand up. 
    
    Your mind travels back to your childhood fairy tales. Particularly one where the old gods chained an untameable evil inside the Moon to protect the Earth, Krushok.
    Now free, the Firstborn Tyrant of the Moon stands over 30ft tall and in the middle of the acropolis. His bottom half is covered in opulescent white scales and is lean and
    clawed like a dragon. His top half is gaunt from millenia of imprisonment but even with skin hugging the bones of his more human half he appears terrifyingly strong.
    Eyes milky white and scarred over, flexing his huge tattered raven wings stolen from Odin's stock, and a wrath unlike any other, Krushok turns towards you. With a noise like inverted
    thunder, pulling you in, Krushok summons a spear of pure moonlight and stalks towards you
    """)
    currentCombat = combat()
    while not currentCombat.gameOver:
      currentCombat.newRound()
      currentCombat.takeTurn(player,krushok)
      currentCombat.monsterTurn(player,krushok)
      currentCombat.displayResult(player,krushok)
      currentCombat.checkWin(player,krushok)
      input("Press enter to continue")
      levelUp()
    print("""
    With one final devastating blow you strike down the ancient god of death and bring peace to the Earth.
    
    If you got this far, congrats! Not only have you won but you have defied all my expectations and managed to beat the game.
    """)

  while userInput not in actions:
    print("I looks like you'll have to fight the beast either way but if you circle it correctly you might be able to take it on one head at a time.")
    print("Options: (r)ight/(l)eft")
    userInput = input()
    if userInput == "l":
      leftHeadFight()
    elif userInput == "l":
      rightHeadFight()
    else:
      print("Please enter a valid option")

if __name__ == "__main__":
    
  while True:

      
    print("Welcome to the mystical land of Tabletopia")
    
    print("As an avid traveler, you have decided to visit the Catacombs of a nearby temple.")
    
    print("However, during your exploration, you find yourself lost.")
    
    playeracterSelect()


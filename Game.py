
import random
import time
from enum import Enum

from pynput.keyboard import Key, Listener

#Lists for potential inventory systems
Weapon = Enum("Weapon", "LongSword, Greataxe, Spear")
Spell = Enum("Spells", "Fireball, IceStorm, LightningBolt")
Tool = Enum("Tools", "Lockpick, GrapplingHook, " )
Shield = Enum("Defense","Shield, ChainMail, Cloak")
Resistance = Enum("Resistance","MagicShield, RingOfProtection, Counterspell")

def checkForDead():
  if player.hp <= 0:
    print("You Have Died")
    time.sleep(4)
    quit()
  else:
    pass

#Should allow players to select their class, altering their base stats and equipment.
class char:
    def __init__(self, race, hp, strength, dexterity, constitution, intelligence, wisdom,):
        self.race = race
        self.maxhp = hp
        self.hp = hp
        self.dexterity = dexterity
        self.strength = strength
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.weapon = None 
        self.shield = None  
        self.tool = None 
        self.spell = None
        self.resistance = None 
        self.dmg = 10
        self.dmgType = None
        self.xp = 0 
        self.dmgStop = 0 

## toDo - write a simple level up function that checks xp and then allows them to choose some stat increases and increases their HP
## toDo - make a calculate function that adds up damage and stats before fights to make things more progressive, con is a modifier to HP
    def __str__(self):
        return f"{self.race}{self.weapon}{self.shield}{self.tool}{self.spell}{self.resistance}{self.dmgType}()"
    def selectThings(self):
        if self.race == "Warrior":
          weapons = [f"{weapon.value}-{weapon.name}" for weapon in Weapon]
          weapons = ", ".join(weapons[:-1]) + " or " + weapons[-1]
          choice = int(input(f"Choose your weapon {weapons}:  "))
          self.weapon = Weapon(choice)
          if self.weapon == Weapon.Greataxe:
            self.dmgType = 'Slashing'
          if self.weapon == Weapon.LongSword:
            self.dmgType = 'Slashing'
          if self.weapon == Weapon.Spear:  
            self.dmgType = 'Piercing'
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
            self.dmgType = 'Fire'
          if self.spell == Spell.IceStorm:
            self.dmgType = 'Cold'
          if self.spell == Spell.LightningBolt:
            self.dmgType = "Lightning"
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
          if self.weapon == Weapon.Greataxe:
            self.dmgType = 'Slashing'
          if self.weapon == Weapon.LongSword:
            self.dmgType = 'Slashing'
          if self.weapon == Weapon.Spear:  
            self.dmgType = 'Piercing'
          tools = [f"{tool.value}-{tool.name}" for tool in Tool]
          tools = ", ".join(tools[:-1]) + " or " + tools[-1]
          choice = int(input(f"Choose your shield {tools}:  "))
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
class combat:
  def __init__(self):
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
    if player.dmgType in opponent.weakness:
      print("Your dmg type seems particularly strong against this monster, roll + 5!")
      roll += 5
    if roll >= 20:
      print(f"You rolled a {roll} for attacking")
      self.playerDmg = (player.dmg+ random.randint(1,10))*3
      opponent.hp = opponent.hp - self.playerDmg
      print(f"POWER LEVELS OVER 9000!!!")
    elif roll >= 15:
      print(f"You rolled a {roll} for attacking")
      self.playerDmg = (player.dmg+ random.randint(1,10))*1.5
      opponent.hp = opponent.hp - self.playerDmg
      print(f"Critical Hit!")
    elif roll < 10:
      print(f"You rolled a {roll} for attacking")
      print("you missed!")
    else:
      print(f"You rolled a {roll} for attacking")
      self.playerDmg = (player.dmg+ random.randint(1,10))
      opponent.hp = opponent.hp - self.playerDmg
      print(f"You land a hit")
  def monsterTurn(self,player,opponent):
    roll = random.randint(1,20)
    if player.resistance or player.shield in opponent.blockedBy:
      print("Your defenses seem particularly strong against this creature, roll + 5!")
      roll += 5 
    if roll >= 15:
      print(f"You rolled a {roll} for defense ") 
      print(f"Tanked that hit like a boss")
      self.opponentDmg = ((opponent.damage + random.randint(1,10))/2) - player.dmgStop
      player.hp = player.hp - self.opponentDmg
    else:
      print(f"You rolled a {roll} for defense ") 
      print("You take a solid hit")
      self.opponentDmg = ((opponent.damage + random.randint(1,10))) - player.dmgStop
      player.hp = player.hp - self.opponentDmg 
  def displayResult(self,player,opponent):
    if player.race == 'Wizard': 
      print(f"{player.race} blasted a {player.spell.name} at {opponent.name} it dealt {self.playerDmg} dmg.")
      print(f"{opponent.name} attacked {player.race} they dealt {self.opponentDmg} dmg")
      print(f"Opponent hp:{opponent.hp}")
      print(f"Player hp:{player.hp}")
    else:
      print(f"{player.race} used a {player.weapon.name} on {opponent.name} it dealt {self.playerDmg} dmg.")
      print(f"{opponent.name} attacked {player.race} they dealt {self.opponentDmg} dmg")
      print(f"Opponent hp:{opponent.hp}")
      print(f"Player hp:{player.hp}")
      
    
  
  

    
def playeracterSelect():
  classes = ["Warrior","Rogue","Wizard"]
  print("We'll need to start with your class. What kind of adventure are you?")
  userInput = ""
  global player
  player = ()
  while userInput not in classes:
    print("Options: Rogue/Warrior/Wizard")
    userInput = input()
    if userInput == "Rogue":
      player = char('Rogue', 100, 10, 18, 10, 14, 16)
      playerStart()
    elif userInput == "Wizard":
      player = char('Wizard', 75, 8, 10, 12, 18, 14)
      playerStart()
    elif userInput == "Warrior":
      player = char('Warrior', 125, 18, 14, 14, 8, 10) 
      playerStart()
    else: 
      print("Please enter a valid option.")

def playerStart():
  actions = ["Left","Right","Forward"]
  player.selectThings()
  print("You begin in a dusty room made of cobbled stone. There are 3 paths.")
  userInput = ""
  while userInput not in actions:
    print("Options: Left/Right/Forward")
    userInput = input()
    if userInput == "Forward":
      ghoulGames()
    elif userInput == "Right":
      longHallway()
    elif userInput == "Left":
      trollBridge()
    else: 
      print("Please enter a valid option.")


    
#First room that you find by going forwards. Requires a stat check to pass the course
#if they opt to fight or fail the course it initiates combat with the ghoul
#upon completeing the games playeracters with a high wis stat can find a secret room
    
def ghoulGames():
  actions = ["Play along","Fight the ghoul","Turn and run"]
  print("Welcome young",player.race,"to the Ghoul Games. Announces an undead ringmaster")
  print("To escape my room you must prove your worth in my obstacle course")
  userInput = ""
  while userInput not in actions:
    print("Options: Play along/Fight the ghoul/Turn and run")
    userInput = input()
    if userInput == "Fight the ghoul":
      vsGhoul() 
    elif userInput == "Play along":
      if player.dexterity >= 16 or player.strength >= 16:
        print("Thanks to your athletcism you manage to duck, dodge, and weave through the obstacles")
        print("'Well done young ",player.race," take this amulet as a testament to your feat' exclaims the Ringmaster before vanishing into a mist")
        print("As you don the amulet you feel a sharp burst of magical energy course through you, making you faster")
        player.dexterity = player.dexterity + 2
        player.wisdom = player.wisdom + 2
        if player.wisdom < 18:
          print("A single door opens on the left wall of the room")
          longHallway()
        else:
          print("While you do notice a door open to the left that seems to obvious a route for catacomb such as this.")
          print("Your trained eyes, now heightened by the amulet, notice the seems of a small trapdoor below the ringmaster.")
          print("Unable to resist the same curiosity that brought you deep underground you slip into the hatch, barely able")
          print("to hear the ringmaster's cries of protest behind you")
          print()
          print()
          print()
          time.sleep(4)
          treasureRoom()
      else:
        print("You make it part way through the course but you lose your grip on a rope and fall")
        print("partially into a pool of lava, singeing your leg")
        print("'Bah, what a poor showing. You must die for wasting my audience's valuable time'")
        player.hp = player.hp - 10
        checkForDead()
        vsGhoul() 
    elif userInput == "Turn and run":
      print("You find the door has slammed closed behind you")
      ghoulGames()
    else: 
      print("Please enter a valid option.")

    
#First combat, player fights the ghoul and either dies or gains access to long hallway or treasure room

def vsGhoul():
  actions = ["Small trapdoor","Doorway"]
  print("hohoho, I see you have chosen death, young adventurer.")
  ghoul = monster('ghoul', 225, 8, Spell  , Resistance, 10 )
  currentCombat = combat() 
  while not currentCombat.gameOver:
    print("Type Next to begin next round ")
    currentCombat.newRound()
    currentCombat.takeTurn(player,ghoul)
    currentCombat.monsterTurn(player,ghoul)
    currentCombat.displayResult(player,ghoul)
    currentCombat.checkWin(player,ghoul)
    input("Press enter to continue")
  print("""As the ghoul dies he drifts apart into whisps "Beware the beast that lays within, you don't know the powers you play with" """)
  print("""
    A small hatch pop open from underneath where the ghost died. You think you can see treasure down there but you're not too sure.
    you also notice a door off to the side that looks much less rewarding, but also much less ominous
  """)
  print("Options: Small trapdoor/Doorway ")
  userInput = ""
  while userInput not in actions:
    userInput = input()
    if userInput == "Doorway":
      longHallway()
    elif userInput == "Small trapdoor":
      treasureRoom()
    else:
      print("please enter a valid option")
   
def treasureRoom():
  actions = ["Take sword", "Take armor", "Take wand"]
  print("""
    As you duck down into the trapdoor you're greeted by luminescent piles of gold, amongst which you spy 
    multiple magic weapons. You get the feeling that these are powerful enough that you can probably only handle using one of them.
    There's a a jagged and cruel looking sword cut from obsidian, some well crafted dwarven platemail, and a steel wand inlayed with 
    saphires all resting on pedestals
  """)
  userInput = ""
  while userInput not in actions:
    userInput = input("Options: Take sword/Take armor/Take wand")
    ending = "Taking your newfound item you travel through a plain wood door at the end of the room, deeper into the catacombs."
    if userInput == "Take sword":
      print("""
        As you grasp the hilt the hilt of the black stone blade you feel infernal strength race through you. You feel both stronger and as though you 
        would take less damage from fire.
      """)
      player.resistance = 'Fire'
      player.strength += 5
      player.dexterity += 2 
      print(ending)
      dungeon() 
    if userInput == "Take armor":
      print(""" 
        Picking up the heavy suit of armor feels like a momentous task, let alone donning it. Thankfully, after some manuevering you manage to get it on
        you definetly feel like regardless of whats attacking you this will help prevent damage.  
      """)
      player.dmgStop = 5
      print(ending)
      dungeon()
    if userInput == "Take wand":
      print(""" 
        As you pick up the wand you feel a jolt of electricity course through you, your senses seem to be moving faster. 
        or at least everything else seems slower. Your magic feels more powerful as well  
      """)
      player.wisdom += 2
      player.intelligence += 2
      player.dmg += 2 
      print(ending)
      dungeon()
    else:
      print("please enter a valid option")

    
  quit()
  
def trollBridge():
  actions = ["Answer the riddle","Fight the troll","Turn back", "Jump across"]
  print("""
    As you wander through the tunnels you reach a wide chamber with a large chasm nearly 20 ft across crossing through it, thankfully there's a well built stone bridge crossing it.
    The only issue is that there's a lorge troll standing in the middle of the bridge, munching on an apple. 'Why hello there little one, you must want to be exploring of the dungeon, yes? 
    I'm sorry to say that I only let people who answer my riddle pass' declares the troll. While he doesn't seem particularly hostile the troll is quite large and has what appears to be a large mace sitting next to him. 
  """)

  userInput = ""
  while userInput not in actions:
    print("Options: Answer the riddle/Fight the troll/Turn back/Jump across")
    userInput = input()
    if userInput == "Answer the riddle":
      print("""'Ohh yes, this is very good, it's been a long time since something so living and fleshy wanted to talk to me. Here's the riddle:
      My life can be measured in hours,

      I only serve to be devoured.

      Slim, I am quick.

      Fat, I am slow.

      Wind is my foe.
      
      What am I?
      It's really good isn't it? I came up with it myself'
      """)
      playerAnswer = ""
      answer = "candle"
      attempts = 0
      print("So anyways, I will need an answer if imma let you pass. Because it's been s long since I've seen anyone I'll give you 3 tries(answer in lowercase)")
      while answer not in playerAnswer:
        print(f"You have {3 - attempts} remaining little one")
        if attempts == 2:
          print("you have one more try, make it a good one ")
        elif attempts == 3:
          print("Oh well, we can't all be as smart as me I suppose")
          trollFight()
        playerAnswer = input()
        if answer not in playerAnswer:
          print("Sorry, but that's not it")
          attempts += 1 
    elif userInput == "Jump across":
      print("You decide that you'd rather trust your own athleticism than the word of a troll or his bridge")
      if player.strength >= 20 or player.dexterity >= 20:
        print("You make a running jump and manage to sail over the chasm. Tucking into a roll on the other side you rapidly pop to your feet.")
        print("the troll turns around 'Oh ho, I see. Well aren't you quite the individual, don't even need my bridge. Perhaps you could could actually survive what lay ahead.")
        print("As you turn away from the troll and continue down the passage the air thickens and you think you hear voices ahead")
        time.sleep(2)
        cultGathering() 
      else:
        print("""
          Unfortunately you overestimated you abilities and while you do make a running jump you realize all too late that you aren't going to make it.
          You tumble down into the darkness
        """)
        player.hp -= 40
        checkForDead()
        ## toDo - make a race system that gives abilities and stats
        print("Thankfully you were in good enough shape to survive the fall. You slowly come to crumpled in the dark on cobbles wet with your blood")
        dungeon()
    elif userInput == "Fight the troll":
      print("You draw your breath and prepare for battle hopeing to get the first strike in before the eventual battle.")
      trollFight()
    elif userInput == "Turn back":
      print("You find the door has slammed closed behind you")
      trollBridge()
    else: 
      print("Please enter a valid option.")
    quit()
  quit() 

def trollFight ():
  troll = monster('troll', 400, 12, Spell , Shield, 15)





def longHallway(): 
  actions = ["Approach the door","Investigate the walls","Turn and run"]
  print("You step into a long hallway, dimly lit and dank. The walls seems to covered in a scrawl that looks like a language, though not one that you know")
  print("At the end of the hallway you see a tall door carved of ebony.")
  print("The door is covered in latches and locks on your side... meaning there must have been or may still be something trapped in there")
  userInput = ""
  while userInput not in actions:
    print("Options: Approach the Door/Investigate the walls/Turn and run")
    userInput = input()
    if userInput == "Approach the door":
      print("""
        As you walk down the hallway you can't help but feel like the air clings to you in an unnatural way,
        making the air itself feel thick and oily. Upon reaching the door you realize it's even larger than you initially thought.
        The door is easily over 9ft tall and the locks are rusted over. Theres a series of claw marks on the sarrounding floor and walls. 
      """)
      print("Options: Open the door/Back away")
      denOfTheBeast()
    elif userInput == "Investigate the walls":
      print("""
        As you approach the wall you begin to hear whispering from the edges of your vision, 
        it's almost as though some unseen force is laughing at you. Now that the writing comes into focus it takes
        nearly all your willpower to to stay focused on the swirling caligraphy of the text as the laughing gets louder.
        It's beginning to sound like you yourself are also laughing.
      """)
      if player.intelligence >= 18:
        print("Thankfully because of your rigorous mental training you find yourself able to fight through the laughter and find your own mental voice.")
        print("""
          You make out the text "Here, imprisoned, lies Krushok, Firstborn Tyrant of the Moon" underneath seems to be inscribed some kind of spell
          "Ecliptic beam" 
        """)
        player.spell = "EclipticBeam"
      else:
        print("""
          As you get within range of touching the wall the voices grow so loud that they begin to drown out your thoughts
          until all you can experience is the mania that rolls over you. You stumble into the wall and hit your head on the stone, knocking yourself out.
          When you come too it the wall seems perfectly mundane and you can't see any writing. You feel like a bit of sanity has left your body but 
          perhaps you gained a bit of knowledge. As you walk away from the wall you begin to hear the whispers again...
        """)
        player.wisdom = player.wisdom - 2
        player.intelligence = player.intelligence + 1
        player.hp = player.hp - 10
        longHallway()
    else:
      print("Please enter a valid option")

if __name__ == "__main__":
    
  while True:

      
    print("Welcome to the mystical land of Tabletopia")
    
    print("As an avid traveler, you have decided to visit the Catacombs of a nearby temple.")
    
    print("However, during your exploration, you find yourself lost.")
    
    print("Let's start with your name: ")
    
    name = input()
    
    print("Good luck, " +name+ ".")
    
    playeracterSelect()


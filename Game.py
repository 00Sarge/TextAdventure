
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
Basic = Enum("Basics", "Shortsword, Buckler, Hammer, Flame, Amulet")

def checkForDead():
  if player.hp <= 0:
    print("You Have Died")
    quit()
  else:
    pass

#Should allow players to select their class, altering their base stats and equipment.
class char:
    def __init__(self, race, hp, strength, dexterity, constitution, intelligence, wisdom,):
        self.race = race
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
    def __init__(self, name, hp, damage, weakness, blockedBy):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weakness = weakness
        self.blockedBy = blockedBy 
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
    elif player.hp <= 0:
      print("You have died")
      quit()
  def takeTurn(self,player,opponent):
    roll = random.randint(1,20)
    if player.dmgType == opponent.weakness:
      print("Your dmg type seems particularly strong against this monster")
      roll = roll + 5
    if roll >= 15:
      print(f"You rolled a {roll} for attacking")
      self.playerDmg = (player.dmg+ random.randint(1,10))*1.5
      opponent.hp = opponent.hp - self.playerDmg
      print(f"Critical Hit!")
    if roll >= 20:
      print(f"You rolled a {roll} for attacking")
      self.playerDmg = (player.dmg+ random.randint(1,10))*3
      opponent.hp = opponent.hp - self.playerDmg
      print(f"POWER LEVELS OVER 9000!!!")
    else:
      print(f"You rolled a {roll} for attacking")
      self.playerDmg = (player.dmg+ random.randint(1,10))
      opponent.hp = opponent.hp - self.playerDmg
      print(f"You land a hit")
  def monsterTurn(self,player,opponent):
    roll = random.randint(1,20)
    if roll >= 15:
      print(f"You rolled a {roll} for defense ") 
      print("Your defenses seem particularly strong against this creature")
      self.opponentDmg = (opponent.damage + random.randint(1,10))/2
      player.hp = player.hp - self.opponentDmg
    else:
      print("You take a solid hit")
      self.opponentDmg = (opponent.damage + random.randint(1,10))
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
      player = char('Rogue', 50, 10, 18, 10, 14, 16)
      playerStart()
    elif userInput == "Wizard":
      player = char('Wizard', 50, 8, 10, 12, 18, 14)
      playerStart()
    elif userInput == "Warrior":
      player = char('Warrior', 75, 18, 14, 14, 8, 10) 
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
        print("'Well done young ",player.race," take this amulet as a testament to your feat' exclaims the Ringmaster")
        player.dexterity = player.dexterity + 2
        player.wisdom = player.wisdom + 2
        print("your inventory now contains")
        if player.wisdom < 18:
          print("A single door opens on the left wall of the room")
          longHallway()
        else:
          print("While you do notice a door open to the left that seems to obvious a route for catacomb such as this.")
          print("Your trained eyes, now heightened by the amulet, notice the seems of a small trapdoor below the ringmaster.")
          print("Unable to resist the same curiosity that brought you deep underground you slip into the hatch, barely able")
          print("to hear the ringmaster's cries of protest behind you")
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
  ghoul = monster('ghoul', 300, 8, 'Fire'  , 'MagicShield' )
  currentCombat = combat() 
  while not currentCombat.gameOver:
    print("Type Next to begin next round ")
    currentCombat.newRound()
    currentCombat.takeTurn(player,ghoul)
    currentCombat.monsterTurn(player,ghoul)
    currentCombat.displayResult(player,ghoul)
    currentCombat.checkWin(player,ghoul)
    time.sleep(2)
  print("""As the ghoul dies he drifts apart into whisps "Beware the beast that lays within, you don't know the powers you play with" """)
  print("""A small hatch pop open from underneath where the ghost died. You think you can see treasure down there but you're not too sure.
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
  print("""As you duck down into the trapdoor you're greeted by luminescent piles of gold, amongst which you spy 
  multiple magic weapons. You get the feeling that these are powerful enough that you can probably only handle using one of them.
  There's a a jagged and cruel looking sword cut from obsidian, some well crafted dwarven platemail, and a steel wand inlayed with 
  saphires all resting on pedestals
  """)
  userInput = ""
  while userInput not in actions:
    userInput = input("Options: Take sword/Take armor/Take wand")
    if userInput == "Take sword":
      print("""As you grasp the hilt the hilt of """)
    quit()
  quit()
  
      

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
      print("""As you walk down the hallway you can't help but feel like the air clings to you in an unnatural way,
        making the air itself feel thick and oily. Upon reaching the door you realize it's even larger than you initially thought.
        The door is easily over 9ft tall and the locks are rusted over. Theres a series of claw marks on the sarrounding floor and walls. 
        """)
      print("Options: Open the door/Back away")
      theBeast()
    elif userInput == "Investigate the walls":
      print("""As you approach the wall you begin to hear whispering from the edges of your vision, 
        it's almost as though some unseen force is laughing at you. Now that the writing comes into focus it takes
        nearly all your willpower to to stay focused on the swirling caligraphy of the text as the laughing gets louder.
        It's beginning to sound like you yourself are also laughing.
        """)
      if player.intelligence >= 18:
        print("Thankfully because of your rigorous mental training you find yourself able to fight through the laughter and find your own mental voice.")
        print("""You make out the text "Here, imprisoned, lies Krushok, Firstborn Tyrant of the Moon" underneath seems to be inscribed some kind of spell
          "Ecliptic beam" 
          """)
        player.spell = "EclipticBeam"
      else:
        print("""As you get within range of touching the wall the voices grow so loud that they begin to drown out your thoughts
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


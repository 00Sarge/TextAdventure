import random
from enum import Enum

#Lists for potential inventory systems
Weapon = Enum("Weapon", "LongSword, Greataxe, Spear")
Spell = Enum("Spells", "Fireball, IceStorm, LightningBolt")
Tool = Enum("Tools", "Lockpick, GrapplingHook, " )
Shield = Enum("Defense","Shield, Chain mail, Cloak")
Resistance = Enum("Resistance","MagicShield, RingOfProtection, Counterspell")

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
    def __str__(self):
        return f"{self.race}()"
    def selectThings(self):
        if self.race == "Warrior":
          weapons = [f"{weapon.value}-{weapon.name}" for weapon in Weapon]
          weapons = ", ".join(weapons[:-1]) + " or " + weapons[-1]
          choice = int(input(f"Choose your weapon {weapons}:  "))
          self.weapon = Weapon(choice)
          shields = [f"{shield.value}-{shield.name}" for shield in Shield]
          shields = ", ".join(shields[:-1]) + " or " + shields[-1]
          choice = int(input(f"Choose your shield {shields}:  "))
          self.shield = Shield(choice)
          print("Excellent selection, Sir")
        #Reminder here to make the stats become modified based on what equipment is selected
        #and that equipment can return as a string so that it can be output in descriptions. 
        elif self.race == "Wizard":
          spells = [f"{spell.value}-{spell.name}" for spell in Spell]
          spells = ", ".join(spells[:-1]) + " or " + spells[-1]
          choice = int(input(f"Choose your weapon {spells}:  "))
          self.spell = Spell(choice)
          resistances = [f"{resistance.value}-{resistance.name}" for resistance in Resistance]
          resistances = ", ".join(resistances[:-1]) + " or " + resistances[-1]
          choice = int(input(f"Choose your shield {resistances}:  "))
          self.resistance = Resistance(choice)
          print("May your magic burn bright")
        elif self.race == "Rogue":
          weapons = [f"{weapon.value}-{weapon.name}" for weapon in Weapon]
          weapons = ", ".join(weapons[:-1]) + " or " + weapons[-1]
          choice = int(input(f"Choose your weapon {weapons}:  "))
          self.weapon = Weapon(choice)
          tools = [f"{tool.value}-{tool.name}" for tool in Tool]
          tools = ", ".join(tools[:-1]) + " or " + tools[-1]
          choice = int(input(f"Choose your shield {tools}:  "))
          self.resistance = Tool(choice)
          print("Happy hunting")

    
#same as the above character template but for monsters
class monster:
    def __init__(self, name, hp, damage, weakness):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weakness = weakness
    def __str__(self):
        return f"{self.race}{self.weakness}()"
       

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
      player = char('Rogue', 10, 10, 16, 10, 14, 16)
      playerStart()
    elif userInput == "Wizard":
      player = char('Wizard', 10, 8, 10, 12, 18, 14)
      playerStart()
    elif userInput == "Warrior":
      player = char('Warrior', 15, 18, 12, 4, 8, 3)
      player.selectThings() 
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
      VsGhoul() 
    elif userInput == "Play along":
      if player.dexterity >= 16 or player.strength >= 16:
        print("Thanks to your athletcism you manage to duck, dodge, and weave through the obstacles")
        print("'Well done young ",player.race," take this amulet as a testament to your feat' exclaims the Ringmaster")
        player.dexterity = player.dexterity + 2
        player.wisdom = player.wisdom + 2
        print("your inventory now contains",player.intelligence)
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
        player.hp = player.hp - 2
        checkForDead()
        VsGhoul() 
    elif userInput == "Turn and run":
      print("You find the door has slammed closed behind you")
      ghoulGames()
    else: 
      print("Please enter a valid option.")

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
      The door is easily over 9ft tall and the locks are rusted over. Theres a series of claw marks on the sarrounding floor and walls. """)
      print("Options: Open the door/Back away")
      theBeast()
    elif userInput == "Investigate the walls":
      print("""As you approach the wall you begin to hear whispering from the edges of your vision, 
      it's almost as though some unseen force is laughing at you. Now that the writing comes into focus it takes
      nearly all your willpower to to stay focused on the swirling caligraphy of the text as the laughing gets louder.
      It's beginning to sound like you yourself are also laughing.""")
      if player.intelligence >= 18:
        print("Because of your rigorous mental training you find yourself able to fight through the laughter and find your own mental voice.")
        print("""You make out the text "Here, imprisoned, lies Krushok, Firstborn Tyrant of the Moon" underneath seems to be inscribed some kind of spell
        "Ecliptic beam" """)
        player.spell = "EclipticBeam"
      else:
        print("""As you get within range of touching the wall the voices grow so loud that they begin to drown out your thoughts
        until all you can experience is the mania that rolls over you. You stumble into the wall and hit your head on the stone, knocking yourself out.
        When you come too it the wall seems perfectly mundane and you can't see any writing. You feel like a bit os sanity has left your body but 
        perhaps you gained a bit of knowledge. As you walk away from the wall you begin to hear the whispers again...""")
        player.wisdom = player.wisdom - 2
        player.intelligence = player.intelligence + 1
        player.hp = player.hp - 2
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


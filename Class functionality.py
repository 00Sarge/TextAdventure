import random
from enum import Enum

#Lists for potential inventory systems
Weapon = Enum("Weapon", "Long Sword, Greataxe, Spear")
Spells = Enum("Spells", "Fireball, Ice storm, Lightning bolt")
Tools = Enum("Tools", "Lockpick, Grappling Hook, " )
physDefense = Enum("physDefense","Shield, Chain mail, Cloak")
magDefense = Enum("magDefense","Magic shield, Ring of protection, Counterspell")

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
        self.defense = None
        self.tools = None
        self.spells = None
    def __str__(self):
        return f"{self.race}()"
    def selectThings(self):
        if self.race == "Warrior":
          weapons = [f"{weapon.value}-{weapon.name}" for weapon in Weapon]
          weapons = ", ".join(weapons[:-1]) + " or " + weapons[-1]
          choice = int(input(f"Choose your weapon {weapons}:  "))
          self.weapon = Weapon(choice)

        #Reminder here to make the stats become modified based on what equipment is selected
        #and that equipment can return as a string so that it can be output in descriptions.
          quit() 
        elif self.race == "Wizard":

          quit() 

        elif self.race == "Rogue":
          quit()

    
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
      playerStart()
    else: 
      print("Please enter a valid option.")

def playerStart():
  actions = ["Left","Right","Forward"]
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
      if player.race == "Wizard":
        wizardVsGhoul()
      elif player.race == "Rogue":
        rogueVsGhoul()
      elif player.race == "Warrior":
        warriorVsGhoul()  
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
        if player.race == "Wizard":
          wizardVsGhoul()
        elif player.race == "Rogue":
          rogueVsGhoul()
        elif player.race == "Warrior":
          warriorVsGhoul()  
    elif userInput == "Turn and run":
      print("You find the door has slammed closed behind you")
      ghoulGames()
    else: 
      print("Please enter a valid option.")



if __name__ == "__main__":
    
  while True:

      
    print("Welcome to the mystical land of Tabletopia")
    
    print("As an avid traveler, you have decided to visit the Catacombs of a nearby temple.")
    
    print("However, during your exploration, you find yourself lost.")
    
    print("Let's start with your name: ")
    
    name = input()
    
    print("Good luck, " +name+ ".")
    
    playeracterSelect()


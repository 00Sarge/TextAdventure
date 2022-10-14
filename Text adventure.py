advHlth = 10
advMana = 10
advStr = 10
advCha = 10
advInt = 10
advWis = 10
advDex = 10
advInv = []
advClass = ""

def checkForDead():
  if advHlth <= 0:
    print("You Have Died")
    quit()
  else:
    pass

#Should allow players to select their class, altering their base stats and equipment.

def characterSelect():
  classes = ["Warrior","Rogue","Wizard"]
  print("We'll need to start with your class. What kind of adventure are you?")
  userInput = ""
  while userInput not in classes:
    print("Options: Rogue/Warrior/Wizard")
    userInput = input()
    if userInput == "Rogue":
      advHlth = 12
      advMana = 5
      advStr = 10
      advCha = 12
      advInt = 14
      advWis = 16
      advDex = 16
      advInv.append("Cloak")
      advInv.append("Dagger")
      advClass = "Rogue"
      playerStart()
    elif userInput == "Wizard":
      advHlth = 10
      advMana = 10
      advStr = 8
      advCha = 12
      advInt = 18
      advWis = 12
      advDex = 10
      advInv.append("Staff")
      advInv.append("Fireball Spell")
      advClass = "Wizard"
      playerStart()
    elif userInput == "Warrior":
      advHlth = 15
      advMana = 0
      advStr = 18
      advCha = 10
      advInt = 8
      advWis = 10
      advDex = 12
      advInv.append("Greataxe")
      advInv.append("Chain Mail")
      advClass = "Warrior"
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
#upon completeing the games characters with a high wis stat can find a secret room
    
def ghoulGames():
  actions = ["Play along","Fight the ghoul","Turn and run"]
  print("'Welcome young,",advClass," to the Ghoul Games.' Announces an undead ringmaster")
  print("'To escape my room you must prove your worth in my obstacle course'")
  userInput = ""
  while userInput not in actions:
    print("Options: Play along/Fight the ghoul/Turn and run")
    userInput = input()
    if userInput == "Fight the ghoul":
      if advClass == "Wizard":
        wizardVsGhoul()
      elif advClass == "Rogue":
        rogueVsGhoul()
      elif advClass == "Warrior":
        warriorVsGhoul()  
    elif userInput == "Play along":
      if advDex > 10 and advStr > 10:
        print("Thanks to your athletcism you manage to duck, dodge, and weave through the obstacles")
        print("'Well done young ",advClass," take this amulet as a testament to your feat")
        advInv.append("Amulet of the fox")
        advDex = advDex + 2
        advWis = advWis + 2
        print("your inventory now contains ",advInv,"")
        if advWis < 18:
          print("A single door opens on the left wall of the room")
          longHallway()
        else:
          print("While you do notice a door open to the left that seems to obvious a route for catacomb such as this.")
          print("your trained eyes, now heightened by the amulet, notice the seems of a small trapdoor below the ringmaster.")
          print("Unable to resist the same curiosity that brought you deep underground you slip into the hatch, barely able")
          print("to hear the ringmaster's cries of protest behind you")
          treasureRoom()
      else:
        print("You make it part way through the course but you lose your grip on a rope and fall")
        print("partially into a pool of lava, singeing your leg")
        print("'Bah, what a poor showing. You must die for wasting my audience's valuable time'")
        advHlth = advHlth - 2
        if advClass == "Wizard":
          wizardVsGhoul()
        elif advClass == "Rogue":
          rogueVsGhoul()
        elif advClass == "Warrior":
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
    
    characterSelect()


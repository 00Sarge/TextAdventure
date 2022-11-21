 if self.name == "Wayne":
          print("Excellent choice sir, Batman mode activated")
          self.maxhp = 200
          self.hp = 200
          self.strength = 40
          self.dexterity = 40
          self.constitution = 40
          self.intelligence = 40
          self.wisdom = 40
          self.weapon = Weapons["BatFist"] 
          self.shield = None  
          self.tool = "GrapplingHook"
          self.spell = Spells["EclipticBeam"]
          self.resistance = "Fire"
          self.dmg = 20
          self.dmgType = None
          self.xp = 0 
          self.dmgStop = 10
          self.dmgBonus = 10
          calcStats()
          printStats()
        else:
myGrid = [[0,1,2,3,],
         [4,5,6,7,],
         [8,9,10,11]]
         
height = 100
width = 100

gridModel = [0] * height
nextGridModel = [0] * height


for i in range(height):
    gridModel[i] = [0] * width
    nextGridModel[i] = [0] * width

words = {}
words['large'] = {'definition':'Having much size.', 'synonyms':['big','volumous','grande'],'UseCount':5}
words['small'] = {'definition':'Having low size.', 'synonyms':['little','mini'],'UseCount':10}
words['gray'] = {'definition':'A neutral color that is neither black nor white.', 'synonyms':['grey','ash'],'UseCount':15}

def averageWordUse():
   total = 0
   for word in words:
      currentWord = words[word]
      total += currentWord['UseCount']
   return total / len(words)

print(averageWordUse())
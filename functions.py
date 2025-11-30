import random

blocks = [
  [
    [
      ["  ", "▒▒", "  "],
      ["▒▒", "▒▒", "▒▒"],
      ["  ", "  ", "  "],
    ], 
    [
      ["  ", "  ", "  "],
      ["▒▒", "▒▒", "▒▒"],
      ["  ", "▒▒", "  "],
    ], 
    [
      ["  ", "▒▒", "  "],
      ["  ", "▒▒", "▒▒"],
      ["  ", "▒▒", "  "],
    ], 
    [
      ["  ", "▒▒", "  "],
      ["▒▒", "▒▒", "  "],
      ["  ", "▒▒", "  "],
    ]
  ], 

  [
    [
      ["  ", "  ", "  ", "  "],
      ["▒▒", "▒▒", "▒▒", "▒▒"],
      ["  ", "  ", "  ", "  "],
      ["  ", "  ", "  ", "  "],
    ],
    [
      ["  ", "  ", "▒▒", "  "],
      ["  ", "  ", "▒▒", "  "],
      ["  ", "  ", "▒▒", "  "],
      ["  ", "  ", "▒▒", "  "],
    ],
    [
      ["  ", "  ", "  ", "  "],
      ["  ", "  ", "  ", "  "],
      ["▒▒", "▒▒", "▒▒", "▒▒"],
      ["  ", "  ", "  ", "  "],
    ],
    [
      ["  ", "▒▒", "  ", "  "],
      ["  ", "▒▒", "  ", "  "],
      ["  ", "▒▒", "  ", "  "],
      ["  ", "▒▒", "  ", "  "],
    ],
  ],

  [
    [
      ["▒▒", "▒▒"],
      ["▒▒", "▒▒"]
    ],
  ],
  
  [
    [
      ["▒▒", "  ", "  "],
      ["▒▒", "▒▒", "▒▒"],
      ["  ", "  ", "  "],
    ], 
    [
      ["  ", "▒▒", "▒▒"],
      ["  ", "▒▒", "  "],
      ["  ", "▒▒", "  "]
    ], 
    [
      ["  ", "  ", "  "],
      ["▒▒", "▒▒", "▒▒"],
      ["  ", "  ", "▒▒"],
    ], 
    [
      ["  ", "▒▒", "  "],
      ["  ", "▒▒", "  "],
      ["▒▒", "▒▒", "  "]
    ], 
  ],

  [
    [
      ["  ", "  ", "▒▒"],
      ["▒▒", "▒▒", "▒▒"],
      ["  ", "  ", "  "],
    ], 
    [
      ["  ", "▒▒", "  "],
      ["  ", "▒▒", "  "],
      ["  ", "▒▒", "▒▒"],
    ], 
    [
      ["  ", "  ", "  "],
      ["▒▒", "▒▒", "▒▒"],
      ["▒▒", "  ", "  "],
    ], 
    [
      ["▒▒", "▒▒", "  "],
      ["  ", "▒▒", "  "],
      ["  ", "▒▒", "  "]
    ], 
  ], 

  [
    [
      ["  ", "▒▒", "▒▒"],
      ["▒▒", "▒▒", "  "],
      ["  ", "  ", "  "],
    ], 
    [
      ["  ", "▒▒", "  "],
      ["  ", "▒▒", "▒▒"],
      ["  ", "  ", "▒▒"]
    ], 
  ],

  [
    [
      ["▒▒", "▒▒", "  "],
      ["  ", "▒▒", "▒▒"],
      ["  ", "  ", "  "],
    ], 
    [
      ["  ", "  ", "▒▒"],
      ["  ", "▒▒", "▒▒"],
      ["  ", "▒▒", "  "],
    ], 
  ]
]

class Block:
  def __init__(self, x, y, formationlist=None, formationid=None, formation=None, keydown=None):
    self.formationlist = random.choice(blocks)
    self.formation = random.choice(self.formationlist)
    
    self.formationid = self.formationlist.index(self.formation)
    self.x = x
    self.y = y
    self.keydown = keydown

  def notBottomOfBoard(self, boardmatrix):
    truex = self.x
    truey = self.y
    #value = False
    #print(truex, truey)
  
    xposused = []
    #checked = 0
  
    for i in range(len(self.formation)-1, -1, -1):
      for j in range(len(self.formation[0])):
        if self.formation[i][j] == "▒▒" and j not in xposused:
            xposused.append(j)
          
            if truey+i+1 > len(boardmatrix):
              return False
  
              
    return True

  def canSwitch(self, boardmatrix, truex, truey, formation): 
    #or just canswitch, in that case remove switching code and put in seperate fucntion
    #actually, yeah, no manually editing board, that's for update function to do
    #canswitch and not ifcanswitchthenswitch that makes it onot constant
    ogformationcoordinates = []
    
    for i in range(len(formation)):
      for j in range(len(formation[0])):
        ogformationcoordinates.append((i, j))
    
    if self.formationid == len(self.formationlist) - 1:
      newformation = self.formationlist[0]
    else:
      newformation = self.formationlist[self.formationid + 1]
      
    #if truex + len(newformation[0]) - 1 <= len(boardmatrix[0]) - 1 and truey + len(newformation) - 1 <= len(boardmatrix) - 1:
    
    #print(truex + len(newformation[0]) - 1, len(boardmatrix[0]) - 1)
    
    for i in range(len(newformation)):
      for j in range(len(newformation[0])):
        if newformation[i][j] == "▒▒":
          if truey+i > len(boardmatrix) - 1 or truex+j < 0 or truex+j > len(boardmatrix[0]) - 1:
            return False
          elif boardmatrix[truey+i][truex+j] == "▒▒" and (i, j) not in ogformationcoordinates:
            return False
 
    return True
    #return False
        
  
  def canMoveLeft(self, boardmatrix):

    # testing! remove and put back in parameter if faulty.
    truex = self.x
    truey = self.y
    formation = self.formation

    move = -1
    yposused = []
    #if truex != 0:
    for i in range(len(formation)):
      for j in range(len(formation[0])):
        if formation[i][j] == "▒▒" and i not in yposused:
          yposused.append(i)
          if truex+j+move < 0:
            return False
          if boardmatrix[truey+i][truex+j+move] == "▒▒":
            #print("THERES A BLOCK ON THE LEFT!!!!")
            return False
    return True
    #return False

  def changeformationdata(self):
    if self.formationid == len(self.formationlist) - 1:
      self.formationid = 0
    else:
      self.formationid += 1

    self.formation = self.formationlist[self.formationid]

  def canMoveRight(self, boardmatrix):

    # testing! remove and put back in parameter if faulty.
    truex = self.x
    truey = self.y
    formation = self.formation

    move = 1
    yposused = []
    #if truex + len(formation[0]) - 1 != len(boardmatrix[0]) - 1:
    for i in range(len(formation)):
      for j in range(len(formation[0])-1, -1, -1):
        if formation[i][j] == "▒▒" and i not in yposused:
          yposused.append(i)
          #print(truey + i, truex+j+move)
          if truex+j+move > len(boardmatrix[0]) - 1: #or <?
            return False
          if boardmatrix[truey+i][truex+j+move] == "▒▒":
              #print("THERES A BLOCK ON THE RIGHT!!!!")
            return False
    return True
    #return False

  def hasBlockUnder(self, boardmatrix):

    formation = self.formation
    truex = self.x
    truey = self.y
    #value = False
    #print(truex, truey)

    xposused = []
    checked = 0

    for i in range(len(formation)-1, -1, -1):
      for j in range(len(formation[0])):
        if formation[i][j] == "▒▒" and j not in xposused:
            
            xposused.append(j)

            if truey+i+1 > len(boardmatrix) - 1:
              return True

            if boardmatrix[truey+i+1][truex+j] == "▒▒":
              return True

              
    return False
    
def updateBlock(boardmatrix, formation, x, y):
    
  #8, 1
  truex = x #7
  truey = y #0

  for i in range(len(formation)):
    for j in range(len(formation[0])):
      if formation[i][j] == "▒▒":
        boardmatrix[truey+i][truex+j] = formation[i][j]

def clearBlockArea(boardmatrix, formation, x, y):
  #8, 1
  truex = x #7
  truey = y #0

  for i in range(len(formation)):
    for j in range(len(formation[0])):
      if formation[i][j] == "▒▒":
        boardmatrix[truey+i][truex+j] = ". "

def permanentlyPaste(boardmatrix, formation, x, y):
  truex = x #7
  truey = y #0

  for i in range(len(formation)):
    for j in range(len(formation[0])):
      if formation[i][j] == "▒▒":
        boardmatrix[truey+i][truex+j] = "▒▒"


def updateBoardIfFullRow(row, boardmatrix):
  for char in row:
    if char == ". ":
      return False

  temprow = []
  for i in range(len(boardmatrix[0])):
    temprow.append(". ")
  #print('creating inserting')
  boardmatrix.remove(row)
  boardmatrix.insert(0, temprow)
  #print('done')
  return True

'''
def updateBoardIfFullRow(boardmatrix):
  for row in boardmatrix:
    for char in row:
      if char == ". ":
        return "not full"

    temprow = []
    for i in range(len(boardmatrix[0])):
      temprow.append(". ")
    print('creating inserting')
    boardmatrix.remove(row)
    boardmatrix.insert(0, temprow)
    print('done')
    return "row indeed full"
'''
#try with break statement instead of return not full, cuz google said it only breaks out of one loop
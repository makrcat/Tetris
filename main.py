from functions import *
import time, os
db = {}

print("Loading..")

gameend = False
changexrequestamount = 0
changeyrequestamount = 0
quickdrop = False
formationswitchrequest = False

from pynput import keyboard

def on_activate_d():
  print("d clicked")
  global gameend, changexrequestamount, changeyrequestamount, quickdrop, formationswitchrequest
  changexrequestamount += 1

def on_activate_a():
  global gameend, changexrequestamount, changeyrequestamount, quickdrop, formationswitchrequest
  changexrequestamount += -1

def on_activate_w():
  global gameend, changexrequestamount, changeyrequestamount, quickdrop, formationswitchrequest
  formationswitchrequest = True

def on_activate_s():
  global gameend, changexrequestamount, changeyrequestamount, quickdrop, formationswitchrequest
  changeyrequestamount += 1

def on_activate_dot():
  global gameend, changexrequestamount, changeyrequestamount, quickdrop, formationswitchrequest
  quickdrop = True

listener = keyboard.GlobalHotKeys({
  'd': on_activate_d,
  'a': on_activate_a,
  'w': on_activate_w,
  's': on_activate_s,
  '.': on_activate_dot})

listener.start()

def game():
  global changexrequestamount, changeyrequestamount, formationswitchrequest, quickdrop, gameend

  # intialize game variables & stuff
  # next block
  nextformationlist = random.choice(blocks)
  nextformation = random.choice(nextformationlist)
    
  # some default variables
  rows_hit = 0
  score = 0
  level = 0
  
  # stuff to display & stuff to configure
  board = []
  addedrows = 3 # these are for on top
  frame = 0
  fps = 30 # [chore: only update when user press]
  blockfallspeed = fps/2

  # print the first rows
  for i in range(20 + addedrows):
    row = []
    for j in range(10):
      row.append(". ")
    board.append(row)
    
  # make a block to fall
  activeblock = Block(0, 0)
  activeblock.x = random.randint(0, len(board[0])-len(activeblock.formation[0]))
    
  # run the rest of the game
  while True:

    # if the game has ended, break out of the loop
    if gameend == True:
      print("Game Over! \n\n\r")
      break
      
    # frame increment
    frame += 1

    # move left request, move (if available)
    if changexrequestamount < 0 and activeblock.canMoveLeft(board):
      activeblock.x += changexrequestamount
      changexrequestamount = 0
    # else reset the request
    elif changexrequestamount < 0:
      changexrequestamount = 0
      
    # move right request, move (if available)
    if changexrequestamount > 0 and activeblock.canMoveRight(board):
      activeblock.x += changexrequestamount
      changexrequestamount = 0
    # else reset the request
    elif changexrequestamount > 0:
      changexrequestamount = 0

    # soft drop request (if available)
    if changeyrequestamount != 0 and not activeblock.hasBlockUnder(board):
      activeblock.y += 1
      changeyrequestamount = 0
    # else reset request (usually not needed just a safety check)
    # this actually isn't needed as much, since if it isn't available, a new block is probably spawning
    elif changeyrequestamount != 0:
      changeyrequestamount = 0

    # switch formation
    if formationswitchrequest == True and activeblock.canSwitch(board, activeblock.x, activeblock.y, activeblock.formation):
      activeblock.changeformationdata()
      formationswitchrequest = False
    # can't switch right now!
    elif formationswitchrequest == True:
      formationswitchrequest = False

    # drop until stop!
    if quickdrop == True:
      while not activeblock.hasBlockUnder(board):
        activeblock.y += 1
      quickdrop = False

    # drop every [drop fps] frames
    if frame % blockfallspeed == 0: 
      if activeblock.notBottomOfBoard(board) and not activeblock.hasBlockUnder(board):
        activeblock.y += 1
        
    # reached the end of the drop! Paste block, generate new.
    if activeblock.hasBlockUnder(board):
      permanentlyPaste(board, activeblock.formation, activeblock.x, activeblock.y)
      for row in board:
        a = updateBoardIfFullRow(row, board)
        if a == True:
          rows_hit += 1
          level = rows_hit // 10 #yes
          # fall speed get faster
          blockfallspeed = round(blockfallspeed*0.95)
          # I think this is tetris rules?
          score += 10 * level

      score += 10

      # make a new block. (from the generated formation list)
      activeblock = Block(0, 0)
      activeblock.formationlist = nextformationlist
      activeblock.formation = nextformation
      activeblock.formationid = activeblock.formationlist.index(activeblock.formation) #pleaseee
      activeblock.x = random.randint(0, len(board[0])-len(activeblock.formation[0]))

      # generate new block for next time
      nextformationlist = random.choice(blocks)
      nextformation = random.choice(nextformationlist)

    # if the board is filled,
    for char in board[addedrows - 1]:
      if char == "▒▒":
        gameend = True
        break
    
    # update the block and paste on screen (I think)
    updateBlock(board, activeblock.formation, activeblock.x, activeblock.y)

    # do a check? if no update, no updating.
    # then everything under is irrelevant yeah

    deepcopiedformation = []
    for i in range(len(nextformation)):
      deepcopiedformation.append("".join(nextformation[i]))

    # print the board!
    chonk = " ______________________ \r\n"
    for i in range(addedrows, len(board)): 
      if i != len(board):
        chonk += "｜"+"".join(board[i])+"｜" 
        
        if i == addedrows + 0:
          chonk += "   Rows hit: {}".format(rows_hit)
        elif i == addedrows + 1:
          chonk += "   Score: {}".format(score)
        elif i == addedrows + 2:
          chonk += "   Level: {}".format(level)

        elif i == 8:
          chonk += "   -- Next Block --"
        
        elif i >= 10 and 0 <= i - 10 < len(deepcopiedformation):
          chonk += "   {}".format(deepcopiedformation[i - 10])
   
        elif i == 19:
          chonk += "   [W] - rotate"
        elif i == 20:
          chonk += "   [A/D] - left/right"
        elif i == 21:
          chonk += "   [S] - soft drop"
        elif i == 22:
          chonk += "   [.] - hard drop"
        chonk += "\n\r"
      else:
        chonk += "".join(board[i])

    chonk += " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ "
    print(chonk+"\n\r")

    clearBlockArea(board, activeblock.formation, activeblock.x, activeblock.y)
    time.sleep(1/fps)
    #input() I am literally praying.
    os.system("clear")


print('''
,--------.,------.,--------.,------. ,--. ,---.   
'--.  .--'|  .---''--.  .--'|  .--. '|  |'   .-'  
   |  |   |  `--,    |  |   |  '--'.'|  |`.  `-.  
   |  |   |  `---.   |  |   |  |\  \ |  |.-'    | 
   `--'   `------'   `--'   `--' '--'`--'`-----'  
                                                ''')
input("Press [ENTER] to play.")

os.system("clear")

game()



def checkLeftValid():
    global left, right
    #print(left[1], left[0])
    
    if  len(left[1]) > len(left[0]) and len(left[0]) >0:
       
        print("missionary eaten on left side")
        return False
        
        
    else:
        print("left is ok")
        return True
         
         
         
def checkRightValid():
    global left, right
    #print(right[1], right[0])
    
    if  len(right[1]) > len(right[0]) and len(right[0]) >0:
       
        print("missionary eaten on right side")
        return False
        
        
    else:
        print("right is ok")
        return True
        
        
def toRight():
    global left, right
    print(len(left[1]))
    
    validBoat = False
    while validBoat == False:
        print("The boat is on the left bank. It is going to the right bank")
        print("The boat holds 2:")
        boatTotal = 0
        m=0
        c=0
            
        m = int(input("how many missionaries: "))
        boatTotal += m
        
        if boatTotal < 2:
            c = int(input("how many cannibals: "))
            boatTotal += c
        if (boatTotal == 1 or boatTotal == 2) and c <= len(left[1]) and m <= len(left[0]):
            print("valid entry")
            validBoat = True
        else:
            print("NOT A VALID ENTRY")
            showState()
         
    print("m = ",m,"c = ",c)
    for i in range(m):
        left[0].pop()
        right[0].append('m')
        
    for i in range(c):
        left[1].pop()
        right[1].append("c")
        
     
    showState()
     
     
def toLeft():
    global left, right
    print(len(left[1]))
    
    validBoat = False
    while validBoat == False:
        print("The boat is on the RIGHT bank. It is going to the LEFT bank")
        print("The boat holds 2:")
        boatTotal = 0
        m=0
        c=0
            
        m = int(input("how many missionaries: "))
        boatTotal += m
        
        if boatTotal < 2:
            c = int(input("how many cannibals: "))
            boatTotal += c
        if (boatTotal == 1 or boatTotal == 2) and c <= len(right[1]) and m <= len(right[0]):
            print("valid entry")
            validBoat = True
        else:
            print("NOT A VALID ENTRY")
            showState()
         
    print("m = ",m,"c = ",c)
    for i in range(m):
        right[0].pop()
        left[0].append('m')
        
    for i in range(c):
        right[1].pop()
        left[1].append("c")
    
    showState()
        
   
    
    
    
def showState():
    
    print("/"*50)
    print("left Side",left)
    print("~-"*20)
    print("-~"*20)
    print("~-"*20)
    print("-~"*20)
    print("right Side",right)
    print("/"*50)
    


def checkWin():
    if len(right[0])==3 and len(right[1])==3:
        print("YOU WIN")
        return True
    else:
        return False
    
def compMoveRight(m,c):
    for i in range(m):
        left[0].pop()
        right[0].append('m')
        
    for i in range(c):
        left[1].pop()
        right[1].append("c")
        
    showState()
        
def compMoveLeft(m,c):
    for i in range(m):
        right[0].pop()
        left[0].append('m')
        
    for i in range(c):
        right[1].pop()
        left[1].append("c")
        
    showState()
        
        
def compCurrState():
    
    global x, y
    currState = allStates[y][x]
    print("the current State :", currState)
    
def compToRight():
    # move from left bank to right bank usually by 2
    global x, y, left, right
    
    currState = allStates[y][x]
    ## initial tests are really to  make sure they are not out of range of array
    # subtract y by 2
    if y >=2:
        test1state = allStates[y-2][x]
        ml, mr, cl, cr = getValsForState(test1state)
        print("bing")
        print(ml, cl, mr, cr)
        if (ml >= cl or ml == 0) and (mr >=cr or mr == 0):
            print("this is a valid move y-2", test1state)
            y = y - 2
            compMoveRight(0,2)
            return
    # subtract x by 2  cannot use an  else if both testing cases can be true
    if x >=2:
        test1state = allStates[y][x-2]
        ml, mr, cl, cr = getValsForState(test1state)
        print("bang")
        print(ml, cl, mr, cr)
        if (ml >= cl or ml == 0) and (mr >=cr or mr == 0):
            print("this is a valid move x-2 ", test1state)
            x = x - 2
            compMoveRight(2,0)
            return
    # subtract x  by 1 y by 1  
    else:
        test1state = allStates[y-1][x-1]
        ml, mr, cl, cr = getValsForState(test1state)
        print(ml, cl, mr, cr)
        if (ml >= cl or ml == 0) and (mr >=cr or mr == 0):
            print("this is a valid move x-1 y-1", test1state)
            x = x - 1
            y = y - 1
            compMoveRight(1,1)
            return




def compToLeft():
    # move from right bank to left bank / returning the boat
    global x, y, left, right
    
    currState = allStates[y][x]
    
    # add one y  return with cannibal
    test1state = allStates[y+1][x]
    ml, mr, cl, cr = getValsForState(test1state)
    print("bing")
    print(ml, cl, mr, cr)
    if (ml >= cl or ml == 0) and (mr >=cr or mr == 0):
        print("this is a valid move y+1", test1state)
        y = y +1
        compMoveLeft(0,1)
        return
    # add x by 1
    
    test1state = allStates[y][x+1]
    ml, mr, cl, cr = getValsForState(test1state)
    print("bang")
    print(ml, cl, mr, cr)
    if (ml >= cl or ml == 0) and (mr >=cr or mr == 0):
        print("this is a valid move x+1 ", test1state)
        x = x +1
        compMoveLeft(1,0)
        return
    # subtract x  by 1 y by 1  
     
    test1state = allStates[y+1][x+1]
    ml, mr, cl, cr = getValsForState(test1state)
    print(ml, cl, mr, cr)
    if (ml >= cl or ml == 0) and (mr >=cr or mr == 0):
        print("this is a valid move x+1 y+1", test1state)
        x = x + 1
        y = y + 1
        compMoveLeft(1,1)
        return        
         
        
def getValsForState(state):
    missLeft = state[0]
    missRight = abs(state[0] - 3)
    cannLeft = state[1]
    cannRight = abs(state[1] - 3)
    return missLeft, missRight, cannLeft, cannRight

# first the computer solves the problem using the
# graphing all possible states cannibals (y axis) to missionarys (x axis)
# the boats movement is


x= 3
y=3

 

# left[0] = len(left[0]) is the number of missionaries
# lett[1] = len(left[1]) is the number of cannibals
left = [["m","m","m"],["c","c","c"]]

right =[[],[]]
 
# in computer cooridinates (not standard cartesian)  y increacing downwad
# see my paper gameboard solution in standard cartesian coordinates
allStates = [
    
                [(0,0),(1,0),(2,0),(3,0)],
                [(0,1),(1,1),(2,1),(3,1)],
                [(0,2),(1,2),(2,2),(3,2)],
                [(0,3),(1,3),(2,3),(3,3)]
             
             ]

print("*"*50)
print(" computer "*5)
print("*"*50)


while True:
    compCurrState()
    ## win on a move right so you must check after it
    compToRight()
    if allStates[y][x] == (0,0):
        break
    compCurrState()
    compToLeft()
    
    
# now the interactive

left = [["m","m","m"],["c","c","c"]]

 
right =[[],[]]

print("*"*50)
print(" interactive "*5)
print("*"*50)


while True:
 
    showState()
    
    toRight()
    if checkLeftValid() == False:
        break
        
    if checkRightValid() == False :
        break
    if checkWin():
        break
    
    toLeft()
    if checkLeftValid() == False:
        break
        
    if checkRightValid() == False :
        break
    if checkWin():
        break
     

import numpy as np
import random as rd
#N,M
Positions = ['U','D','R','L']
SmartShow = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
SmartShow = np.array(SmartShow)
SmartArray = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
SmartPosition = ([[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]])
for i in range(1,5):
    for j in range(1,5):
        SmartArray[i][j] = rd.choice(np.arange(1,5,1))
        Positions = ['U','D','R','L']
        for k in range(SmartArray[i][j]):
            SmartPosition[i][j].append(rd.choice(Positions))
            Positions = [x for x in Positions if (x != SmartPosition[i][j][-1])]

for j in range(1,5):
    Positions = ['D','R','L']
    SmartArray[0][j] = rd.choice(np.arange(1,4,1))
    for k in range(SmartArray[0][j]):
            SmartPosition[0][j].append(rd.choice(Positions))
            Positions = [x for x in Positions if (x != SmartPosition[0][j][-1])]
    SmartArray[5][j] = rd.choice(np.arange(1,4,1))
    Positions = ['U','R','L']
    for k in range(SmartArray[5][j]):
            SmartPosition[5][j].append(rd.choice(Positions))
            Positions = [x for x in Positions if (x != SmartPosition[5][j][-1])]
    SmartArray[j][0] = rd.choice(np.arange(1,4,1))
    Positions = ['U','D','R']
    for k in range(SmartArray[j][0]):
            SmartPosition[j][0].append(rd.choice(Positions))
            Positions = [x for x in Positions if (x != SmartPosition[j][0][-1])]
    SmartArray[j][5] = rd.choice(np.arange(1,4,1))
    Positions = ['U','D','L']
    for k in range(SmartArray[j][5]):
            SmartPosition[j][5].append(rd.choice(Positions))
            Positions = [x for x in Positions if (x != SmartPosition[j][5][-1])]
Positions = ['D','R']
SmartArray[0][0] = rd.choice([1,2])
for k in range(SmartArray[0][0]):
    SmartPosition[0][0].append(rd.choice(Positions))
    Positions = [x for x in Positions if (x != SmartPosition[0][0][-1])]
Positions = ['D','L']
SmartArray[0][5] = rd.choice([1,2])
for k in range(SmartArray[0][5]):
    SmartPosition[0][5].append(rd.choice(Positions))
    Positions = [x for x in Positions if (x != SmartPosition[0][5][-1])]    
Positions = ['U','R']
SmartArray[5][0] = rd.choice([1,2])
for k in range(SmartArray[5][0]):
    SmartPosition[5][0].append(rd.choice(Positions))
    Positions = [x for x in Positions if (x != SmartPosition[5][0][-1])]
Positions = ['U','L']
SmartArray[5][5] = rd.choice([1,2])
for k in range(SmartArray[5][5]):
    SmartPosition[5][5].append(rd.choice(Positions))
    Positions = [x for x in Positions if (x != SmartPosition[5][5][-1])]

for i in range(6):
    for j in range(6):
        SmartPosition[i][j] = sorted(SmartPosition[i][j])

print (sorted(['U','L','D','R']))
RandomStart1 = rd.choice(range(36))
RandomStart2 = rd.choice([x for x in range(36) if (x != RandomStart1)])
SmartShow[RandomStart1//6][RandomStart1%6] = SmartArray[RandomStart1//6][RandomStart1%6]
SmartShow[RandomStart2//6][RandomStart2%6] = SmartArray[RandomStart2//6][RandomStart2%6]
SUM = 0
def fixArray (i,j):
    for k in SmartPosition[i][j]:
        if (k == 'D' and SmartShow[i+1][j] != 0):
            SmartArray[i][j] -= 1 
            SmartPosition[i][j] = [x for x in SmartPosition[i][j] if (x != 'D')]
        if (k == 'L' and SmartShow[i][j-1] != 0):
            SmartArray[i][j] -= 1
            SmartPosition[i][j] = [x for x in SmartPosition[i][j] if (x != 'L')]
        if (k == 'R' and SmartShow[i][j+1] != 0):
            SmartArray[i][j] -= 1
            SmartPosition[i][j] = [x for x in SmartPosition[i][j] if (x != 'R')]
        if (k == 'U' and SmartShow[i-1][j] != 0):
            SmartArray[i][j] -= 1
            SmartPosition[i][j] = [x for x in SmartPosition[i][j] if (x != 'U')]


def opencell (i,j):
    global SUM 
    SUM += SmartArray[i][j]
    for k in range(SmartArray[i][j]):
        current =  SmartPosition[i][j].pop()
        if (current == 'D'):
            fixArray(i+1,j)
            SmartShow[i+1][j] = SmartArray[i+1][j]
        if (current == 'L'):
            fixArray(i,j-1)
            SmartShow[i][j-1] = SmartArray[i][j-1]
        if (current == 'R'):
            fixArray(i,j+1)
            SmartShow[i][j+1] = SmartArray[i][j+1]
        if (current == 'U'):
            fixArray(i-1,j)
            SmartShow[i-1][j] = SmartArray[i-1][j]
#opencell(RandomStart1//6,RandomStart1%6)
print (SUM)
print (SmartShow)
Connection = ""
while (Connection != "Stop"):
    i = input("Input X position of the cell.\n")
    j = input("Input Y position of the cell.\n")
    opencell(int(i),int(j))
    print (SUM)
    print (SmartShow)
    Connection = input('Press "Play" or "Stop"\n')


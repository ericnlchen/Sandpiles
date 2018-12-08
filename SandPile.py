import matplotlib.pylab as plt

#Create sandpile:
rows=int(input('How many rows? '))
columns=int(input('How many columns? '))
toppleSize=int(input('What is the maximum size of a sandpile? '))
sandPile=[]
for y in range(rows):
    sandPile.append([])
    for x in range(columns):
        sandPile[y].append(0)

#Change sand values:
flag=True
while flag==True:
    x = int(input('X-coordinate of sand you want to change? '))
    y = int(input('Y-coordinate of sand you want to change? '))
    val = int(input('How much sand do you want? '))
    sandPile[y][x] = val
    changeFlag = input('To change another, type y. ')
    if changeFlag!='y':
        flag=False

#Print sandpile:
for i in sandPile:
    print('')
    for j in i:
        print(j, end=' ')
print('')

#Topple:
toppleFlag=True
while toppleFlag==True:
    for i in range(len(sandPile)):
        for j in range(len(sandPile[i])):
            if sandPile[i][j] >= toppleSize:
                sandPile[i][j+1]+=1
                sandPile[i][j]-=1
                sandPile[i][j-1]+=1
                sandPile[i][j]-=1
                sandPile[i+1][j]+=1
                sandPile[i][j]-=1
                sandPile[i-1][j]+=1
                sandPile[i][j]-=1
    toppleFlag=False
    for i in sandPile:
        for j in i:
            if j>=toppleSize:
                toppleFlag=True

#Print result:
for i in range(len(sandPile)):
    for j in range(len(sandPile[i])):
        if sandPile[i][j] == 0:
            plt.plot(i,j,'bs', markersize = 5)
        elif sandPile[i][j] == 1:
            plt.plot(i,j,'gs', markersize = 5)
        elif sandPile[i][j] == 2:
            plt.plot(i,j,'ys', markersize = 5)
        else:
            plt.plot(i,j,'rs', markersize = 5)

plt.gca().set_aspect('equal', adjustable='box')
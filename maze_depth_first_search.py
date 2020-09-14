maze = [
    [1,1,0,0,1],
    [0,1,1,1,1],
    [0,1,0,0,1],
    [1,1,1,0,0],
    [1,0,1,1,1]
]

sol = [[ 0 for i in range(5)] for j in range(5)]

x=0
y=0

def solvemaze(maze,x,y,sol):
    if(x==4 and y ==4):
        sol[x][y]=1
        return True
    
    if(-1<x<5)and(-1<y<5)and(maze[x][y]==1)and(sol[x][y]!=1):
        sol[x][y]=1

        if solvemaze(maze,x+1,y,sol)==True:
            return True
        
        if solvemaze(maze,x-1,y,sol)==True:
            return True

        if solvemaze(maze,x,y-1,sol)==True:
            return True

        if solvemaze(maze,x,y+1,sol)==True:
            return True

        sol[x][y]=0
        return False

    return False

solvemaze(maze,x,y,sol)
for i in sol:
    print(i)

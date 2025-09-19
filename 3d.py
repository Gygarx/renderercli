import math, time, os

testvert = [[0,0,0]]

vertices = [
    [10, -20, 0],
    [-10, 10, 0],
    [10,  10, 0]
]

indices = [0,1,2]

nodeOn = True

def initRendering():
    rednerMatrix = createRenderMatrix(49,49)
    return rednerMatrix

def createRenderMatrix(x,y):
    matrix = []
    for xlocal in range(x):
        matrix.append([])
        for ylocal in range(y):
            matrix[xlocal].append("   ")
    
    #fps limiter
    
            
    return matrix

def draw(matrix,ver,ind,fov):
    mX = len(matrix)
    mY = len(matrix[0])
    
    cX = math.floor(mX/2)
    cY = math.floor(mY/2)
    
    for vert in ver:
        matrix[(vert[1]+cY)][(vert[0]+cX)] = " X "
        
    for i in range(0,len(ind)):
        v1 = ver[i]
        try:
            v2 = ver[i+1]
        except:
            v2 = ver[0]
            
        y1 = v1[1]
        y2 = v2[1]
        
        x1 = v1[0]
        x2 = v2[0]
        
        if (x2-x1) == 0:
            m = 0
        else: 
            m = (y2-y1) / (x2-x1)
        
        stepY = m*-1
        stepX = 1
        
        if x1 > x2:
            stepX = -1
        
        nextVert = [x1+stepX,y1+stepY,v1[2]] 
        while not (nextVert[0] == x2 and nextVert[1] == y2):
        #for l in range(3):
            nextVert = [x1+stepX,y1+stepY,v1[2]] 
            x1+=stepX
            y1+=stepY
        
            matrix[int(nextVert[1]+cY)][int(nextVert[0]+cX)] = " X "
            print(nextVert)

        
        print(v1,v2, m, nextVert)
        
        
    
    
    

def renderLoop(renderMatrix):
    firstLoop = True
    while nodeOn:
        if firstLoop:
            newTimeCurrent  = time.time()
            firstLoop = False
        
        lastTimeCurrent = newTimeCurrent
        newTimeCurrent  = time.time()
        
        
        os.system("clear")
        
        
        draw(renderMatrix,vertices,indices,1)
        
        #rendering
        for pixel in renderMatrix:
            for subPixel in pixel:
                print(subPixel,end="")
            print("")
        print(f"FPS={round(1/(newTimeCurrent - lastTimeCurrent),1)} Frame Time={round(newTimeCurrent - lastTimeCurrent,2)}")
        
        
        time.sleep(0.085)


def main():
    
    renderLoop(initRendering())
    
    
main()
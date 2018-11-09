import math
import random


def generatePolygon(ctrX, ctrY, aveRadius=0, irregularity=0, spikeyness=0, numVerts=0):
    numVerts = numVerts or random.randint(100, min(ctrX, ctrY))
    aveRadius = aveRadius or random.randint(100, max(ctrX, ctrY))
    irregularity = irregularity or random.randint(50, aveRadius)*random.randint(100,1000)
    spikeyness = spikeyness or random.randint(50, aveRadius)*random.randint(100,1000)

    # generate n angle steps
    angleSteps = []
    lower = (2*math.pi / numVerts) - irregularity
    upper = (2*math.pi / numVerts) + irregularity
    sum = 0
    for i in range(numVerts):
        tmp = random.uniform(lower, upper)
        angleSteps.append(tmp)
        sum = sum + tmp

    # normalize the steps so that point 0 and point n+1 are the same
    k = sum / (2*math.pi)
    for i in range(numVerts):
        angleSteps[i] = angleSteps[i] / k

    # now generate the points
    points = []
    angle = random.uniform(0, 2*math.pi)
    for i in range(numVerts):
        r_i = clip(random.gauss(aveRadius, spikeyness), 0, 2*aveRadius)
        x = ctrX + r_i*math.cos(angle)
        y = ctrY + r_i*math.sin(angle)
        points.append((int(x), int(y)))
        angle = angle + angleSteps[i]

    # random.shuffle(points)
    return points


def clip(x, min, max):
    if(min > max):
        return x
    elif(x < min):
        return min
    elif(x > max):
        return max
    else:
        return x


if __name__ == '__main__':
    verts = generatePolygon(ctrX=250, ctrY=250, aveRadius=100,
                            irregularity=0, spikeyness=0, numVerts=100)
    tupVerts = list(map(tuple, verts))
    print(tupVerts)

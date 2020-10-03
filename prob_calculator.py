import copy
import random
import math
# Consider using the modules imported above.

class Hat(object):
    def __init__(self, red=0, orange=0, yellow=0, blue=0, green=0, pink=0, striped=0, black=0):
        self.red = red
        self.orange = orange
        self.yellow = yellow
        self.blue = blue
        self.green = green
        self.pink = pink
        self.striped = striped
        self.black = black
        self.hat = {'red':red, 'orange':orange, 'yellow':yellow, 'blue':blue, 'green':green, 'pink':pink, 'striped':striped, 'black':black}
        #self.contents = []
        self.contents = self.getContents()
        self.numBalls = self.getNumBalls()
        if self.numBalls == 0: self.addBalls(1)
    def __str__(self):
        return self.contents
    def getNumBalls(self):
        # Returns the number of balls in the hat
        numBalls = 0      
        for value in self.hat.values():
            numBalls += value        
        return numBalls
    def getContents(self):
        # Generates a list of strings of the balls in the hat
        self.contents = []
        for key in self.hat.keys():
            if self.hat[key] == 0:
                #print('No ' + str(key) + ' balls in hat.')
                pass
            else:
                # print(str(self.hat[key]) + ' ' + str(key) + ' balls in hat.')
                for i in range(self.hat[key]):
                    self.contents.append(str(key))
                    #print(str(i) + ' ' + str(key))
        return self.contents
    def addBalls(self,numBalls):
        # Adds balls into the hat
        balls = ['red', 'orange', 'yellow', 'blue', 'green', 'pink', 'striped', 'black']
        b = 0
        for i in balls:
            b += 1
        
        for i in range(numBalls):
            r = math.floor(random.random()*10%b)
            #print(str(balls[r]))
            self.hat[balls[r]] += 1
            #print(str(self.hat[balls[r]]))
        return None  
    def draw2(self,numDrawn):
        # Draws a specific number of balls from the hat and moves them in to a new list of strings.
        copy_contents = copy.copy(self.contents)
        hatCopy = copy_contents
        totBalls = self.getNumBalls()
        ballsDrawn = []
        if numDrawn >= totBalls:
            ballsDrawn = hatCopy
        else:
            for i in range(numDrawn):
                # pick a random ball from the copy hat
                r = math.floor(random.random()*10%totBalls)
                #print(str(r))
                #print((hatCopy[r]))
                ballsDrawn.append(hatCopy[r])
                #print((ballsDrawn))
                # delete the ball from the copy hat
                hatCopy.remove(hatCopy[r])
                #print('updated copy: '+str(hatCopy))
                # decrement the number of balls in the copy hat
                totBalls -= 1
        return ballsDrawn
    def draw(self,numDrawn):
        # Draws a specific number of balls from the hat and moves them in to a new list of strings.
        copy_contents = copy.copy(self.contents)
        hatCopy = copy_contents
        totBalls = self.getNumBalls()
        ballsDrawn = []
        if numDrawn >= totBalls:
            ballsDrawn = hatCopy
        else:
            for i in range(numDrawn):
                # pick a random ball from the copy hat
                r = math.floor(random.random()*10%totBalls)
                #print(str(r))
                #print((hatCopy[r]))
                ballsDrawn.append(hatCopy[r])
                #print((ballsDrawn))
                # delete the ball from the copy hat
                hatCopy.remove(hatCopy[r])
                #print('updated copy: '+str(hatCopy))
                # decrement the number of balls in the copy hat
                totBalls -= 1
        # change the hat, need a method to go from contents to hat
        self = hatFromContents(hatCopy)
        return ballsDrawn
def hatFromContents(contents):
    emptyHat = {'red':0, 'orange':0, 'yellow':0, 'blue':0, 'green':0, 'pink':0, 'striped':0, 'black':0}
    for i in contents:
        emptyHat[i] += 1
    #print(str(emptyHat))
    hat = Hat(red=emptyHat['red'],orange=emptyHat['orange'],yellow=emptyHat['yellow'],blue=emptyHat['blue'],green=emptyHat['green'],pink=emptyHat['pink'],striped=emptyHat['striped'],black=emptyHat['black'])
    return hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    drawn = []
    drawnDict = {'red':0, 'orange':0, 'yellow':0, 'blue':0, 'green':0, 'pink':0, 'striped':0, 'black':0}
    for i in range(num_experiments):
        m = 0
        count = 0
        drawnDict = {'red':0, 'orange':0, 'yellow':0, 'blue':0, 'green':0, 'pink':0, 'striped':0, 'black':0}
        copy_hat = copy.copy(hat)
        drawn = copy_hat.draw(num_balls_drawn)
        #print(drawn)
        # store the drawn balls in a dictionary to compare with expected balls
        for b in drawn:
            #print(str(drawnDict[b]))
            drawnDict[b] += 1
        #print(str(drawnDict))
        for key in expected_balls.keys():
            count += 1
            #print(str(key))
            #print('Expected: '+str(expected_balls[key]))
            #print('Drawn: '+str(drawnDict[key]))
            if expected_balls[key] <= drawnDict[key]:
                m += 1
            else:
                break
        #print('m: '+str(m))
        #print('count: '+str(count))
        if m == count:
            M += 1
            #print('increnented M: '+str(M))
   
    #print('final M: '+str(M))
    probability = M/num_experiments
    return probability

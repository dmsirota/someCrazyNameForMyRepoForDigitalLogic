from util import *

class Player(object):
    """
    player class. 
    
    To test your own machine player strategy, you should implement the ```make_decision()``` method. 
    To test your implementation, you should modify the configy.py to set one or two player(s) as 'machine' 
    """

    def __init__(self, id, name=None):
        self.points=0
        self.id=id
        self.name=name if name else 'player'+str(id)
        self.add = lambda val,rand: (val+rand) % 16
        self.replace = lambda val,rand: rand % 16
        self.skip = lambda val, rand: val

    def make_decision(self, four_bits, next_randoms, code_digits):
        """
        This function decide next move of the machine player.

        You should only modify '#Your Code is Here' to define your own machine player.
        To enable your machine player, please check & modify the configuration in config.py.

        Args:
            four_bits (int[]): the four bit number in the LED 
            next_randoms (int[]): the next 3 random digits
            code_digits(int[]): 2 code digits.
        Returns:
            operation: [self.skip | self.add | self.replace]
            selected: [0|1|2|3]
        """
        
        operation = self.skip
        selected = 0
        #Your Code is Here
        # tuple[0] = val; tuple[1] = pos
        currMax = [0,0]
        dirMax = [0,0]
        for i in range(4):
            numAdj = 0
            tempSum = next_randoms[0] + four_bits[i]
            # test for adj
            if i == 0:
                adjLst = [1,2,3]
                for j in adjLst:
                    if tempSum % 16 == four_bits[j]:
                        numAdj += 1
                    else:
                        break
            elif i == 1:
                for j in [0,2,3]:
                    if tempSum % 16 == four_bits[j]:
                        numAdj += 1
                    else:
                        if j == 2:
                            break
            elif i == 2:
                for j in [3,1,0]:
                    if tempSum % 16 == four_bits[j]:
                        numAdj += 1
                    else:
                        if j == 1:
                            break
            elif i == 3:
                for j in [2,1,0]:
                    if tempSum % 16 == four_bits[j]:
                        numAdj += 1
                    else:
                        break
            
            pts = (tempSum % 16) * (2**numAdj)
            if pts >= currMax[0]:
                currMax[0] = pts
                currMax[1] = i

        # test for direct insertion
        for i in range(4):
            val = next_randoms[0]
            if i == 0:
                adjLst = [1,2,3]
                for j in range(1,4):
                    if val == four_bits[j]:
                        numAdj += 1
                    else:
                        break
            elif i == 1:
                for j in [0,2,3]:
                    if val == four_bits[j]:
                        numAdj += 1
                    else:
                        if j == 2:
                            break
            elif i == 2:
                for j in [3,1,0]:
                    if val == four_bits[j]:
                        numAdj += 1
                    else:
                        if j == 1:
                            break
            elif i == 3:
                for j in [2,1,0]:
                    if val == four_bits[j]:
                        numAdj += 1
                    else:
                        break
            pts = (tempSum % 16) * (2**numAdj)
            if pts >= dirMax[0]:
                dirMax[0] = pts
                dirMax[1] = i

        if dirMax > currMax:
            operation = self.replace
            selected = dirMax[1]
        else:
            operation = self.add
            selected = currMax[1]
                
        return operation, selected

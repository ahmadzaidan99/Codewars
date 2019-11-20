import math
def find_next_square(sq):
    sr=math.sqrt(sq)
    if((sr - math.floor(sr)) == 0):return (sr+1)**2 #Checking if it's a perfect square
    else: return -1

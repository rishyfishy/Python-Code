import math
def isInt(number:float)->bool:
    return ((math.floor(number)==number) or (math.ceil(number)==number))
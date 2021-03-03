import math
def vector_longitude(x=int(input("enter  x")),y=int(input("enter  y")),z=int(input("enter  z"))):

    return(math.sqrt(x**x+y**y+z**z))

print(vector_longitude())
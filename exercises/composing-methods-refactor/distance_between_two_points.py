# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math
circle1_x = 4
circle1_y = 4.25

circle2_x = 53
circle2_y = -5.35


# Calculate the distance between the two circle
def circle_distance(circle1_x,circle1_y,circle2_x,circle2_y):
    distance = math.sqrt((circle1_x-circle2_x)**2 + (circle1_y - circle2_y)**2)
    print('distance', distance)


# *** somewhere else in your program ***
xa = -36
ya = 97

xb = .34
yb = .91

def vector_distance(xa,ya,xb,yb):
    # calcualte the length of vector AB vector which is a vector between A and B points.
    length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
    print('length', length)

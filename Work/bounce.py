# bounce.py
#
# Exercise 1.5
bounce = 0
height = 100

while bounce < 10:
    newHeight = height * 0.6
    height = newHeight
    print(round(newHeight, 4))
    bounce+= 1
    


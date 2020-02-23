import random
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create("192.168.1.15")

# Add the count variable here
u = 0
# Start the while loop here
while u < 1:
    x = random.randint(-127, 127) # Indent the code from this line
    y = random.randint(0, 64)
    z = random.randint(-127, 127)
    mc.player.setTilePos(x, y, z)

    # Add 1 to the value of the count variable here
    u +=1
    print (u)

    # Timer for number of seconds between each teleportation
    time.sleep(5)
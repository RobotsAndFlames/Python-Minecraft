from mcpi.minecraft import Minecraft
mc = Minecraft.create("192.168.1.15")

pos = mc.player.getPos()
mc.setBlock(pos.x, pos.y, pos.z, 8)
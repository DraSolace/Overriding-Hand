from libs import mouse
from libs import keyboard
import time

if __name__ == '__main__':
	def macro():
		def usedname():

					keyboard.send("windows+r")

					time.sleep(0.2)

					keyboard.write("cmd")

					keyboard.send("enter")

					time.sleep(0.2)

					keyboard.write("color a")

					keyboard.send("enter")

					time.sleep(0.2)

					keyboard.write("cd /")

					keyboard.send("enter")

					time.sleep(0.2)

					keyboard.send("alt+enter")

					time.sleep(0.2)

					keyboard.write("tree")

					keyboard.send("enter")
		keyboard.add_hotkey("t", lambda: usedname())

		keyboard.wait("escape")
		exit()
	macro()
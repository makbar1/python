import time
from pynput.mouse import Button, Controller

mouse = Controller()


print ("Current position: " + str(mouse.position))

mouse.position = (10, 20)
mouse.move(20, -13)


def click_mouse():

	# Click the left button
	mouse.click(Button.left, 1)
	# Click the right button
	mouse.click(Button.right, 1)
	# Click the middle button
	mouse.click(Button.middle, 1)
	# Double click the left button
	mouse.click(Button.left, 2)
	# Click the left button ten times
	mouse.click(Button.left, 10)

j = 100

while True:
	mouse.move(20, 20)
	for i in range(10, 1000, 10):
		time.sleep(10)
		#click_mouse()
		mouse.click(Button.left, 1)
		mouse.move(i, j + i)
		print ("Current position: " + str(mouse.position))

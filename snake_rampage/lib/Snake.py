import sys, pygame

class Snake(object):

	size_x = 12
	size_y = 12 
	eyes = (255, 193, 37)
	eyes_size = 5
	nose_size = 7
	move_x = 300
	move_y = 300
	body = []

	def __init__(self, window, color, x, y):
		#draw head
		pygame.draw.rect(window, color, [x, y, self.size_x, self.size_y])
		#draw eyes
		pygame.draw.rect(window, self.eyes, [x+2, y-3, self.eyes_size, self.eyes_size])
		pygame.draw.rect(window, self.eyes, [x+2, y+10, self.eyes_size, self.eyes_size])
		#draw nose
		pygame.draw.rect(window, color, [x+10, y+3, self.nose_size, self.nose_size])
		#draw first body element
		pygame.draw.rect(window, color, [x-10, y, self.size_x, self.size_y])


	def grow(self, window, color, x, y):
		#add rect to end
		pygame.draw.rect(window, color, [x-50, y-10, 100, self.size_y])


	def eat(self, window, actual_x, actual_y, prey_x, prey_y):
		print("Eat! cords: ", actual_x, actual_y, prey_x, prey_y)
		#detect collision
		collision = False
		actual_y += 15
		actual_x += 15
		actual_x_p = actual_x - 30
		actual_y_p = actual_y - 30
		if (actual_x_p <= prey_x <= actual_x) and (actual_y_p <= prey_y <= actual_y):
			collision = True
		return collision
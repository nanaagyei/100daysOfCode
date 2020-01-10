import pygame
import random
import sys

pygame.init() #initializes the pygame

WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size] #position of player in the (x,y) coordinate on the screen.(0,0) starts at the top left corner

BACKGROUND_COLOR = (207,11,238)

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0] #enemies fall at random positions from the top of the screen
enemy_list = [enemy_pos] #gives the list of enemies

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #displays the pygame screen 

SPEED = 10

score = 0

game_over = False 

clock = pygame.time.Clock() #enable the pygame clock to check the speed of the game

myFont = pygame.font.SysFont("monospace", 35) #enables the font function in pygame. 

def set_level(score, SPEED): #set the level of the game(increases the speed for each level)
	if score < 10:
		SPEED = 10
	elif score < 20:
		SPEED += 18
	elif score < 40:
		SPEED = 20
	return SPEED

def drop_enemies(enemy_list): #drops the enemies
	delay = random.random() #same as randint(0,1)
	if len(enemy_list) < 10 and delay < 0.1: #delays other enemies so that they don't come at the same time
		x_pos = random.randint(0, WIDTH-enemy_size) #randomizes the position of the enemies at the top of the screen
		y_pos = 0
		enemy_list.append([x_pos, y_pos]) #adds each enemy to the list

def draw_enemies(enemy_list): #draws the enemy boxes
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemies_position(enemy_list, score): #updates position of enemies and the score
	for idx, enemy_pos in enumerate(enemy_list): #numbers the enemies in the list
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT: #drops the enemies
			enemy_pos[1] += SPEED
		else:
			enemy_list.pop(idx) #removes enemy from the list as it gets the bottom
			score += 1 #for every enemy that is removed the score increases by 1
	return score #returns the score

def collision_check(enemy_list, enemy_pos): #checks if there is collision between enemy and player
	for enemy_pos in enemy_list:
		if detect_collision(player_pos, enemy_pos):
			return True
		else:
			return False #continues the game if no collision detected

def detect_collision(enemy_pos, player_pos): #finds the collision between enemy and player
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)): #if there's any overlapping between enemy and player in the x or y axis
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
			return True
	return False

while not game_over: #infinite loop of game until collision detected

	for event in pygame.event.get(): #any event that happens on the pygame screen

		if event.type == pygame.QUIT: 
			sys.exit() #quits the game. import sys library first

		if event.type == pygame.KEYDOWN: #for any key press on the keyboard
			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT: #if left arrow is pressed
		 		x -= player_size

			elif event.key == pygame.K_RIGHT: #if right arrow is pressed
		 		x += player_size

			player_pos = [x,y] #updates player position after key pressed
	screen.fill(BACKGROUND_COLOR) #background color

	#Update the position enemy
	# if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
	# 	enemy_pos[1] += SPEED
	# else:
	# 	enemy_pos[0] = random.randint(0, WIDTH-enemy_size)
	# 	enemy_pos[1] = 0

	# if detect_collision(player_pos, enemy_pos):
	# 	game_over = True
	# 	break

	drop_enemies(enemy_list)
	score = update_enemies_position(enemy_list, score)
	SPEED = set_level(score, SPEED)

	text = "Score:" + str(score)
	label = myFont.render(text, 1, YELLOW)
	screen.blit(label, (WIDTH-200, HEIGHT-40))  #position of the score text

	if collision_check(enemy_list, enemy_pos): #closes the game if there is a collision
		game_over = True
		break

	draw_enemies(enemy_list) 
	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(10) #speed of the game

	pygame.display.update() #updates any change made in the pygame
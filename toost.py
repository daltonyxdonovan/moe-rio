import pygame
from pygame.constants import *
import level
from settings import *
pygame.init()
pygame.mixer.init()
pygame.joystick.init()
pygame.mixer.Sound.set_volume(jumpSound, volume)
pygame.mixer.Sound.set_volume(select, volume)

while running:
	



	if levelEditor:
		playerscreen.blit(background2, (0,0))
		if juststarted == True:
			mapx = 0
			juststarted = False
		
		for row in range(len(level.start)):
			for column in range(len(level.edits[row])):
				playerscreen.blit(level.textures[level.edits[row][column]],
								 (column*level.tilesize-mapx, row*level.tilesize))
		cursorgroup.draw(playerscreen)
		helpgroup.draw(playerscreen)
		helpgroup.update()
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			if event.type == KEYDOWN:
				level.editsbuffer = level.edits
				if event.key == K_ESCAPE:
					title = True
					levelEditor = False
				if event.key == K_e:
					mapx = 0
					level.edits = level.editsbackup
				if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_LCTRL:
					level.edits = level.editsbuffer
					
				if event.key == K_SPACE:
					mapx = 0
					level.level = level.edits
					levelEditor = False
					game = True
				if event.key == K_F11:
					pygame.display.toggle_fullscreen()
				if event.key == K_w:
					if cursor.rect.y >=49:
						cursor.rect.y -= 50
				if event.key == K_s:
					if cursor.rect.y <= SCREEN_HEIGHT-51:
						cursor.rect.y += 50
				if event.key == K_a:
					if cursor.rect.x >=51:
						cursor.rect.x -= 50
					else:
						mapx -= 50
				if event.key == K_d:
					if cursor.rect.x <= SCREEN_WIDTH-51:
						cursor.rect.x += 50
					else:
						mapx +=50
				position = [cursor.rect.x, cursor.rect.y]
				cursorrow = (position[1]//CELL)
				cursorcolumn = (position[0]+mapx)//CELL
				if event.key == K_KP_0:
					if cursorrow >= 0 and cursorrow < int(level.mapheight/CELL) and cursorcolumn >= 0 and cursorcolumn < int(level.mapwidth/CELL):
						level.edits[cursorrow][cursorcolumn] = 0
				if event.key == K_KP_1:
					if cursorrow >= 0 and cursorrow < int(level.mapheight/CELL) and cursorcolumn >= 0 and cursorcolumn < int(level.mapwidth/CELL):
						level.edits[cursorrow][cursorcolumn] = 1
				if event.key == K_KP_2:
					if cursorrow >= 0 and cursorrow < int(level.mapheight/CELL) and cursorcolumn >= 0 and cursorcolumn < int(level.mapwidth/CELL):
						level.edits[cursorrow][cursorcolumn] = 2
				if event.key == K_KP_3:
					if cursorrow >= 0 and cursorrow < int(level.mapheight/CELL) and cursorcolumn >= 0 and cursorcolumn < int(level.mapwidth/CELL):
						level.edits[cursorrow][cursorcolumn] = 3
				if event.key == K_KP_4:
					if cursorrow >= 0 and cursorrow < int(level.mapheight/CELL) and cursorcolumn >= 0 and cursorcolumn < int(level.mapwidth/CELL):
						level.edits[cursorrow][cursorcolumn] = 4
				if event.key == K_KP_5:
					if cursorrow >= 0 and cursorrow < int(level.mapheight/CELL) and cursorcolumn >= 0 and cursorcolumn < int(level.mapwidth/CELL):
						level.edits[cursorrow][cursorcolumn] = 5
				if event.key == K_KP_6:
					if cursorrow >= 0 and cursorrow < int(level.mapheight/CELL) and cursorcolumn >= 0 and cursorcolumn < int(level.mapwidth/CELL):
						level.edits[cursorrow][cursorcolumn] = 6
				else:
					pass
		pygame.display.update()
	if win:
		playerscreen.blit(background, (0, 0))
		playerscreen.blit(winimage, (360, 100))
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					level.level = level.backup
					select.play()
					running = False
				if event.key == K_RETURN:
					level.level = level.backup
					select.play()
					levelswon = levelswon + 1
					title = True
					win = False
				if event.key == K_F11:
					pygame.display.toggle_fullscreen()
					select.play()
				
		pygame.display.update()
	if over:
		mapx = 0
		playerscreen.fill(BLACK)
		playerscreen.blit(gameover, (300, 200))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.JOYBUTTONDOWN:
				if event.button == 0:
					select.play()
					title = True
					over = False
				
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					level.level = level.backup
					title = True
					over = False
					select.play()
				if event.key == K_ESCAPE:
					level.level = level.backup
					title = True
					over = False
					select.play()
				
				if event.key == K_F11:
					pygame.display.toggle_fullscreen()
					select.play()
		pygame.display.update()
	if title:
		playerscreen.blit(background, (0, 0))
		jump = False
		onground = False
		juststarted = True
		v = 4
		m = 2
		player.rect.x = SCREEN_WIDTH/2
		player.rect.y = SCREEN_HEIGHT/2
		for row in range(len(level.start)):
			for column in range(len(level.start[row])):
				playerscreen.blit(level.textures[level.start[row][column]],
								 (column*level.tilesize-mapx, row*level.tilesize))
		titlegroup.draw(playerscreen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			
			
			if event.type == pygame.JOYBUTTONDOWN:
				if event.button == 0:
					if choice == 0:
						select.play()
						title = False
						game = True
					if choice == 1:
						select.play()
						levelEditor = True
						title = False
						
				if event.button == 11:
					select.play()
					choice = choice - 1
				if event.button == 12:
					select.play()
					choice = choice + 1

				print("Joystick button pressed.")
			if event.type == pygame.JOYBUTTONUP:
				print("Joystick button released.")

			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_h:
					if helping == False:
						helping = True
						print("h")
					elif helping == True:	
						helping = False
				if event.key == K_w:
					choice = choice + 1
					select.play()
				if event.key == K_s:
					choice = choice - 1
					select.play()
				if event.key == K_F11:
					pygame.display.toggle_fullscreen()
					select.play()
				if event.key == K_ESCAPE:
					running = False
					select.play()
				if event.key == K_RETURN:
					if choice == 0:
						if levelswon == 0:
							level.level = level.level
						if levelswon == 1:
							level.level = level.level2
						if levelswon == 2:
							level.level = level.level3
						game = True
						title = False
						select.play()
					if choice == 1:

						levelEditor = True
						title = False
		playerscreen.blit(levelimg, (75, 350))
		playerscreen.blit(editor, (75, 450))
		dgroup.draw(playerscreen)
		if choice == 0:
			playerscreen.blit(selector, (25, 375))
		if choice == 1:
			playerscreen.blit(selector, (25, 475))
		if choice > 1:
			choice = 0
		if choice < 0:
			choice = 1
		pygame.display.update()
		mapx += 3
		if mapx > level.mapwidth-1100:
			mapx = 1400
		
		titlegroup.update()
		
		dgroup.update()
	if game:
		playerscreen.blit(background, (0, 0))
		if juststarted:
			mapx = 0
			juststarted = False
		if player.rect.y > SCREEN_HEIGHT-CELL-11:
			over = True
			game = False
		playerbuffer[0] = player.rect.x
		playerbuffer[1] = player.rect.y
		playerbuffer[2] = mapx
		if mapx == level.mapwidth-SCREEN_WIDTH:
			mapx = level.mapwidth-SCREEN_WIDTH
		if mapx < 0:
			mapx = 0
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			if event.type == JOYBUTTONDOWN:
				if event.button == 0:
					if onground:
						playerbuffer.pop(0)
						playerbuffer.pop(0)
						playerbuffer.pop(0)
						playerbuffer.append(player.rect.x)
						playerbuffer.append(player.rect.y)
						playerbuffer.append(mapx)
						jump = True
						onground = False
						jumpSound.play()
				if event.button == 13:
					if cellNumber(playerrow3,playercolumn3) == 2:
						player.moveLeft()
						if mapx > 0 and player.rect.x <=(SCREEN_WIDTH/2):
							mapx -= playerspeed
						else:
							player.rect.x -= playerspeed
						playerbuffer.pop(0)
						playerbuffer.pop(0)
						playerbuffer.pop(0)
						playerbuffer.append(player.rect.x)
						playerbuffer.append(player.rect.y)
						playerbuffer.append(mapx)
				if event.button == 14:
					if cellNumber(playerrow2,playercolumn2) == 2:
						player.moveRight()
						if mapx < level.mapwidth-SCREEN_WIDTH and player.rect.x >=(SCREEN_WIDTH/2):
							mapx += playerspeed
						else:
							player.rect.x += playerspeed
						playerbuffer.pop(0)
						playerbuffer.pop(0)
						playerbuffer.pop(0)
						playerbuffer.append(player.rect.x)
						playerbuffer.append(player.rect.y)
						playerbuffer.append(mapx)


			if cellNumber(playerrow3,playercolumn3) == 0 and left == True:
				player.moveLeft()
				if mapx > 0 and player.rect.x <=(SCREEN_WIDTH/2):
					mapx -= playerspeed
				else:
					player.rect.x -= playerspeed
				playerbuffer.pop(0)
				playerbuffer.pop(0)
				playerbuffer.pop(0)
				playerbuffer.append(player.rect.x)
				playerbuffer.append(player.rect.y)
				playerbuffer.append(mapx)
			if cellNumber(playerrow2,playercolumn2) == 0 and right == True:
				player.moveRight()
				if mapx < level.mapwidth-SCREEN_WIDTH and player.rect.x >=(SCREEN_WIDTH/2):
					mapx += playerspeed
				else:
					player.rect.x += playerspeed
				playerbuffer.pop(0)
				playerbuffer.pop(0)
				playerbuffer.pop(0)
				playerbuffer.append(player.rect.x)
				playerbuffer.append(player.rect.y)
				playerbuffer.append(mapx)
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					level.level = level.backup
					title = True
					game = False
					select.play()
				if event.key == K_F11:
					pygame.display.toggle_fullscreen()
					select.play()
				if event.key == K_SPACE:
					if onground:
						playerbuffer.pop(0)
						playerbuffer.pop(0)
						playerbuffer.pop(0)
						playerbuffer.append(player.rect.x)
						playerbuffer.append(player.rect.y)
						playerbuffer.append(mapx)
						jump = True
						onground = False
						jumpSound.play()	
			if event.type == KEYUP:
				if event.key == K_d:
					player.standingRight()
				if event.key == K_a:
					player.standingLeft()
		keys = pygame.key.get_pressed()
		if keys[K_LSHIFT]:
			playerspeed = 6
		else:
			playerspeed = 4
		if keys[K_d]:
			if cellNumber(playerrow2,playercolumn2) == 0 or cellNumber(playerrow2,playercolumn2) == 7:
				player.moveRight()
				if mapx < level.mapwidth-SCREEN_WIDTH and player.rect.x >=(SCREEN_WIDTH/2):
					mapx += playerspeed
				else:
					player.rect.x += playerspeed
				playerbuffer.pop(0)
				playerbuffer.pop(0)
				playerbuffer.pop(0)
				playerbuffer.append(player.rect.x)
				playerbuffer.append(player.rect.y)
				playerbuffer.append(mapx)
			
		if keys[K_a]:
			if cellNumber(playerrow3,playercolumn3) == 0 or cellNumber(playerrow3,playercolumn3) == 7:
				player.moveLeft()
				if mapx > 0 and player.rect.x <=(SCREEN_WIDTH/2):
					mapx -= playerspeed
				else:
					player.rect.x -= playerspeed
				playerbuffer.pop(0)
				playerbuffer.pop(0)
				playerbuffer.pop(0)
				playerbuffer.append(player.rect.x)
				playerbuffer.append(player.rect.y)
				playerbuffer.append(mapx)
			
		if onground == False and jump == True:
			F = (1/2)*m*(v**2)
			player.rect.y -= F
			v = v - .22
			if v < 0:
				m = -1
		if onground == False and jump == False:
			F = (1/2)*m*(v**2)
			player.rect.y -= F
			m = -1
			v = -3
		position = ((player.rect.x+30)+mapx, player.rect.y+60)
		position2 = ((player.rect.x+1)+mapx, player.rect.y+50)
		position3 = ((player.rect.x+59)+mapx, player.rect.y+50)
		position4 = ((player.rect.x+30)+mapx, player.rect.y+60)

		playercolumn = (position[0] // CELL)
		playercolumn2 = (position2[0] // CELL)+1
		playercolumn3 = (position3[0] // CELL)-1
		playercolumn4 = (position4[0] // CELL)


		playerrow = (position[1] // CELL)
		playerrow2 = (position2[1] // CELL)
		playerrow3 = (position3[1] // CELL)
		playerrow4 = (position4[1] // CELL)-1
		if cellNumber(playerrow4, playercolumn4) == 1 or cellNumber(playerrow4, playercolumn4) == 2:
			player.rect.x = playerbuffer[0]
			player.rect.y = playerbuffer[1]
			mapx = playerbuffer[2]
		if cellNumber(playerrow,playercolumn) == 4:
			win = True
			game = False
		if cellNumber(playerrow,playercolumn) == 0 or cellNumber(playerrow,playercolumn) == 7:
			onground = False
		else:
			
			player.rect.x = playerbuffer[0]
			mapx = playerbuffer[2]
			onground = True
			v = 4
			m = 2
			jump = False
		if cellNumber(playerrow,playercolumn) == 6:
			over = True
			game = False
		for row in range(len(level.level)):
			for column in range(len(level.level[row])):
				playerscreen.blit(level.textures[level.level[row][column]],
							(column*level.tilesize-mapx, row*level.tilesize))
		playergroup.draw(playerscreen)
		
		playergroup.update()
		if cellNumber(playerrow2,playercolumn2) == 1 or cellNumber(playerrow3,playercolumn3) == 2:
			jump = True
			onground = True
			v = 4
			m = 2
		if cellNumber(playerrow3,playercolumn3) == 1 or cellNumber(playerrow3,playercolumn3) == 2:
			jump = True
			onground = True
			v = 4
			m = 2
#                                                                                                      it's these two checks above that make the player jump wonky ^^^^^^^^^^^^^^
		pygame.display.update()
	
	clock.tick(60)
	
			
		

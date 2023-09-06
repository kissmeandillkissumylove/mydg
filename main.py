import pygame #import pygame
pygame.init() #pygame init


#WINDOW SETTINGS
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #screen size


#CHARACTER SETTINGS
player_img = pygame.image.load('dgfiles/player.png') #image for character
player_rect = player_img.get_rect() #get player rect
player_rect.x = 20
player_rect.y = 20
player_speed = 2



#SCREEN BARIERS
top_wall = pygame.Rect(0, 0, SCREEN_WIDTH, 5)
bottom_wall = pygame.Rect(0, SCREEN_HEIGHT-5, SCREEN_WIDTH, 5)
left_wall = pygame.Rect(0, 0, 5, SCREEN_HEIGHT)
right_wall = pygame.Rect(SCREEN_WIDTH-5, 0, 5, SCREEN_HEIGHT)


#MAIN LOOP
running = True #flag for game is running
while running: #main loop


   #KEYBOARD
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
   if pygame.key.get_pressed()[pygame.K_UP]: #move character up
      player_rect.y -= player_speed
      if player_rect.colliderect(top_wall):
         player_rect.y += player_speed  #undo move
   if pygame.key.get_pressed()[pygame.K_DOWN]: #move character down
      player_rect.y += player_speed
      if player_rect.colliderect(bottom_wall):
         player_rect.y -= player_speed  #undo move
   if pygame.key.get_pressed()[pygame.K_LEFT]: #move character left
      player_rect.x -= player_speed
      if player_rect.colliderect(left_wall):
         player_rect.x += player_speed  #undo move
   if pygame.key.get_pressed()[pygame.K_RIGHT]: #move character right
      player_rect.x += player_speed
      if player_rect.colliderect(right_wall):
         player_rect.x -= player_speed  #undo move


   #SCREEN UPDATE
   screen.fill((200, 200, 200)) #fill screen for updating
   screen.blit(player_img, (player_rect.x, player_rect.y)) #draw char
   pygame.draw.rect(screen, (0, 0, 0), top_wall) #draw walls
   pygame.draw.rect(screen, (0, 0, 0), bottom_wall)
   pygame.draw.rect(screen, (0, 0, 0), left_wall)
   pygame.draw.rect(screen, (0, 0, 0), right_wall)
   #LAST UPDATE
   pygame.display.update() #display update
   pygame.time.Clock().tick(60) #60fps
import pygame

pygame.init()

            #---------Clock---------
clock= pygame.time.Clock()
enemy_respawn_timer = pygame.time.get_ticks()
enemy2_respawn_timer = pygame.time.get_ticks()
            #----------display---------
screen = pygame.display.set_mode((1500,770))
title = pygame.display.set_caption("My game")

animation_index_reaper = 0
animation_state_reaper = 'idle'
            #--------BG----------
BG = pygame.image.load('BG.jpg')
            #-----------font--------------------
font1 = pygame.font.Font('DigitalDisco.ttf',72)
            #----------------------------------------
life = 15
score = 0
            #----------------text----------------
life_text = font1.render('Life = {}'.format(life),True,(255,255,255))
score_text = font1.render('Score = {}'.format(score),True,(255,255,255))
Game_Over = font1.render('Game Over',True,(255,0,0))
            #----------------------------------------reaper-----------------------------------------------------------------------------
reaper_pos_x=500
reaper_pos_y=500

reaper_idle = [pygame.image.load(f'Reaper/Idle Blinking/Reaper{i}.png')for i in range (1,18)]
reaper_idle_right = [pygame.transform.scale(sprite,(300,300))for sprite in reaper_idle]

reaper_idle = [pygame.image.load(f'Reaper/Idle Blinking/Reaper{i}.png')for i in range (1,18)]
reaper_idle = [pygame.transform.scale(sprite,(300,300))for sprite in reaper_idle]
reaper_idle_left = [pygame.transform.flip(sprite,True,False)for sprite in reaper_idle]


reaper_run_right = [pygame.image.load(f'Reaper/Running/0_Reaper_Man_Running_{i}.png')for i in range (1,13)]
reaper_run_right = [pygame.transform.scale(sprite,(300,300))for sprite in reaper_run_right]

reaper_run_left = [pygame.image.load(f'Reaper/Running/0_Reaper_Man_Running_{i}.png')for i in range (1,13)]
reaper_run_left= [pygame.transform.scale(sprite,(300,300))for sprite in reaper_run_left]
reaper_run_left = [pygame.transform.flip(sprite,True,False)for sprite in reaper_run_left]

reaper_attack= [pygame.image.load(f'Reaper/Run Slashing/0_Reaper_Man_Run Slashing_{i}.png')for i in range (1,13)]
reaper_attack_right= [pygame.transform.scale(sprite,(300,300))for sprite in reaper_attack]

reaper_attack_left = [pygame.image.load(f'Reaper/Run Slashing/0_Reaper_Man_Run Slashing_{i}.png')for i in range (1,13)]
reaper_attack_left = [pygame.transform.scale(sprite,(300,300))for sprite in reaper_attack_left]
reaper_attack_left = [pygame.transform.flip(sprite,True,False)for sprite in reaper_attack_left]

reaper_dead= [pygame.image.load(f'Reaper/Dying/{i}.png')for i in range (1,16)]
reaper_dead_right= [pygame.transform.scale(sprite,(300,300))for sprite in reaper_dead]

reaper_dead= [pygame.image.load(f'Reaper/Dying/{i}.png')for i in range (1,16)]
reaper_dead_right= [pygame.transform.scale(sprite,(300,300))for sprite in reaper_dead]
reaper_dead_left = [pygame.transform.flip(sprite,True,False)for sprite in reaper_dead_right]

reaper_jump = [pygame.image.load(f'Reaper/Jump Start/{i}.png')for i in range (1,7)]
reaper_jump = [pygame.transform.scale(sprite,(300,300))for sprite in reaper_jump]
            #------------------------------------------Golem--------------------------------------
life_golem = 3
life_golem2 = 3

golem_pos_x =1400
golem_pos_y =500

golem2_pos_x=-300
golem2_pos_y =500

animation_index_golem = 0
animation_index_golem2 = 0

golem_idle = [pygame.image.load(f'Golem/Idle Blinking/{i}.png')for i in range (1,19)]
golem_idle_left = [pygame.transform.scale(sprite,(300,300))for sprite in golem_idle]

golem_idle = [pygame.image.load(f'Golem/Idle Blinking/{i}.png')for i in range (1,19)]
golem_idle_right = [pygame.transform.scale(sprite,(300,300))for sprite in golem_idle]
golem_idle_right = [pygame.transform.flip(sprite,True,False)for sprite in golem_idle_right]

golem_walk_right =[pygame.image.load(f'Golem/Walking/{i}.png')for i in range (1,25)]
golem_walk_right = [pygame.transform.scale(sprite,(300,300))for sprite in golem_walk_right]

golem_walk_left =[pygame.image.load(f'Golem/Walking/{i}.png')for i in range (1,25)]
golem_walk_left = [pygame.transform.scale(sprite,(300,300))for sprite in golem_walk_left]
golem_walk_left = [pygame.transform.flip(sprite,True,False)for sprite in golem_walk_left]

golem_attack = [pygame.image.load(f'Golem/Slashing/{i}.png')for i in range (1,13)]
golem_attack_right = [pygame.transform.scale(sprite,(300,300))for sprite in golem_attack]

golem_attack = [pygame.image.load(f'Golem/Slashing/{i}.png')for i in range (1,13)]
golem_attack = [pygame.transform.scale(sprite,(300,300))for sprite in golem_attack]
golem_attack_left = [pygame.transform.flip(sprite,True,False)for sprite in golem_attack]

golem_dead_right = [pygame.image.load(f'Golem/Dying/{i}.png')for i in range (1,16)]
golem_dead_right = [pygame.transform.scale(a,(300,300))for a in golem_dead_right]

golem_dead_left = [pygame.image.load(f'Golem/Dying/{i}.png')for i in range (1,16)]
golem_dead_left = [pygame.transform.scale(a,(300,300))for a in golem_dead_left]
golem_dead_left = [pygame.transform.flip(a,True,False)for a in golem_dead_left]

running = True
walk_right=False
walk_left=False
animation_state_golem = 'spawn'
animation_state_golem2 = 'spawn'
idle_reaper='right'
i=1
a=1
p=1
turn_enemy2 = 'a'
turn_enemy = 'a'
while running:
    screen.blit(BG,(0,0))
    screen.blit(life_text,(50,10))
    screen.blit(score_text,(1000,10))
    #---------------Game Over-----------------------
    if animation_state_reaper == 'dead':
        screen.blit(Game_Over,(510,290))
    #-------------------------------------Hit Box------------------------------------------
    player_hitbox = pygame.Rect(reaper_pos_x,reaper_pos_y,200,100)
    enemy_hitbox = pygame.Rect(golem_pos_x+25,golem_pos_y,175,100)
    enemy2_hitbox = pygame.Rect(golem2_pos_x+25,golem2_pos_y,175,100)
    #---------------------------animation enemy1111111---------------------------------------
    
    if animation_state_golem == 'spawn':
        
        if turn_enemy == 'right':
            if animation_index_golem >= 18:
                animation_index_golem = 0
            screen.blit(golem_idle_left[animation_index_golem],(golem_pos_x,golem_pos_y))
            animation_index_golem +=1
        
        if turn_enemy == 'left':
            if animation_index_golem >= 18:
                animation_index_golem = 0
            screen.blit(golem_idle_right[animation_index_golem],(golem_pos_x,golem_pos_y))
            animation_index_golem +=1
    
    if animation_state_golem == 'attack':
        if animation_index_golem >=12:
            if enemy_hitbox.colliderect(player_hitbox):
                animation_state_golem = 'attack'
            else:
                animation_state_golem = 'spawn' 
            animation_index_golem = 0
        
        if golem_pos_x > reaper_pos_x:
            screen.blit(golem_attack_left[animation_index_golem],(golem_pos_x,golem_pos_y))
            turn_enemy = 'left'
            if animation_index_golem ==5:
                life -=1
                if life == 0:
                    r='right'
                life_text = font1.render('Life = {}'.format(life),True,(255,255,255))
            animation_index_golem +=1
        else:
            screen.blit(golem_attack_right[animation_index_golem],(golem_pos_x,golem_pos_y))
            turn_enemy = 'right'
            if animation_index_golem ==5:
                life -=1
                if life == 0:
                    r='left'
                life_text = font1.render('Life = {}'.format(life),True,(255,255,255))
            animation_index_golem +=1
            
            
    if animation_state_golem == 'right':
        if animation_index_golem >= 24:
            animation_index_golem = 0
        screen.blit(golem_walk_right[animation_index_golem],(golem_pos_x,golem_pos_y))
        animation_index_golem +=1
        
    if animation_state_golem == 'left':
        if animation_index_golem >= 24:
            animation_index_golem = 0
        screen.blit(golem_walk_left[animation_index_golem],(golem_pos_x,golem_pos_y))
        animation_index_golem +=1
    if animation_state_golem == 'dead':
        if dead_golem == 'right':
            if animation_index_golem <15:
                screen.blit(golem_dead_right[animation_index_golem],(golem_pos_x,golem_pos_y))
                animation_index_golem +=1
        if dead_golem == 'left':
            if animation_index_golem <15:
                screen.blit(golem_dead_left[animation_index_golem],(golem_pos_x,golem_pos_y))
                animation_index_golem +=1
    
    
    if animation_state_golem != 'attack':
        if animation_state_reaper != 'dead':
            if reaper_pos_x < golem_pos_x:
                golem_pos_x -=5
                turn_enemy = 'left'
                animation_state_golem = 'left'
            if reaper_pos_x > golem_pos_x:
                golem_pos_x +=5
                turn_enemy = 'right'
                animation_state_golem = 'right'
    
    #---------------------------animation enemy22222---------------------------------------
    
    if animation_state_golem2 == 'spawn':
        if turn_enemy2 == 'right':
            if animation_index_golem2 >= 18:
                animation_index_golem2 = 0
            screen.blit(golem_idle_left[animation_index_golem2],(golem2_pos_x,golem2_pos_y))
            animation_index_golem2 +=1
        if turn_enemy2 == 'left':
            if animation_index_golem2 >= 18:
                animation_index_golem2 = 0
            screen.blit(golem_idle_right[animation_index_golem2],(golem2_pos_x,golem2_pos_y))
            animation_index_golem2 +=1
    

    
    if animation_state_golem2 == 'attack':
        if animation_index_golem2 >=12:
            if enemy2_hitbox.colliderect(player_hitbox):
                animation_state_golem2 = 'attack'
            else:
                animation_state_golem2 = 'spawn' 
            animation_index_golem2 = 0
        
        if golem2_pos_x > reaper_pos_x:
            screen.blit(golem_attack_left[animation_index_golem2],(golem2_pos_x,golem2_pos_y))
            turn_enemy2 = 'left'
            if animation_index_golem2 ==5:
                life -=1
                if life == 0:
                    r='right'
                life_text = font1.render('Life = {}'.format(life),True,(255,255,255))
            animation_index_golem2 +=1
        else:
            screen.blit(golem_attack_right[animation_index_golem2],(golem2_pos_x,golem2_pos_y))
            turn_enemy2 = 'right'
            if animation_index_golem2 ==5:
                life -=1
                if life == 0:
                    r='left'
                life_text = font1.render('Life = {}'.format(life),True,(255,255,255))
            animation_index_golem2 +=1
            
    if animation_state_golem2 == 'right':
        if animation_index_golem2 >= 24:
            animation_index_golem2 = 0
        screen.blit(golem_walk_right[animation_index_golem2],(golem2_pos_x,golem2_pos_y))
        animation_index_golem2 +=1
        
    if animation_state_golem2 == 'left':
        if animation_index_golem2 >= 24:
            animation_index_golem2 = 0
        screen.blit(golem_walk_left[animation_index_golem2],(golem2_pos_x,golem2_pos_y))
        animation_index_golem2 +=1
    if animation_state_golem2 == 'dead':
        if dead_golem2 == 'right':
            if animation_index_golem2 <15:
                screen.blit(golem_dead_right[animation_index_golem2],(golem2_pos_x,golem2_pos_y))
                animation_index_golem2 +=1
        if dead_golem2 == 'left':
            if animation_index_golem2 <15:
                screen.blit(golem_dead_left[animation_index_golem2],(golem2_pos_x,golem2_pos_y))
                animation_index_golem2 +=1
    
    
    if animation_state_golem2 != 'attack':
        if animation_state_reaper != 'dead':
            if reaper_pos_x < golem2_pos_x:
                golem2_pos_x -=5
                turn_enemy2 = 'left'
                animation_state_golem2 = 'left'
            if reaper_pos_x > golem2_pos_x:
                golem2_pos_x +=5
                turn_enemy2 = 'right'
                animation_state_golem2 = 'right'
    #-------------------animation player--------------------------------------------------------
    if animation_state_reaper == 'idle':
        if animation_index_reaper>=17:
            animation_index_reaper=0
        if idle_reaper == 'right':
            screen.blit(reaper_idle_right[animation_index_reaper],(reaper_pos_x,reaper_pos_y))
            animation_index_reaper +=1
        if idle_reaper == 'left':
            screen.blit(reaper_idle_left[animation_index_reaper],(reaper_pos_x,reaper_pos_y))
            animation_index_reaper +=1
            
    if animation_state_reaper == 'right':
        if animation_index_reaper >=12:
            animation_index_reaper = 0
        screen.blit(reaper_run_right[animation_index_reaper],(reaper_pos_x,reaper_pos_y))
        animation_index_reaper +=1
        
    if animation_state_reaper == 'left':
        if animation_index_reaper >= 12:
            animation_index_reaper =0
        screen.blit(reaper_run_left[animation_index_reaper],(reaper_pos_x,reaper_pos_y))
        animation_index_reaper +=1
        
    if animation_state_reaper == 'jump':
        if animation_index_reaper >= 6:
            animation_index_reaper = 0
        screen.blit(reaper_jump[animation_index_reaper],(reaper_pos_x,reaper_pos_y))
        animation_index_reaper +=1
        
    if animation_state_reaper == 'attack':
        if animation_index_reaper >=12:
            animation_index_reaper = 0
        
        if idle_reaper=='left':
            screen.blit(reaper_attack_left[animation_index_reaper],(reaper_pos_x,reaper_pos_y))
            animation_index_reaper += 1
        
        else:
            screen.blit(reaper_attack_right[animation_index_reaper],(reaper_pos_x,reaper_pos_y))
            animation_index_reaper += 1
        #------------Gravity----------------------
    if reaper_pos_y <500:
        reaper_pos_y +=20
            #------------event Game--------------
    for event in pygame.event.get():
          
            
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print('Walk right')
                animation_state_reaper = 'right'
                walk_right = True
                animation_state_reaper = 'right'
            if event.key == pygame.K_a:
                print('Walk Left')
                animation_state_reaper = 'left'
                walk_left = True
                animation_state_reaper = 'left'
            if event.key == pygame.K_SPACE:
                animation_state_reaper = 'attack'
                if player_hitbox.colliderect(enemy_hitbox):
                    print('hit')
                    life_golem -=1
                if player_hitbox.colliderect(enemy2_hitbox):
                    print('hit')
                    life_golem2 -=1
                        
                
            if event.key == pygame.K_w:
                if reaper_pos_y < 500:
                    pass
                else:
                    reaper_pos_y -=200
                    animation_state_reaper = 'jump'
                
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                walk_right = False
                animation_state_reaper = 'idle'
            if event.key == pygame.K_a:
                walk_left = False
                animation_state_reaper = 'idle'
            if event.key == pygame.K_w:
                animation_state_reaper = 'idle'
            if event.key == pygame.K_SPACE:
                animation_state_reaper = 'idle'
        
        
    
    #---------------------------------------score------------------------------------
    if life_golem == 0:
        if i==1:
            score +=1
        score_text = font1.render('Score = {}'.format(score),True,(255,255,255))
    if life_golem2 == 0 :
        if a==1:
            score +=1
        score_text = font1.render('Score = {}'.format(score),True,(255,255,255))
    #------------------------- enemy attack --------------------
    if enemy_hitbox.colliderect(player_hitbox):
        animation_state_golem = 'attack'
    if enemy2_hitbox.colliderect(player_hitbox):
        animation_state_golem2 = 'attack'
        
    if life < 1 :
        animation_state_reaper = 'dead'
    #------------------------ enemy dead-------------------------
    if life_golem < 1:
        animation_state_golem = 'dead'
        if golem_pos_x > reaper_pos_x:
            dead_golem = 'left'
        if golem_pos_x <reaper_pos_x:
            dead_golem = 'right'
    
    if life_golem2 < 1:
        animation_state_golem2 = 'dead'
        if golem2_pos_x > reaper_pos_x:
            dead_golem2 = 'left'
        if golem2_pos_x <reaper_pos_x:
            dead_golem2 = 'right'
    
     
     #---------------------------------- enemy respawn------------------   (every 5s)   
    if animation_state_golem == 'dead':
        if animation_index_golem >=15:
            golem_pos_x = 2000
        if  i == 1:
            enemy_respawn_timer = pygame.time.get_ticks()
        i =65
        if pygame.time.get_ticks()-enemy_respawn_timer>=5000:
            golem_pos_x = 1400
            animation_state_golem = 'spawn'
            life_golem = 3
            i=1
    
    if animation_state_golem2 == 'dead':
        if animation_index_golem2 >=15:
            golem2_pos_x = 2000
        if  a == 1:
            enemy2_respawn_timer = pygame.time.get_ticks()
        a =65
        if pygame.time.get_ticks()-enemy2_respawn_timer>=5000:
            golem2_pos_x = -300
            animation_state_golem2 = 'spawn'
            life_golem2 = 3
            a=1
    
    #-------------------reaper dead-----------------------
    if animation_state_reaper == 'dead':
        if p==1:
            animation_index_reaper == 0
        
        if r=='right':
            if animation_index_reaper <15:
                screen.blit(reaper_dead_right[animation_index_reaper],(reaper_pos_x,reaper_pos_y))
                animation_index_reaper+=1
                
        if r=='left':
            if animation_index_reaper <15:
                screen.blit(reaper_dead_left[animation_index_reaper],(reaper_pos_x,reaper_pos_y))
                animation_index_reaper+=1
        if animation_index_golem >= 1:
            animation_state_golem = 'spawn'
        if animation_index_golem2 >= 1:
            animation_state_golem2 = 'spawn'
        p = 0
    
    #-------------Walk--------------
    if walk_right:
        reaper_pos_x += 10
        idle_reaper = 'right'
    if walk_left:
        reaper_pos_x -=10
        idle_reaper = 'left'        
     #-------------boundary----------------
    if animation_state_reaper != 'dead':
        if reaper_pos_x <=-80 :
            reaper_pos_x = -80
        if reaper_pos_x >=1310:
            reaper_pos_x = 1310
    
    #-------------------------if life < 0 : life =0--------------------
    if life < 0:
        life = 0
        life_text = font1.render('Life = {}'.format(life),True,(255,255,255))
        
    pygame.display.update()
    clock.tick(25)
    
pygame.quit()
        
    
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():    
    #初始化pygame、设置和屏幕对象  	
    pygame.init()    
    ai_settings = Settings()    
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))    	 
    pygame.display.set_caption("Alien Invasion")
    
    # 创建Play按钮    
    play_button = Button(ai_settings, screen, "Play")
    
    #创建一个用于存储游戏统计信息的实例,并创建记分牌    
    stats = GameStats(ai_settings)    
    sb = Scoreboard(ai_settings, screen, stats)        
    
    #创建一艘飞船    
    ship = Ship(ai_settings,screen)    
    
    #创建一个用于存储子弹的编组    
    bullets = Group()    
    aliens = Group()    
    
    #创建一个外星人    
    alien = Alien(ai_settings, screen)    
    
    #创建外星人群    
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #开始游戏的主循环    
    while True:        
    #监听键盘和鼠标事件             
    	gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)        
    	if stats.game_active:            
    	    ship.update()            
    	    gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)            
    	    gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)        
    	gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)        
    	
    	#删除已消失的子弹        
    	for bullet in bullets.copy():            
    	    if bullet.rect.bottom <= 0:                
    	        bullets.remove(bullet)        
    	print(len(bullets))
run_game()
